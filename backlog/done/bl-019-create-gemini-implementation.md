**Completed:** 2026-02-11 — implementations/gemini/ with GEMINI.md, .agent/rules/, README. canonical-tool-mapping.json and implementations/README.md updated. Parity check run.

# BL-019: Create Gemini CLI Implementation

**Phase:** Later

## 1. Outcome
Gemini CLI implementation added under `implementations/gemini/`. GEMINI.md and .agent/rules/ translate canonical AI Blindspots principles. README with setup instructions. Parity check updated for Gemini.

## 2. Constraints & References
- Uses [gemini-translation.md](../../ai-blindspots/checklists/gemini-translation.md) for validation.
- Output: GEMINI.md, .agent/rules/ per Gemini conventions.
- Translate intent, not mechanism; no tool-specific references.
- Human review before commit.

**References:** BL-007, BL-008, BL-010, BL-016, [TOOL_TRANSLATION_GUIDE.md](../../ai-blindspots/TOOL_TRANSLATION_GUIDE.md).

## 3. Acceptance Checks
- [x] `implementations/gemini/GEMINI.md` exists with guidelines.
- [x] `.agent/rules/` structure created per Gemini conventions.
- [x] gemini-translation checklist applied; intent preserved.
- [x] Parity check run; canonical-tool-mapping.json updated for Gemini.
- [x] README with setup and usage instructions.
- [x] implementations/README.md table updated.

## 4. Explicit Non-Goals
- .agent/skills/; optional follow-up.
- Full parity (gaps acceptable; document in mapping).
