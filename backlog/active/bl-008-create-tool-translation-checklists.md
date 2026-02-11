# BL-008: Create Tool Translation Checklists

**Phase:** Next

## 1. Outcome
Per-tool validation checklist for semantic parity. Each tool has a checklist that verifies intent preservation and mechanism adaptation.

## 2. Constraints & References
- Tools: Cursor, Claude Code, Codex, Gemini CLI, Antigravity.
- Aligns with BL-007 Mapping Matrix and `ai-blindspots/TOOL_TRANSLATION_GUIDE.md`.
- Principle: translate intent, not mechanism.

**References:** `ai-blindspots/TOOL_TRANSLATION_GUIDE.md`, `ai-blindspots/examples/translation-examples.md`.

## 3. Acceptance Checks
- [ ] Each tool has a checklist document.
- [ ] Checklist verifies intent preservation.
- [ ] Checklist verifies mechanism adaptation (tool-specific format).
- [ ] Checklist used in at least one translation review.

## 4. Explicit Non-Goals
- Automating parity checks (BL-010).
- Implementing translations.
- Mapping matrix (BL-007).
