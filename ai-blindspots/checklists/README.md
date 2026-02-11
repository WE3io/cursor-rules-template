# Tool Translation Checklists

Per-tool validation checklists for semantic parity when translating AI Blindspots rules.

**Principle:** Translate intent, not mechanism.

## Checklists

| Tool | File | Use When |
|------|------|----------|
| Cursor | [cursor-translation.md](cursor-translation.md) | Translating to `.cursor/rules` |
| Claude Code | [claude-translation.md](claude-translation.md) | Translating to `CLAUDE.md`, `.claude/rules/` |
| Codex | [codex-translation.md](codex-translation.md) | Translating to `AGENTS.md` |
| Gemini CLI | [gemini-translation.md](gemini-translation.md) | Translating to `GEMINI.md`, `.agent/rules/` |
| Antigravity | [antigravity-translation.md](antigravity-translation.md) | Translating to Antigravity config |

## Usage

1. Run the checklist for the target tool when implementing or reviewing a translation.
2. Verify intent preservation and mechanism adaptation.
3. Cross-reference [CANONICAL_TOOL_MAPPING.md](../CANONICAL_TOOL_MAPPING.md) for coverage.

## Related

- [TOOL_TRANSLATION_GUIDE.md](../TOOL_TRANSLATION_GUIDE.md) — Translation principles
- [translation-examples.md](../examples/translation-examples.md) — Side-by-side examples
