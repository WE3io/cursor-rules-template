# Claude Code Implementation

AI Blindspots principles translated for Claude Code. Canonical source: [ai-blindspots/](../../ai-blindspots/) in this repo.

## Setup

1. Copy this folder into your project root, or copy the contents into an existing project.
2. Ensure `CLAUDE.md` is at project root.
3. Ensure `.claude/rules/` contains the rule files.

## Structure

```
implementations/claude/
├── CLAUDE.md              # High-level principles
├── .claude/
│   └── rules/
│       ├── security.md
│       ├── debugging.md
│       ├── context-management.md
│       └── testing.md
├── docs/
│   └── articles/         # Bundled AI Blindspots articles (prompt-injection, debugging-blindspot)
└── README.md
```

## Usage

- **CLAUDE.md** — Loaded as primary project guidelines (hierarchy: Enterprise > Project > User).
- **.claude/rules/** — Auto-loaded supplements. Files map to concerns: security, debugging, context, testing.

## Translation

Principles translated from canonical rules. See [ai-blindspots/TOOL_TRANSLATION_GUIDE.md](../../ai-blindspots/TOOL_TRANSLATION_GUIDE.md) for translation approach.

## Bundled Docs

`docs/articles/` contains bundled AI Blindspots articles for offline/standalone use. Source: `ai-blindspots/` in this repo; sync via `scripts/sync-bundled-docs.py`. For latest: [AI Blindspots](https://ezyang.github.io/ai-blindspots/). Do not edit bundled copies; they are overwritten by sync.

## References

- [AI Blindspots](https://ezyang.github.io/ai-blindspots/)
- [ai-blindspots/](../../ai-blindspots/) — Canonical rules, articles, QUICK_REFERENCE
