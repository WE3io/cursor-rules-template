#!/usr/bin/env python3
"""
One-command setup for AI assistant rules. Interactive when no args, flag-driven for automation.

Run from ai-assistant-rules repo root:
  python scripts/setup-rules.py                    # interactive
  python scripts/setup-rules.py --tool cursor --project .
  python scripts/setup-rules.py --doctor --tool cursor --project .
"""
import importlib.util
import sys
from pathlib import Path

# Load install_implementation from sibling script
_script_dir = Path(__file__).resolve().parent
_install_spec = importlib.util.spec_from_file_location(
    "install_implementation",
    _script_dir / "install-implementation.py",
)
_install_mod = importlib.util.module_from_spec(_install_spec)
_install_spec.loader.exec_module(_install_mod)

TOOLS = _install_mod.TOOLS
get_repo_root = _install_mod.get_repo_root
install_implementation = _install_mod.install_implementation

# Tools for "all" - exclude Antigravity to avoid .agent/ collision with Gemini
TOOLS_ALL = ["cursor", "claude", "codex", "gemini"]

# Doctor: required paths per tool (relative to project root)
DOCTOR_PATHS = {
    "cursor": [
        (".cursor/rules", "dir"),
        (".cursor/rules/always", "dir"),
    ],
    "claude": [
        (".claude/rules", "dir"),
        ("CLAUDE.md", "file"),
    ],
    "codex": [
        ("AGENTS.md", "file"),
    ],
    "gemini": [
        (".agent/rules", "dir"),
        ("GEMINI.md", "file"),
    ],
    "antigravity": [
        (".agent/rules", "dir"),
        ("GEMINI.md", "file"),
    ],
}

USER_LEVEL_TOOLS = ["codex"]
SCRIPT_NAME = "setup-rules.py"


def _get_script_path() -> str:
    script = Path(__file__).resolve()
    repo = script.parent.parent
    try:
        rel = script.relative_to(repo)
        return f"python {rel}"
    except ValueError:
        return f"python {script}"


def run_doctor(tool: str, project_dir: Path) -> int:
    """Check expected paths for tool; print pass/fail with actionable fixes."""
    project = project_dir.resolve()
    if tool not in DOCTOR_PATHS:
        print(f"Unknown tool: {tool}. Available: {', '.join(TOOLS)}", file=sys.stderr)
        return 1

    paths = DOCTOR_PATHS[tool]
    all_ok = True
    for rel_path, kind in paths:
        abs_path = project / rel_path
        if kind == "dir":
            exists = abs_path.is_dir()
            if exists:
                # Check for content (at least one file)
                has_content = any(abs_path.rglob("*")) if abs_path.exists() else False
                if not has_content:
                    exists = False
        else:
            exists = abs_path.is_file()

        if exists:
            print(f"  Found: {rel_path}")
        else:
            all_ok = False
            fix_cmd = f"{_get_script_path()} --tool {tool} --project {project}"
            print(f"  Missing: {rel_path} — run: {fix_cmd}")

    if all_ok:
        print(f"  All {tool} rule paths present.")
        return 0
    return 1


def interactive_setup() -> tuple[str, str, str, bool]:
    """Prompt user for tool, project, scope. Returns (tool, project, scope, doctor)."""
    print("Which tool? (cursor/claude/codex/gemini/antigravity/all)")
    tool_input = input("Tool [cursor]: ").strip().lower() or "cursor"

    print("Target directory? (default: current directory)")
    project_input = input("Project [.]: ").strip() or "."

    scope = "project"
    if tool_input == "codex":
        print("Scope? (project/user)")
        scope_input = input("Scope [project]: ").strip().lower() or "project"
        scope = scope_input if scope_input in ("project", "user") else "project"

    print("Run doctor to verify? (y/n)")
    doctor_input = input("Doctor [n]: ").strip().lower()
    doctor = doctor_input in ("y", "yes")

    return tool_input, project_input, scope, doctor


def resolve_target(tool: str, project: str, scope: str) -> Path:
    """Resolve target directory based on tool, project, and scope."""
    if scope == "user" and tool == "codex":
        # Install to ~/.codex/skills/ai-assistant-rules/
        return Path.home() / ".codex" / "skills" / "ai-assistant-rules"
    return Path(project).resolve()


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(
        description="Setup AI assistant rules for a chosen tool. Interactive when no args."
    )
    parser.add_argument(
        "--tool",
        choices=TOOLS + ["all"],
        help="Tool to install (or 'all' for cursor, claude, codex, gemini)",
    )
    parser.add_argument(
        "--project",
        "-p",
        default=".",
        help="Target directory (default: .)",
    )
    parser.add_argument(
        "--scope",
        choices=["project", "user"],
        default="project",
        help="project (default) or user (Codex only)",
    )
    parser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="Overwrite existing files",
    )
    parser.add_argument(
        "--dry-run",
        "-n",
        action="store_true",
        help="Show planned copies without making changes",
    )
    parser.add_argument(
        "--doctor",
        action="store_true",
        help="Verify rule discoverability; report missing paths",
    )
    args = parser.parse_args()

    # Interactive mode: no tool specified and stdin is TTY
    if args.tool is None:
        if sys.stdin.isatty():
            tool, project, scope, doctor = interactive_setup()
            args.tool = tool
            args.project = project
            args.scope = scope
            args.doctor = doctor
        else:
            print(
                "Non-interactive mode: use --tool, --project, etc.\n"
                f"Example: {_get_script_path()} --tool cursor --project .",
                file=sys.stderr,
            )
            return 1

    # Scope user: only Codex supported
    if args.scope == "user" and args.tool != "codex":
        print(
            f"Tool {args.tool} is project-level only. Use --scope project."
        )
        return 1

    repo_root = get_repo_root()

    if args.doctor:
        if args.tool == "all":
            print("Doctor: check each tool separately (e.g. --tool cursor)")
            return 1
        target = resolve_target(args.tool, args.project, args.scope)
        return run_doctor(args.tool, target)

    # Install
    if args.tool == "all":
        for t in TOOLS_ALL:
            target = resolve_target(t, args.project, "project")
            target_str = str(target)
            print(f"\n--- Installing {t} to {target_str} ---")
            rc = install_implementation(
                t, target_str, force=args.force, dry_run=args.dry_run, repo_root=repo_root
            )
            if rc != 0:
                return rc
        print("\nNote: Antigravity shares .agent/ with Gemini; install separately if needed.")
        return 0

    target = resolve_target(args.tool, args.project, args.scope)
    return install_implementation(
        args.tool,
        str(target),
        force=args.force,
        dry_run=args.dry_run,
        repo_root=repo_root,
    )


if __name__ == "__main__":
    sys.exit(main())
