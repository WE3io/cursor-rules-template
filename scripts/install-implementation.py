#!/usr/bin/env python3
"""
Install AI Blindspots implementation into a target directory.

Copies a chosen implementation (claude, cursor, gemini, antigravity, codex) into
the target directory. Default: merge without overwriting. Use --force to overwrite.

Run from ai-assistant-rules repo root, or by path: python scripts/install-implementation.py <tool> [target_dir]
"""
import argparse
import shutil
import sys
from pathlib import Path
from typing import Optional

TOOLS = ["claude", "cursor", "gemini", "antigravity", "codex"]


def get_repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def list_tools() -> None:
    print("Available implementations:", ", ".join(TOOLS))
    print("Usage: python scripts/install-implementation.py <tool> [target_dir]")


def install_implementation(
    tool: str,
    target_dir: str,
    *,
    force: bool = False,
    dry_run: bool = False,
    repo_root: Optional[Path] = None,
) -> int:
    """
    Install a tool implementation into target_dir.
    Returns 0 on success, 1 on failure.
    """
    tool = tool.lower()
    if tool not in TOOLS:
        print(f"Unknown tool: {tool}. Available: {', '.join(TOOLS)}", file=sys.stderr)
        return 1

    root = repo_root or get_repo_root()
    source = root / "implementations" / tool
    if not source.is_dir():
        print(f"Implementation not found: {source}", file=sys.stderr)
        return 1

    target = Path(target_dir).resolve()
    if not target.exists():
        target.mkdir(parents=True, exist_ok=True)

    try:
        for path in source.rglob("*"):
            if path.is_dir():
                continue
            rel = path.relative_to(source)
            if path.name == "README.md" and path.parent == source:
                dest = target / "docs" / f"ai-blindspots-{tool}-README.md"
            else:
                dest = target / rel
            if dest.exists() and not force:
                print(f"Skipped (exists): {dest}")
            elif dry_run:
                print(f"Would copy: {path} -> {dest}")
            else:
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, dest)
                dest_rel = dest.relative_to(target)
                print(f"Copied: {dest_rel}")
    except PermissionError as e:
        print(f"Permission denied: {e}", file=sys.stderr)
        return 1

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Install AI Blindspots implementation into a target directory."
    )
    parser.add_argument(
        "tool",
        nargs="?",
        help="Implementation to install (claude, cursor, gemini, antigravity, codex)",
    )
    parser.add_argument(
        "target_dir",
        nargs="?",
        default=None,
        help="Target directory (default: current directory)",
    )
    parser.add_argument(
        "-t", "--target",
        dest="target_dir",
        help="Target directory (alternative to positional)",
    )
    parser.add_argument(
        "-f", "--force",
        action="store_true",
        help="Overwrite existing files",
    )
    parser.add_argument(
        "-n", "--dry-run",
        action="store_true",
        help="Show planned copies without making changes",
    )
    parser.add_argument(
        "-l", "--list",
        action="store_true",
        help="List available tools",
    )
    args = parser.parse_args()

    if args.list or args.tool is None:
        list_tools()
        return 0

    target_dir = args.target_dir or "."

    return install_implementation(
        args.tool,
        target_dir,
        force=args.force,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    sys.exit(main())
