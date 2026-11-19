"""Fill the Transfer Bans page's current and recent bans from the live register.

migration/pages/transfer-bans.md marks two blocks:

    <!-- live:current -->  ...  <!-- /live:current -->
    <!-- live:recent -->   ...  <!-- /live:recent -->
    <!-- live:table -->    ...  <!-- /live:table -->

At publish time each block is replaced with the bans from the Manager Portal's public register
(bans in force, and bans ended since September 2026, with their required sales and whether each
has been made). The text written between the markers in the repo is the fallback, used only when
the register can't be read. The markers themselves are never published.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import urllib.error
import urllib.request

FEED_URL = os.environ.get(
    "TRANSFER_BANS_FEED", "https://tournaments.smtop100.blog/.netlify/functions/transfer-bans"
)
BLOCK = re.compile(r"<!-- live:(?P<name>[a-z]+) -->\n(?P<body>.*?)<!-- /live:(?P=name) -->\n?", re.S)
LADDER_MONTHS = {1: 1, 2: 3, 3: 4, 4: 6}
MONTH_WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six"}
ORDINALS = {1: "first", 2: "second", 3: "third", 4: "fourth"}


def fetch_register(url: str = FEED_URL) -> dict:
    request = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "smtop100-page-sync/1.4"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8"))
    # URLError and read timeouts are OSErrors; bad JSON or encoding are ValueErrors.
    except (OSError, ValueError) as exc:
        raise RuntimeError(f"Could not read the transfer ban register at {url}: {exc}") from exc
    bans = payload.get("bans")
    if not isinstance(bans, list):
        raise RuntimeError(f"The transfer ban register at {url} returned no list of bans")
    return payload


def long_date(value: str) -> str:
    d = dt.date.fromisoformat(str(value)[:10])
    return f"{d.day} {d.strftime('%B %Y')}"


def player(name: str) -> str:
    # "E.FORSBERG" -> "E. FORSBERG"
    return re.sub(r"\.(?=\S)", ". ", str(name).strip())


def sale_text(sale: dict) -> str:
    players = [player(p) for p in sale.get("players") or []]
    who = players[0] if len(players) == 1 else "one of " + ", ".join(players[:-1]) + " or " + players[-1]
    return f"{who} ({'sold' if sale.get('made') else 'to sell'})"


def months_between(start: str, end: str) -> int:
    a, b = dt.date.fromisoformat(start[:10]), dt.date.fromisoformat(end[:10])
    return max(1, round((b - a).days / 30.4))


def ban_text(ban: dict) -> str:
    level = ban.get("level")
    months = LADDER_MONTHS.get(level) or months_between(ban["startsOn"], ban["endsOn"])
    length = f"{MONTH_WORDS.get(months, str(months))}-month ban"
    offence = f" for a {ORDINALS[level]} level offence" if level in ORDINALS else ""
    text = f"**{ban.get('manager') or 'Unknown manager'} ({ban.get('club')}):** {length}{offence}, from {long_date(ban['startsOn'])} to {long_date(ban['endsOn'])}"
    if ban.get("shortened"):
        text += ", shortened after the manager passed the rules check"
    text += "."
    sales = ban.get("sales") or []
    if sales:
        label = "Required sale" if len(sales) == 1 else "Required sales"
        text += f" {label}, to a club outside Top 100 for cash: " + "; ".join(sale_text(s) for s in sales) + "."
    return text


def months_text(days: int) -> str:
    months = max(1, round(int(days) / 30.4))
    return f"{months} month{'' if months == 1 else 's'}"


def table_text(table: dict) -> str:
    """The managers with the most bans: a Markdown table plus the totals."""
    totals = table.get("totals") or {}
    rows = table.get("managers") or []
    lines = [
        "| | Manager | Bans | Time banned | Longest ban | Latest ban |",
        "|---|---|---|---|---|---|",
    ]
    rank = 0
    previous = None
    for index, row in enumerate(rows, 1):
        key = (row.get("bans"), row.get("days"))
        if key != previous:
            rank, previous = index, key
        latest = dt.date.fromisoformat(str(row["lastStarted"])[:10]).strftime("%B %Y")
        name = row.get("manager") or "Unknown manager"
        if row.get("bannedNow"):
            name += " (banned now)"
        lines.append(f"| {rank} | {name} | {row.get('bans')} | {months_text(row.get('days') or 0)} | "
                     f"{months_text(row.get('longestDays') or 0)} | {latest} |")
    lines.append("")
    if totals:
        lines.append(f"*{totals.get('bans')} bans for {totals.get('managers')} managers on record since {totals.get('firstYear')}, "
                     f"about {round((totals.get('days') or 0) / 365.25, 1)} years of transfer bans in all. Ranked by bans, then time banned. "
                     "Records from before 2023 may be incomplete.*")
    return "\n".join(lines) + "\n\n"


def render(payload, today: dt.date) -> dict[str, str]:
    bans = payload.get("bans", []) if isinstance(payload, dict) else payload
    table = payload.get("table") if isinstance(payload, dict) else None
    current = [b for b in bans if b.get("current")]
    recent = [b for b in bans if not b.get("current")]

    lines = [f"*Updated every day. Last updated {long_date(today.isoformat())}.*", ""]
    if current:
        for ban in current:
            item = ban_text(ban)
            # Sales from the same club's earlier bans that are still to be made.
            earlier = [
                sale_text(s)
                for b in recent
                if b.get("club") == ban.get("club") and b.get("manager") == ban.get("manager")
                for s in b.get("sales") or []
                if not s.get("made")
            ]
            if earlier:
                item += " Still to sell from an earlier ban: " + "; ".join(earlier) + "."
            lines.append(f"- {item}")
    else:
        lines.append("No transfer bans are in force.")

    blocks = {
        "current": "\n".join(lines) + "\n\n",
        "recent": "".join(f"- {ban_text(ban)}\n" for ban in recent),
    }
    # Without the table (an older feed, or it failed), the repo's fallback text stays.
    if table and table.get("managers"):
        blocks["table"] = table_text(table)
    return blocks


def apply(text: str, *, require: bool = False, today: dt.date | None = None) -> str:
    """Replace the live blocks with the register; on failure keep the fallback text unless require."""
    if not BLOCK.search(text):
        return text
    try:
        blocks = render(fetch_register(), today or dt.date.today())
    except RuntimeError as exc:
        if require:
            raise
        print(f"transfer-bans: {exc}; publishing the text in the repo instead")
        blocks = None

    def replace(match: re.Match) -> str:
        if blocks is None or match["name"] not in blocks:
            return match["body"]
        return blocks[match["name"]]

    return BLOCK.sub(replace, text)
