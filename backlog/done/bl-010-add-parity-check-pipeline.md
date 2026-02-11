# BL-010: Add Parity Check Pipeline

**Phase:** Next  
**Completed:** 2026-02-11 — Added `scripts/parity-check.py`, `ai-blindspots/canonical-tool-mapping.json`, `.github/workflows/parity-check.yml`. Report surfaces gaps; fail_on_gap configurable.

## 1. Outcome
Automated canonical-to-tool coverage/parity report. Report generated in CI; missing mappings surfaced as failures or warnings.

## 2. Constraints & References
- Depends on BL-007 Mapping Matrix (or equivalent).
- Canonical source: `ai-blindspots/`.
- Tools: Cursor, Claude, Codex, Gemini, Antigravity.
- Report must be machine-parseable or human-readable.

**References:** BL-007, `ai-blindspots/TOOL_TRANSLATION_GUIDE.md`.

## 3. Acceptance Checks
- [x] Report generated in CI.
- [x] Report surfaces missing mappings.
- [x] Failures or warnings configured (e.g. missing = warn vs fail).
- [x] Report usable for triage.

## 4. Explicit Non-Goals
- Docs QA pipeline (BL-009).
- Implementing missing translations.
- Staleness tracking (BL-011).
