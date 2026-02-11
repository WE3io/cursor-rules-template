# Antigravity Implementation

AI Blindspots principles translated for Antigravity. Canonical source: [ai-blindspots/](../../ai-blindspots/) in this repo.

## Setup

1. Copy this folder into your project root, or copy the contents into an existing project.
2. Ensure `GEMINI.md` (or `AGENT.md`) is at project root.
3. Ensure `.agent/rules/` contains the rule files.
4. Configure terminal execution policy (Allow/Deny lists) in Antigravity UI or settings.

## Structure

```
implementations/antigravity/
├── GEMINI.md
├── .agent/
│   └── rules/
│       ├── security.md
│       ├── debugging.md
│       ├── context-management.md
│       ├── testing.md
│       └── terminal-policy.md   # Antigravity-specific: Allow/Deny example
├── .ai-assistant-rules/
│   └── docs/
│       └── articles/    # Bundled AI Blindspots articles (prompt-injection, debugging-blindspot)
└── README.md
```

## Usage

- **GEMINI.md** — Core principles at project root. Antigravity also supports `AGENT.md`.
- **.agent/rules/** — Modular rules (security, debugging, context-management, testing, terminal-policy).
- **Terminal policy:** Antigravity-specific. Configure Allow/Deny lists for command execution. See `.agent/rules/terminal-policy.md` for example.

## Translation

Principles translated from canonical rules. Antigravity adapts security rules to terminal execution policies. See [ai-blindspots/TOOL_TRANSLATION_GUIDE.md](../../ai-blindspots/TOOL_TRANSLATION_GUIDE.md).

## Bundled Docs

`.ai-assistant-rules/docs/articles/` contains bundled AI Blindspots articles for offline/standalone use. Source: `ai-blindspots/` in this repo; sync via `scripts/sync-bundled-docs.py`. For latest: [AI Blindspots](https://ezyang.github.io/ai-blindspots/). Do not edit bundled copies; they are overwritten by sync.

## References

- [AI Blindspots](https://ezyang.github.io/ai-blindspots/)
- [ai-blindspots/](../../ai-blindspots/) — Canonical rules, articles, QUICK_REFERENCE
