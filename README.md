# Cursor Rules

A unified reference for AI coding assistant rules, guidelines, and best practices.

---

## Repository Layout

```
cursorrules/
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
    ├── cursor/              # Cursor IDE (Claude, Codex, Gemini planned)
    │   ├── .cursor/rules/   # Ready-to-use Cursor rules
    │   └── docs/
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

## Related

- **Source:** [ezyang.github.io/ai-blindspots](https://ezyang.github.io/ai-blindspots/) — Edward Z. Yang's original AI Blindspots collection
- **Cursor Rules Template:** [WE3io/Cursor-Rules-Template](https://github.com/WE3io/Cursor-Rules-Template)
