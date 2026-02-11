# Cursor Rules Documentation

This directory contains rules and guidelines for AI coding assistants in this project.

## Organization

### Always Rules (`always/`)
Rules that are automatically included in every AI interaction:
- `core-principles.mdc` - Core principles and task complexity assessment
- `workflows.mdc` - Task-specific workflows and patterns
- `guardrails.mdc` - Constraints, quality checks, and security requirements

### Agent Requested Rules (`agent-requested/`)
Detailed reference material that AI can fetch when needed:
- `review-checklist.mdc` - Comprehensive self-review checklist

## Rule Types

- **Always**: Automatically included in every context
- **Auto Attached**: Automatically attached based on file paths (none currently)
- **Agent Requested**: Fetched by AI when relevant
- **Manual**: Referenced explicitly with `@rule-name` (none currently)

## Adding New Rules

1. Determine the appropriate rule type and directory
2. Follow the structure and examples in existing rules
3. Include code examples (good and bad patterns)
4. Add scope declarations if not universal
5. Update this README with the new rule

## Related Documentation

Required (expected in this template):
- `../../docs/aca_usage_guide.md` - Full AI Coding Assistant Usage Guide
- `../../docs/cursor_rules_best_practices.md` - Best practices for creating rules

Optional canonical references (available in the monorepo, may be absent in standalone installs):
- `../../../../ai-blindspots/QUICK_REFERENCE.md` - AI Blindspots one-page cheat sheet (when to restart, security red flags, debugging flow)
- `../../../../ai-blindspots/rules/ai-coding-assistant-rules.md` - Comprehensive AI Blindspots ruleset (core principles, implementation guidelines, and decision aids)

If you install only `.cursor/rules/`, replace optional links with project-local docs or absolute URLs.

## Maintenance

Rules should be reviewed monthly and updated when:
- Architecture or patterns change
- New best practices emerge
- Team feedback indicates improvements needed
- Rules become too verbose or complex
