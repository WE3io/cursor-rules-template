**Completed:** 2026-02-11 — Install script added; merge/force/dry-run; README and Installation docs updated.

# BL-024: Add Install Implementation Script

**Phase:** Later

## 1. Outcome
An install script that copies a chosen implementation (Claude, Cursor, Gemini, Antigravity, Codex) into a target directory, placing rule files and bundled docs in the correct locations for standalone use. Automation replaces manual copy steps.

## 2. Constraints & References
- Follows pattern of [scripts/sync-bundled-docs.py](../../scripts/sync-bundled-docs.py): Python stdlib, resolve repo root from `__file__`.
- Must preserve dotfiles (`.claude/`, `.cursor/`, `.agent/`, `.codex/`).
- Default: merge without overwriting existing files (protect user customizations).
- Script runnable from cursorrules repo or from target project (pass script path).

**References:** [implementations/](../../implementations/), [2026-02-11-bundled-docs-exploration.md](../decisions/2026-02-11-bundled-docs-exploration.md), BL-022, BL-023.

## 3. Design (Refinements)

### Invocation
```bash
python scripts/install-implementation.py <tool> [target_dir]

# Examples
python scripts/install-implementation.py claude .                    # into current dir
python scripts/install-implementation.py cursor /path/to/my-project   # into project
python scripts/install-implementation.py claude                      # target defaults to .
python scripts/install-implementation.py                             # list available tools
```

### Merge behavior
- **Default:** Copy files; skip if destination already exists (merge-only).
- **`--force` / `-f`:** Overwrite existing files.
- **`--dry-run` / `-n`:** Show what would be copied; no changes.

### README handling
- Copy implementation README to `docs/ai-blindspots-<tool>-README.md` in target to avoid overwriting project README.
- If `docs/` does not exist, create it.

### Error handling
- Unknown tool → list available tools, exit 1.
- Source (implementation folder) not found → exit 1.
- Target not writable → clear error, exit 1.
- Target missing → create if parent exists; else exit 1.

### Degit alternative (documentation only)
- Add to implementations README: `npx degit <org>/cursorrules/implementations/<tool> .` for users who prefer degit (requires Node, network).

## 4. Acceptance Checks
- [x] Script exists at `scripts/install-implementation.py`.
- [x] Script accepts `claude`, `cursor`, `gemini`, `antigravity`, `codex` (case-insensitive).
- [x] No args or `--list` prints available tools.
- [x] Default merge: skip existing files; `--force` overwrites.
- [x] `--dry-run` shows planned copies; no side effects.
- [x] Implementation README copied to `docs/ai-blindspots-<tool>-README.md` (not project root README).
- [x] Dotfiles (`.claude`, `.cursor`, `.agent`, `.codex`) copied correctly.
- [x] No external deps beyond Python stdlib.
- [x] implementations/README.md documents install script usage and degit alternative.
- [x] Root README or implementations/README links to install instructions.

## 5. Explicit Non-Goals
- curl|bash one-liner (security; out of scope).
- npx create-* package (publishing npm package).
- Interactive prompts (CLI args only).
- Modifying implementation content during install.
