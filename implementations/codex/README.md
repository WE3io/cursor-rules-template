# Codex Implementation

AI Blindspots principles translated for OpenAI Codex. Canonical source: [ai-blindspots/](../../ai-blindspots/) in this repo.

## Setup

1. Copy `AGENTS.md` to your project root.
2. Optionally add `.codex/config.toml` for project-specific settings (e.g. `project_doc_max_bytes = 65536`).

## Structure

```
implementations/codex/
├── AGENTS.md              # Behavioral guidelines (single file, internal sections)
├── .codex/                # Optional (e.g. config.toml)
└── README.md
```

## Usage

- **AGENTS.md** — Codex discovers this at project root. Contains all sections: Problem-Solving, Context Management, Security, Debugging, Testing.
- **Override:** Use `~/.codex/AGENTS.override.md` for temporary constraints.
- **Config:** `~/.codex/config.toml` or `.codex/config.toml` for limits and discovery.

## Translation

Codex uses a single AGENTS.md with internal sections (no separate rule files). Principles translated from canonical rules. See [ai-blindspots/TOOL_TRANSLATION_GUIDE.md](../../ai-blindspots/TOOL_TRANSLATION_GUIDE.md).

## References

- [AI Blindspots](https://ezyang.github.io/ai-blindspots/)
- [ai-blindspots/](../../ai-blindspots/) — Canonical rules, articles, QUICK_REFERENCE
