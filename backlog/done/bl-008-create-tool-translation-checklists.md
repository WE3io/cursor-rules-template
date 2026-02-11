# BL-008: Create Tool Translation Checklists

**Phase:** Next  
**Completed:** 2026-02-11 — Created five per-tool checklists in `ai-blindspots/checklists/`. Cursor rules README now references cursor-translation checklist for validation.

## 1. Outcome
Per-tool validation checklist for semantic parity. Each tool has a checklist that verifies intent preservation and mechanism adaptation.

## 2. Constraints & References
- Tools: Cursor, Claude Code, Codex, Gemini CLI, Antigravity.
- Aligns with BL-007 Mapping Matrix and `ai-blindspots/TOOL_TRANSLATION_GUIDE.md`.
- Principle: translate intent, not mechanism.

**References:** `ai-blindspots/TOOL_TRANSLATION_GUIDE.md`, `ai-blindspots/examples/translation-examples.md`.

## 3. Acceptance Checks
- [x] Each tool has a checklist document.
- [x] Checklist verifies intent preservation.
- [x] Checklist verifies mechanism adaptation (tool-specific format).
- [x] Checklist used in at least one translation review.

## 4. Explicit Non-Goals
- Automating parity checks (BL-010).
- Implementing translations.
- Mapping matrix (BL-007).
