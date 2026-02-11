**Completed:** 2026-02-11

# BL-035: Add One-Command Setup and Doctor for Rules

**Phase:** Active (Untriaged)

## 1. Outcome
A single setup CLI provides beginner-safe installation of AI assistant rules for a chosen tool/project, with a `--doctor` mode that verifies discoverability and reports actionable fixes. Users can complete setup with one command instead of manual file placement.

## 2. Constraints & References
- Build on existing installer behavior in `scripts/install-implementation.py`; avoid duplicating install logic.
- Support both interactive mode (no args) and flag-driven mode for automation.
- Preserve non-destructive defaults (merge, skip existing unless `--force`).
- Keep dependencies to Python stdlib.
- Clarify user-level vs project-level applicability per tool (Codex supports `~/.codex/` config; most others are project/workspace-driven).

**References:** `scripts/install-implementation.py`, `implementations/*/README.md`, `implementations/README.md`, `backlog/done/bl-024-add-install-implementation-script.md`.

## 3. Acceptance Checks
- [x] New script exists (e.g., `scripts/setup-rules.py`) with interactive setup flow when no args are passed.
- [x] Script supports non-interactive flags (minimum: `--tool`, `--project`, `--scope`, `--force`, `--dry-run`).
- [x] Script can install one tool or all tools into isolated targets without collisions.
- [x] `--doctor` mode checks expected files for selected tool/project and prints clear pass/fail diagnostics.
- [x] Tool-specific guidance is emitted when user-level auto-discovery is not supported.
- [x] README/docs include quick-start examples for both interactive and flag-based usage.
- [x] Existing install script remains functional and backward compatible.

## 4. Explicit Non-Goals
- Adding network installers or package-manager distribution.
- Editing rule content semantics for each tool.
- Guaranteeing universal global/user-level auto-discovery across all assistant tools.
