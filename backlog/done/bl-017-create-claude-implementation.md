**Completed:** 2026-02-11 — implementations/claude/ with CLAUDE.md, .claude/rules/, README. canonical-tool-mapping.json and implementations/README.md updated. Parity check run.

# BL-017: Create Claude Code Implementation

**Phase:** Later

## 1. Outcome
Claude Code implementation added under `implementations/claude/`. CLAUDE.md and .claude/rules/*.md translate canonical AI Blindspots principles. README with setup instructions. Parity check updated for Claude.

## 2. Constraints & References
- Uses [claude-translation.md](../../ai-blindspots/checklists/claude-translation.md) for validation.
- Output: CLAUDE.md (high-level principles), .claude/rules/ (security.md, debugging.md, context-management.md, testing.md, etc.).
- Translate intent, not mechanism; no Cursor or other tool-specific references.
- Human review before commit.

**References:** BL-007, BL-008, BL-010, BL-016, [TOOL_TRANSLATION_GUIDE.md](../../ai-blindspots/TOOL_TRANSLATION_GUIDE.md).

## 3. Acceptance Checks
- [x] `implementations/claude/CLAUDE.md` exists with core principles.
- [x] `.claude/rules/` contains topic-specific files (e.g. security.md, debugging.md).
- [x] claude-translation checklist applied; intent preserved.
- [x] Parity check run; canonical-tool-mapping.json updated for Claude (principle status).
- [x] README with setup and usage instructions.
- [x] implementations/README.md table updated.

## 4. Explicit Non-Goals
- Claude skills (.claude/skills/); optional follow-up.
- Enterprise-level CLAUDE.md hierarchy.
- Full parity (gaps acceptable; document in mapping).
