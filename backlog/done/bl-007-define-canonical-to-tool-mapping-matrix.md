# BL-007: Define Canonical-to-Tool Mapping Matrix

**Phase:** Next  
**Completed:** 2026-02-11 — Created `ai-blindspots/CANONICAL_TOOL_MAPPING.md` with 28 principles mapped to Cursor/Claude/Codex/Gemini/Antigravity. Cursor paths documented; gaps flagged. Maintainer review pending.

## 1. Outcome
Mapping of each canonical principle to Cursor, Codex, Claude, Gemini, and Antigravity. Coverage complete for current principles; gaps explicitly flagged.

## 2. Constraints & References
- Canonical source: `ai-blindspots/rules/ai-coding-assistant-rules.md`, `ai-blindspots/articles/`.
- Tools: Cursor (ready), Claude Code, Codex, Gemini CLI, Antigravity (planned).
- See `ai-blindspots/TOOL_TRANSLATION_GUIDE.md` for translation principles.

**References:** `ai-blindspots/TOOL_TRANSLATION_GUIDE.md`, `implementations/README.md`.

## 3. Acceptance Checks
- [x] Matrix document exists.
- [x] All current canonical principles have a row per tool.
- [x] Gaps (no implementation or missing principle) explicitly flagged.
- [ ] Matrix reviewed for accuracy.

## 4. Explicit Non-Goals
- Implementing translations (tool configs).
- Parity check pipeline (BL-010).
- Translation checklists (BL-008).
