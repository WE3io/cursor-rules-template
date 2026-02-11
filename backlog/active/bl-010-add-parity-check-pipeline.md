# BL-010: Add Parity Check Pipeline

**Phase:** Next

## 1. Outcome
Automated canonical-to-tool coverage/parity report. Report generated in CI; missing mappings surfaced as failures or warnings.

## 2. Constraints & References
- Depends on BL-007 Mapping Matrix (or equivalent).
- Canonical source: `ai-blindspots/`.
- Tools: Cursor, Claude, Codex, Gemini, Antigravity.
- Report must be machine-parseable or human-readable.

**References:** BL-007, `ai-blindspots/TOOL_TRANSLATION_GUIDE.md`.

## 3. Acceptance Checks
- [ ] Report generated in CI.
- [ ] Report surfaces missing mappings.
- [ ] Failures or warnings configured (e.g. missing = warn vs fail).
- [ ] Report usable for triage.

## 4. Explicit Non-Goals
- Docs QA pipeline (BL-009).
- Implementing missing translations.
- Staleness tracking (BL-011).
