**Completed:** 2026-02-11 — implementations/antigravity/ with GEMINI.md, .agent/rules/, terminal-policy.md, README. canonical-tool-mapping.json and implementations/README.md updated. Parity check run.

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
- [x] `implementations/antigravity/` contains primary config (GEMINI.md or AGENT.md).
- [x] `.agent/rules/` structure created per Antigravity conventions.
- [x] antigravity-translation checklist applied; intent preserved.
- [x] Parity check run; canonical-tool-mapping.json updated for Antigravity.
- [x] README with setup and usage instructions.
- [x] implementations/README.md table updated.

## 4. Explicit Non-Goals
- .agent/skills/; optional follow-up.
- Full parity (gaps acceptable; document in mapping).
