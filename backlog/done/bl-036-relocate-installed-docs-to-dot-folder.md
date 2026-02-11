**Completed:** 2026-02-11 — Installed docs relocated to `.ai-assistant-rules/docs/`; symlinks added for link checker.

# BL-036: Relocate Installed Docs to `.ai-assistant-rules/docs/`

**Phase:** Later

## 1. Outcome

When rules are installed into a target repository, bundled docs and the implementation README are placed under `.ai-assistant-rules/docs/` instead of `docs/`. This isolates AI-assistant content from project documentation, avoids collision with existing `docs/` folders, and allows the folder to be gitignored safely if desired.

## 2. Constraints & References

- Project has not been publicised; no backward compatibility or migration for existing installs required.
- Implementation source structure (`implementations/<tool>/docs/`) stays unchanged; only the install script relocates during copy.
- `scripts/sync-bundled-docs.py` remains unchanged (writes to implementation folders; install script handles relocation).
- Rule files use relative paths; all doc references must be updated to the new destination.

**References:** [scripts/install-implementation.py](../../scripts/install-implementation.py), [backlog/done/bl-024-add-install-implementation-script.md](../done/bl-024-add-install-implementation-script.md), [backlog/done/bl-021-bundle-referenced-docs-design.md](../done/bl-021-bundle-referenced-docs-design.md).

## 3. Acceptance Checks

- [x] Install script relocates `docs/` to `target/.ai-assistant-rules/docs/` (all files under implementation `docs/`).
- [x] Install script relocates implementation README to `target/.ai-assistant-rules/docs/ai-blindspots-<tool>-README.md`.
- [x] Cursor rule paths updated: `workflows.mdc` → `../../../.ai-assistant-rules/docs/articles/...`; `README.md` and `review-checklist.mdc` → `../../.ai-assistant-rules/docs/aca_usage_guide.md` etc.
- [x] Claude/Gemini/Antigravity rule paths updated: `security.md`, `debugging.md` → `../../.ai-assistant-rules/docs/articles/...`.
- [x] `implementations/cursor/docs/cursor_rules_best_practices.md` internal reference updated (line 415: ACA guide path).
- [x] All implementation READMEs updated: structure diagram, doc paths, and bundled-docs note reference `.ai-assistant-rules/docs/`.
- [x] `implementations/README.md` and root README (if relevant) document new install layout.
- [x] Install dry-run and fresh install verify links resolve correctly.
- [x] CI (docs QA, parity) passes.

## 4. Explicit Non-Goals

- Backward compatibility flag or migration for existing installs.
- Modifying `scripts/sync-bundled-docs.py` or `backlog/manifests/bundled-docs-mapping.json`.
- Adding `.ai-assistant-rules/` to target `.gitignore` automatically (document only; user opt-in).
