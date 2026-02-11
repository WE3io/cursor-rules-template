**Completed:** 2026-02-11 — implementations/codex/ with AGENTS.md, .codex/config.toml, README. canonical-tool-mapping.json and implementations/README.md updated. Parity check run.

# BL-018: Create Codex Implementation

**Phase:** Later

## 1. Outcome
Codex implementation added under `implementations/codex/`. AGENTS.md and .codex/ structure translate canonical AI Blindspots principles. README with setup instructions. Parity check updated for Codex.

## 2. Constraints & References
- Uses [codex-translation.md](../../ai-blindspots/checklists/codex-translation.md) for validation.
- Output: AGENTS.md at project root, .codex/ structure per Codex conventions.
- Translate intent, not mechanism; no tool-specific references.
- Human review before commit.

**References:** BL-007, BL-008, BL-010, BL-016, [TOOL_TRANSLATION_GUIDE.md](../../ai-blindspots/TOOL_TRANSLATION_GUIDE.md).

## 3. Acceptance Checks
- [x] `implementations/codex/AGENTS.md` exists with behavioral guidelines.
- [x] `.codex/` structure created per Codex conventions.
- [x] codex-translation checklist applied; intent preserved.
- [x] Parity check run; canonical-tool-mapping.json updated for Codex.
- [x] README with setup and usage instructions.
- [x] implementations/README.md table updated.

## 4. Explicit Non-Goals
- .codex/config.toml system limits (optional).
- Codex skills; optional follow-up.
- Full parity (gaps acceptable; document in mapping).
