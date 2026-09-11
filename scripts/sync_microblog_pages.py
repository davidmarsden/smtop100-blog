#!/usr/bin/env python3
"""Publish source-controlled Top 100 pages to Micro.blog via Micropub.

The live standalone pages already exist in Micro.blog. This script updates those
pages in place so approved migration/pages/*.md sources can become the publishing
source of truth without creating duplicate pages or changing navigation.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

MICROPUB_ENDPOINT = "https://micro.blog/micropub"

PAGES = {
    "about": {
        "source": Path("migration/pages/about.md"),
        "url": "https://smtop100.blog/about/",
        "title": "About",
        "ready": True,
    },
    "contact": {
        "source": Path("migration/pages/contact.md"),
        "url": "https://smtop100.blog/contact/",
        "title": "Contact / Join",
        "ready": True,
    },
    "rules": {
        "source": Path("migration/pages/rules.md"),
        "url": "https://smtop100.blog/rules/",
        "title": "Rules",
        "ready": True,
    },
    "support": {
        "source": Path("migration/pages/support.md"),
        "url": "https://smtop100.blog/support/",
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


def publish_page(token: str, key: str, *, dry_run: bool = False) -> None:
    page = PAGES[key]
    content = page_body(page["source"])
    payload = {
        "action": "update",
        "url": page["url"],
        "replace": {
            "name": [page["title"]],
            "content": [content],
        },
    }

    if dry_run:
        state = "ready" if page["ready"] else "validation-only"
        print(
            f"DRY RUN {key} [{state}]: {page['source']} -> "
            f"{page['url']} ({len(content)} chars)"
        )
        return

    if not page["ready"]:
        raise RuntimeError(
            f"Refusing to publish {key}: source is not marked production-ready."
        )

    request = urllib.request.Request(
        MICROPUB_ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "smtop100-page-sync/1.1",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            status = response.status
            body = response.read().decode("utf-8", errors="replace").strip()
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace").strip()
        raise RuntimeError(
            f"Micro.blog rejected {key} ({exc.code}): {body or exc.reason}"
        ) from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not reach Micro.blog for {key}: {exc.reason}") from exc

    if status < 200 or status >= 300:
        raise RuntimeError(f"Unexpected Micro.blog response for {key}: HTTP {status} {body}")

    print(f"Published {key}: {page['url']} (HTTP {status})")


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
        for key in selected:
            publish_page(token, key, dry_run=args.dry_run)
    except (RuntimeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
