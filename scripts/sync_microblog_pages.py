#!/usr/bin/env python3
"""Publish source-controlled Top 100 pages to Micro.blog via Micropub.

The live standalone pages already exist in Micro.blog. This script updates those
pages in place so approved migration/pages/*.md sources can become the publishing
source of truth without creating duplicate pages or changing navigation.

Standalone pages live in Micro.blog's dedicated ``pages`` Micropub channel. Their
update identifiers must be discovered from that channel rather than guessed from
the public or ``*.micro.blog`` URL.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

MICROPUB_ENDPOINT = "https://micro.blog/micropub"
MICROPUB_DESTINATION = "https://smtop100.micro.blog/"
DISCOVERY_PAGE_SIZE = 100

PAGES = {
    "about": {
        "source": Path("migration/pages/about.md"),
        "public_url": "https://smtop100.blog/about/",
        "title": "About",
        "ready": True,
    },
    "contact": {
        "source": Path("migration/pages/contact.md"),
        "public_url": "https://smtop100.blog/contact/",
        "title": "Contact / Join",
        "ready": True,
    },
    "rules": {
        "source": Path("migration/pages/rules.md"),
        "public_url": "https://smtop100.blog/rules/",
        "title": "Rules",
        "ready": True,
    },
    "support": {
        "source": Path("migration/pages/support.md"),
        "public_url": "https://smtop100.blog/support/",
        "title": "Support Top 100",
        "ready": True,
    },
}


def page_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n").strip()
    # Micro.blog renders the standalone page title itself. Keep the Markdown
    # sources pleasant to read in GitHub, but avoid duplicating the first H1
    # on the live page.
    text = re.sub(r"^#\s+[^\n]+\n+", "", text, count=1).strip()
    if not text:
        raise ValueError(f"Managed page body is empty after heading removal: {path}")
    return text + "\n"


def micropub_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "smtop100-page-sync/1.3",
    }


def discover_pages(token: str) -> list[dict]:
    """Return all standalone-page records Micro.blog exposes via Micropub."""
    discovered: list[dict] = []
    offset = 0

    while True:
        params = urllib.parse.urlencode(
            {
                "q": "source",
                "mp-channel": "pages",
                "mp-destination": MICROPUB_DESTINATION,
                "limit": DISCOVERY_PAGE_SIZE,
                "offset": offset,
            }
        )
        request = urllib.request.Request(
            f"{MICROPUB_ENDPOINT}?{params}",
            method="GET",
            headers=micropub_headers(token),
        )

        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                body = response.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace").strip()
            raise RuntimeError(
                f"Micro.blog rejected standalone-page discovery ({exc.code}): "
                f"{body or exc.reason}"
            ) from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(
                f"Could not reach Micro.blog while discovering standalone pages: {exc.reason}"
            ) from exc

        try:
            payload = json.loads(body)
        except json.JSONDecodeError as exc:
            raise RuntimeError("Micro.blog returned invalid JSON for standalone-page discovery") from exc

        items = payload.get("items")
        if not isinstance(items, list):
            raise RuntimeError("Micro.blog standalone-page discovery returned no items list")

        discovered.extend(items)
        print(
            f"Discovered standalone Micro.blog page batch at offset {offset}: "
            f"{len(items)} item(s)."
        )

        if len(items) < DISCOVERY_PAGE_SIZE:
            break
        offset += DISCOVERY_PAGE_SIZE

    print(f"Discovered {len(discovered)} standalone Micro.blog page(s) in total.")
    return discovered


def first_property(item: dict, name: str) -> str:
    values = item.get("properties", {}).get(name, [])
    if isinstance(values, list) and values:
        return str(values[0] or "").strip()
    if isinstance(values, str):
        return values.strip()
    return ""


def resolve_page_url(key: str, discovered: list[dict]) -> str:
    """Match a managed page to Micro.blog's exact update URL."""
    page = PAGES[key]
    wanted_path = urllib.parse.urlparse(page["public_url"]).path.rstrip("/") or "/"
    wanted_title = page["title"].casefold()

    title_match = None
    available = []
    for item in discovered:
        item_url = first_property(item, "url")
        item_title = first_property(item, "name")
        if item_url or item_title:
            available.append(f"{item_title or '(untitled)'} -> {item_url or '(no URL)'}")

        if item_url:
            item_path = urllib.parse.urlparse(item_url).path.rstrip("/") or "/"
            if item_path == wanted_path:
                return item_url

        if item_title.casefold() == wanted_title and item_url:
            title_match = item_url

    if title_match:
        return title_match

    detail = "; ".join(available) if available else "none"
    raise RuntimeError(
        f"Could not find managed page {key!r} in Micro.blog's pages channel. "
        f"Available pages: {detail}"
    )


def publish_page(
    token: str,
    key: str,
    *,
    discovered: list[dict] | None = None,
    dry_run: bool = False,
) -> None:
    page = PAGES[key]
    content = page_body(page["source"])

    if dry_run:
        state = "ready" if page["ready"] else "validation-only"
        print(
            f"DRY RUN {key} [{state}]: {page['source']} -> "
            f"discover from Micropub pages channel (public {page['public_url']}; "
            f"{len(content)} chars)"
        )
        return

    if not page["ready"]:
        raise RuntimeError(
            f"Refusing to publish {key}: source is not marked production-ready."
        )
    if discovered is None:
        raise RuntimeError("Standalone pages were not discovered before publishing")

    target_url = resolve_page_url(key, discovered)
    payload = {
        "action": "update",
        "url": target_url,
        "replace": {
            "name": [page["title"]],
            "content": [content],
        },
    }

    headers = micropub_headers(token)
    headers["Content-Type"] = "application/json; charset=utf-8"
    request = urllib.request.Request(
        MICROPUB_ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers=headers,
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            status = response.status
            body = response.read().decode("utf-8", errors="replace").strip()
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace").strip()
        raise RuntimeError(
            f"Micro.blog rejected {key} ({exc.code}) for discovered target {target_url}: "
            f"{body or exc.reason}"
        ) from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not reach Micro.blog for {key}: {exc.reason}") from exc

    if status < 200 or status >= 300:
        raise RuntimeError(f"Unexpected Micro.blog response for {key}: HTTP {status} {body}")

    print(
        f"Published {key}: {page['public_url']} "
        f"(discovered Micropub target {target_url}; HTTP {status})"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "pages",
        nargs="*",
        choices=sorted(PAGES),
        help="Managed page keys to validate/publish. Omit to use production-ready pages only.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Select all managed pages. Intended for validation; unready pages still cannot publish.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Validate sources without publishing.")
    args = parser.parse_args()

    if args.all and args.pages:
        parser.error("--all cannot be combined with explicit page keys")

    ready_pages = [key for key, page in PAGES.items() if page["ready"]]
    selected = list(PAGES) if args.all else (args.pages or ready_pages)

    missing = [
        str(PAGES[key]["source"])
        for key in selected
        if not PAGES[key]["source"].is_file()
    ]
    if missing:
        print("Missing source page(s): " + ", ".join(missing), file=sys.stderr)
        return 2

    token = os.environ.get("MICROBLOG_TOKEN", "").strip()
    if not args.dry_run and not token:
        print("MICROBLOG_TOKEN is required unless --dry-run is used.", file=sys.stderr)
        return 2

    try:
        discovered = None if args.dry_run else discover_pages(token)
        for key in selected:
            publish_page(token, key, discovered=discovered, dry_run=args.dry_run)
    except (RuntimeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
