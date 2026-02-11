# Tool Implementations

Tool-specific rule configurations derived from [AI Blindspots](../ai-blindspots/).

Each implementation translates the canonical rules into the format required by that tool. See [ai-blindspots/TOOL_TRANSLATION_GUIDE.md](../ai-blindspots/TOOL_TRANSLATION_GUIDE.md) for translation principles.

---

## Available Implementations

| Tool | Path | Status |
|------|------|--------|
| **Cursor** | [cursor/](cursor/) | Ready |
| **Claude Code** | [claude/](claude/) | Ready |
| **Codex** | `codex/` | Planned |
| **Gemini CLI** | `gemini/` | Planned |
| **Antigravity** | `antigravity/` | Planned |

---

## Adding a New Implementation

1. Create a new folder: `implementations/<tool-name>/`
2. Follow the translation guide: [TOOL_TRANSLATION_GUIDE.md](../ai-blindspots/TOOL_TRANSLATION_GUIDE.md)
3. Include:
   - Tool-specific config files (e.g., `.cursor/rules/`, `CLAUDE.md`, `AGENTS.md`)
   - README with setup instructions
   - References back to `ai-blindspots/` for the canonical rules
4. Update this README's table

---

## Relationship to AI Blindspots

```
ai-blindspots/          ← Canonical source (rules, articles, quick reference)
       │
       └── implementations/   ← Tool-specific translations
               ├── cursor/
               ├── claude/
               └── ...
```

**Principle:** Translate intent, not mechanism. The rules express universal truths about AI behavior; each tool folder adapts how those truths are communicated.
