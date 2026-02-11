**Completed:** 2026-02-11 — Parity report now separates ok/partial/gap in console and JSON while preserving existing fail-on-gap behavior.

# BL-025: Fix Parity Status Accounting and Reporting

**Phase:** Now

## 1. Outcome
Parity reporting distinguishes `ok`, `partial`, and `gap` statuses explicitly, and no longer reports `partial` coverage as fully covered. Output is accurate in both console report and `parity-report.json`.

## 2. Constraints & References
- Keep existing script entrypoint and usage (`python3 scripts/parity-check.py`).
- Backward compatibility: preserve current top-level JSON keys and add new keys if needed.
- Treat this as reporting semantics only; do not introduce policy changes in this item.

**References:** `scripts/parity-check.py`, `ai-blindspots/canonical-tool-mapping.json`, `backlog/done/bl-010-add-parity-check-pipeline.md`.

## 3. Acceptance Checks
- [x] `scripts/parity-check.py` reports counts separately for `ok`, `partial`, and `gap` by tool.
- [x] Console wording no longer conflates `gap` with `partial`.
- [x] `parity-report.json` includes machine-parseable status breakdown by tool.
- [x] Existing behavior for exit code on configured failures remains unchanged in this item.
- [x] Running `python3 scripts/parity-check.py` completes successfully and produces updated report output.

## 4. Explicit Non-Goals
- Enabling new fail policies (handled by BL-026).
- Filling any missing translation content.
- Modifying CI workflow triggers.
