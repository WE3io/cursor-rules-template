# AI Assistant Rules

A unified reference for AI coding assistant rules, guidelines, and best practices across multiple tools.

## What this is

Canonical rules and best practices for AI coding assistants (Cursor, Claude Code, Codex, Gemini CLI, Antigravity), derived from [AI Blindspots](https://ezyang.github.io/ai-blindspots/). Each tool gets the same principles translated into its configuration format.

## Who this is for

- Developers using AI coding assistants in their workflow
- Teams adopting shared rules for AI-assisted development
- Maintainers of projects that rely on AI pair programming

---

## Supported Tools

- [Cursor](implementations/cursor/) — Cursor IDE
- [Claude Code](implementations/claude/) — Claude Code
- [Codex](implementations/codex/) — Codex
- [Gemini CLI](implementations/gemini/) — Gemini CLI
- [Antigravity](implementations/antigravity/) — Antigravity

Install using the recommended script:

```bash
python scripts/install-implementation.py <tool> [target_dir]
```

See [implementations/README.md#installation](implementations/README.md#installation) for options and examples.

---

## Repository Layout

```
ai-assistant-rules/
├── ai-blindspots/           # Canonical rules & articles (Edward Z. Yang)
│   ├── articles/            # In-depth articles by topic
│   ├── rules/               # Comprehensive AI coding assistant rules
│   ├── QUICK_REFERENCE.md
│   └── TOOL_TRANSLATION_GUIDE.md
│
├── backlog/
│   ├── active/              # Work items (phases: Now, Next, Later)
│   └── done/                # Completed work items
│
└── implementations/        # Tool-specific rule configurations
    ├── cursor/              # Cursor IDE rules
    ├── claude/              # Claude Code rules
    ├── codex/               # Codex rules
    ├── gemini/              # Gemini CLI rules
    └── antigravity/         # Antigravity rules
```

**Relationship:** All implementations derive from `ai-blindspots`. Each tool folder contains the same principles translated into that tool's configuration format. See [implementations/README.md](implementations/README.md) for details.

---

## Where to Start

| Goal | Start Here |
|------|-------------|
| **Quick cheat sheet** | [ai-blindspots/QUICK_REFERENCE.md](ai-blindspots/QUICK_REFERENCE.md) (5 min) |
| **Full ruleset** | [ai-blindspots/rules/ai-coding-assistant-rules.md](ai-blindspots/rules/ai-coding-assistant-rules.md) (30 min) |
| **Set up a new Cursor project** | [implementations/cursor/README.md](implementations/cursor/README.md) |
| **Install an implementation** | [implementations/README.md#installation](implementations/README.md#installation) |
| **Browse tool implementations** | [implementations/README.md](implementations/README.md) |
| **Adapt rules for other tools** | [ai-blindspots/TOOL_TRANSLATION_GUIDE.md](ai-blindspots/TOOL_TRANSLATION_GUIDE.md) (Claude, Codex, Gemini, Antigravity) |
| **Deep dive on a topic** | [ai-blindspots/articles/](ai-blindspots/articles/) |

---

## Quality

CI workflows run on pull requests:

- [Docs QA](.github/workflows/docs-qa.yml) — Markdown lint, link checks, required sections
- [Parity check](.github/workflows/parity-check.yml) — Canonical-to-tool coverage
- [Staleness check](.github/workflows/staleness-check.yml) — Sunset tracking

---

## Related

- **Source:** [ezyang.github.io/ai-blindspots](https://ezyang.github.io/ai-blindspots/) — Edward Z. Yang's original AI Blindspots collection
- **Cursor Rules Template:** [WE3io/Cursor-Rules-Template](https://github.com/WE3io/Cursor-Rules-Template)
