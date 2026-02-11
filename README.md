# AI Assistant Rules

<table style="background-color: #F4EAD0;color: #29004B;">
  <tr>
    <td width="132" style="border:none; background-color: #F4EAD0;" valign="middle">
      <a href="https://we3.io"><img src="assets/WE3io-logo-200px.png" alt="WE3io Logo" width="56" /></a>
    </td>
    <td style="border:none; background-color: #F4EAD0;">
      <strong>WE3</strong> builds products and companies with senior Product, Design, and Engineering teams. This repository is part of our open-source community offerings. <a href="https://we3.io/brief">Start your brief</a>.
    </td>
  </tr>
</table>

---

A unified reference for AI coding assistant rules, guidelines, and best practices across multiple tools.

## Quick navigation

[What this is](#what-this-is) · [Who this is for](#who-this-is-for) · [Supported Tools](#supported-tools) · [Repository Layout](#repository-layout) · [Where to Start](#where-to-start) · [Quality](#quality) · [Related](#related)

---

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

Install using the setup script (interactive or flag-based):

```bash
python scripts/setup-rules.py                    # interactive
python scripts/setup-rules.py --tool cursor --project .
```

Or use the direct install script:

```bash
python scripts/install-implementation.py cursor .                    # install Cursor rules to current dir
python scripts/install-implementation.py claude /path/to/project    # install Claude rules to target
python scripts/install-implementation.py                            # list available tools (no args)
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
├── assets/                  # Images (logos, diagrams)
├── backlog/
│   ├── active/              # Work items (phases: Now, Next, Later)
│   └── done/                # Completed work items
│
├── docs/                    # User-facing documentation
├── implementations/         # Tool-specific rule configurations
│   ├── cursor/              # Cursor IDE rules
│   ├── claude/              # Claude Code rules
│   ├── codex/               # Codex rules
│   ├── gemini/              # Gemini CLI rules
│   └── antigravity/         # Antigravity rules
│
└── scripts/                 # Install and maintenance scripts
    ├── install-implementation.py
    └── setup-rules.py
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
- **Lightweight AI Development Agent Skills:** [WE3io/lightweight-ai-development-agent-skills](https://github.com/WE3io/lightweight-ai-development-agent-skills) — A small set of reusable AI agent skills (Work Item Designer, Implementation Executor, Decision Lens, Documentation Lens, Safety Lens) for disciplined, low-ceremony development. Use it alongside these rules for comprehensive guidance across tools.
