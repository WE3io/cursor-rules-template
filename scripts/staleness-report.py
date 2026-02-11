#!/usr/bin/env python3
"""
Staleness report: List guidance items past review_date.
Threshold: stale = review_date has passed (YYYY-MM-DD).
Reads backlog/staleness-manifest.json.
"""

import json
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_FILE = REPO_ROOT / "backlog" / "staleness-manifest.json"


def main():
    if not MANIFEST_FILE.exists():
        print(f"Error: {MANIFEST_FILE} not found", file=sys.stderr)
        sys.exit(2)

    with open(MANIFEST_FILE) as f:
        data = json.load(f)

    items = data.get("items", [])
    today = date.today()
    stale = []

    for item in items:
        rd = item.get("review_date")
        if not rd:
            continue
        try:
            review_date = date.fromisoformat(rd)
        except (ValueError, TypeError):
            continue
        if review_date < today:
            stale.append({
                **item,
                "due_date": rd,
            })

    # Report
    lines = ["# Staleness Report\n"]
    lines.append(f"**Threshold:** stale = review_date has passed\n")
    lines.append(f"**Generated:** {today.isoformat()}\n\n")

    if not stale:
        lines.append("No stale items.\n")
        print("".join(lines))
        sys.exit(0)

    lines.append(f"**Stale items:** {len(stale)}\n\n")
    lines.append("| ID | Title | Owner | Due Date | Location |\n")
    lines.append("|----|-------|-------|----------|----------|\n")
    for s in stale:
        lines.append(f"| {s.get('id', '')} | {s.get('title', '')} | {s.get('owner', '')} | {s.get('due_date', '')} | {s.get('location', '')} |\n")

    print("".join(lines))
    sys.exit(1)


if __name__ == "__main__":
    main()
