# Canonical Guidance Schema

Standard structure for each rule or guidance item in the AI Blindspots collection. Supports downstream tool translation and quality gates.

## Schema Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes | Unique identifier (e.g. `context-pollution`, `security-sql-injection`) |
| `title` | string | Yes | Human-readable title |
| `intent` | string | Yes | What the guidance aims to achieve; the "why" |
| `rationale` | string | Yes | Why this guidance works; evidence or reasoning |
| `examples` | string or list | Optional | Concrete examples (good/bad patterns, scenarios) |
| `risk` | string | Optional | What goes wrong if ignored |
| `confidence` | enum | Optional | `high`, `medium`, `low` — confidence in the guidance |
| `sources` | list | Optional | URLs, papers, or references (e.g. blog posts, docs) |
| `owner` | string | Optional | Responsible for review |
| `review_date` | date | Optional | Next scheduled review (YYYY-MM-DD) |

## Worked Example

```yaml
id: context-pollution
title: Restart sessions at ~20-30 messages
intent: Prevent accumulated errors and misconceptions from degrading AI responses in long conversations.
rationale: LLMs have no meta-awareness of earlier mistakes; each response builds on previous context. Early errors compound over time.
examples:
  - "After 25 messages, AI keeps proposing the same failing fix"
  - "症状: Same errors repeating → Action: Restart session (QUICK_REFERENCE)"
risk: Continued conversation produces increasingly unreliable or contradictory output.
confidence: high
sources:
  - https://ezyang.github.io/ai-blindspots/
  - ai-blindspots/articles/context-management/context-pollution.md
owner: maintainer
review_date: 2026-08-01
```

## Usage

- **Rules:** Apply to `ai-blindspots/rules/` and `ai-blindspots/articles/`
- **Tool translation:** Schema supports mapping to Cursor, Claude, Codex, Gemini, Antigravity
- **Quality gates:** Use with change acceptance criteria (BL-002) and manifest format (BL-006)

## Related

- [Change acceptance criteria](../done/bl-002-add-change-acceptance-criteria.md)
- [Change manifest format](../done/bl-006-build-change-manifest-format.md)
