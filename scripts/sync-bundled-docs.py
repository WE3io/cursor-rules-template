#!/usr/bin/env python3
"""
Sync bundled AI Blindspots articles from ai-blindspots/ into implementation docs folders.

Run from repo root: python scripts/sync-bundled-docs.py
Run when: ai-blindspots articles change, or before release.

Manifest: backlog/manifests/bundled-docs-mapping.json
"""
import json
import shutil
from pathlib import Path


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    manifest_path = repo_root / "backlog" / "manifests" / "bundled-docs-mapping.json"

    with open(manifest_path) as f:
        data = json.load(f)

    for entry in data["bundled_articles"]:
        source = repo_root / entry["source"]
        for dest_rel in entry["destinations"]:
            dest = repo_root / dest_rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, dest)
            print(f"Copied {source.name} -> {dest_rel}")


if __name__ == "__main__":
    main()
