# Tool Implementations

Tool-specific rule configurations derived from [AI Blindspots](../ai-blindspots/).

Each implementation translates the canonical rules into the format required by that tool. This monorepo provides implementations for Cursor, Claude Code, Codex, Gemini CLI, and Antigravity. See [ai-blindspots/TOOL_TRANSLATION_GUIDE.md](../ai-blindspots/TOOL_TRANSLATION_GUIDE.md) for translation principles.

---

## Available Implementations

| Tool | Path | Status |
|------|------|--------|
| **Cursor** | [cursor/](cursor/) | Ready |
| **Claude Code** | [claude/](claude/) | Ready |
| **Codex** | [codex/](codex/) | Ready |
| **Gemini CLI** | [gemini/](gemini/) | Ready |
| **Antigravity** | [antigravity/](antigravity/) | Ready |

---

## Installation

### One-command setup (recommended for beginners)

Interactive setup with prompts, or pass flags for automation:

```bash
# Interactive (run from repo root)
python scripts/setup-rules.py

# Flag-based
python scripts/setup-rules.py --tool cursor --project .

# Verify install
python scripts/setup-rules.py --doctor --tool cursor --project .
```

Options: `--tool`, `--project`, `--scope` (project/user; user-level for Codex only), `--force`, `--dry-run`, `--doctor`.

### Install script (direct)

From the ai-assistant-rules repo root, or by path to the script:

```bash
python scripts/install-implementation.py <tool> [target_dir]
```

Examples: `claude .` (current dir), `cursor /path/to/project`, or no args to list tools. Use `-t` or `--target` when passing flags: `claude -t /path --dry-run`.
Options: `--force` / `-f` (overwrite existing), `--dry-run` / `-n` (preview only).

### Degit alternative

If you have Node.js and prefer not to clone the repo:

```bash
npx degit <org>/ai-assistant-rules/implementations/<tool> .
```

Replace `<org>` with the repository owner (e.g. `WE3io`). Requires network access.

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
               ├── codex/
               ├── gemini/
               ├── antigravity/
               └── ...
```

**Principle:** Translate intent, not mechanism. The rules express universal truths about AI behavior; each tool folder adapts how those truths are communicated.
