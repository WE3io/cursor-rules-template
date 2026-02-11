# BL-020: Create Antigravity Implementation

**Phase:** Later

## 1. Outcome
Antigravity implementation added under `implementations/antigravity/`. GEMINI.md or AGENT.md and .agent/rules/ translate canonical AI Blindspots principles. README with setup instructions. Parity check updated for Antigravity.

## 2. Constraints & References
- Uses [antigravity-translation.md](../../ai-blindspots/checklists/antigravity-translation.md) for validation.
- Output: GEMINI.md or AGENT.md, .agent/rules/ per Antigravity conventions.
- Translate intent, not mechanism; no tool-specific references.
- Human review before commit.

**References:** BL-007, BL-008, BL-010, BL-016, [TOOL_TRANSLATION_GUIDE.md](../../ai-blindspots/TOOL_TRANSLATION_GUIDE.md).

## 3. Acceptance Checks
- [ ] `implementations/antigravity/` contains primary config (GEMINI.md or AGENT.md).
- [ ] `.agent/rules/` structure created per Antigravity conventions.
- [ ] antigravity-translation checklist applied; intent preserved.
- [ ] Parity check run; canonical-tool-mapping.json updated for Antigravity.
- [ ] README with setup and usage instructions.
- [ ] implementations/README.md table updated.

## 4. Explicit Non-Goals
- .agent/skills/; optional follow-up.
- Full parity (gaps acceptable; document in mapping).
