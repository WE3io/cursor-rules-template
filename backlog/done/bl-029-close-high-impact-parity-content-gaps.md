**Completed:** 2026-02-11

# BL-029: Close High-Impact Parity Content Gaps

**Phase:** Now

## 1. Outcome
High-impact parity gaps identified by mapping/reporting are addressed in tool implementations so coverage improves for foundational principles currently marked as `gap`.

## 2. Constraints & References
- Scope this item to currently flagged high-impact principles:
  - `type-systems`
  - `static-types`
  - `stateless-commands`
  - `knowledge-limitations`
  - Cursor-specific `file-size-limits`
- Translate intent, not mechanism, per canonical translation guidance.
- Keep edits localized to implementation artifacts and related mapping updates needed to reflect new status.

**References:** `ai-blindspots/canonical-tool-mapping.json`, `ai-blindspots/TOOL_TRANSLATION_GUIDE.md`, `ai-blindspots/checklists/`, `implementations/`, `parity-report.json`.

## 3. Acceptance Checks
- [x] Required principles are implemented in relevant tool outputs or documentation references.
- [x] Mapping file status updates reflect actual post-change state for affected principles/tools.
- [x] `python3 scripts/parity-check.py` shows reduced `gap` count for targeted principles.
- [x] Updated implementation docs/rules pass configured CI checks for this change (parity/staleness; docs QA workflow is PR-only).
- [x] Any introduced wording remains tool-appropriate and consistent with canonical intent.

## 4. Explicit Non-Goals
- Rewriting the full canonical ruleset.
- Achieving zero parity gaps across all principles in one change.
- Changing parity policy behavior (handled by BL-025/BL-026).
