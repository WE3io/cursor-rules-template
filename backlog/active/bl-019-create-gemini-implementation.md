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
- [ ] `implementations/gemini/GEMINI.md` exists with guidelines.
- [ ] `.agent/rules/` structure created per Gemini conventions.
- [ ] gemini-translation checklist applied; intent preserved.
- [ ] Parity check run; canonical-tool-mapping.json updated for Gemini.
- [ ] README with setup and usage instructions.
- [ ] implementations/README.md table updated.

## 4. Explicit Non-Goals
- .agent/skills/; optional follow-up.
- Full parity (gaps acceptable; document in mapping).
