**Completed:** 2026-02-11 — Created scripts/llm-generator/ with prompt-template.md, runbook.md, README. Generated Claude implementation as proof. BL-017 will formalize.

# BL-016: Create LLM Implementation Generator Scaffold

**Phase:** Later

## 1. Outcome
Reusable prompt template and optional invocation script for generating tool implementations from canonical content via LLM. Enables one-tool-at-a-time generation with human review before commit.

## 2. Constraints & References
- Uses Option D (LLM with custom prompt) from [phase3-template-generation-design.md](../phase3-template-generation-design.md).
- Input: canonical content (ai-blindspots rules, articles, canonical-tool-mapping.json).
- Prompt context must include TOOL_TRANSLATION_GUIDE excerpt and tool-specific checklist (BL-008).
- Human review before commit required; no auto-commit.

**References:** BL-007, BL-008, BL-015, [TOOL_TRANSLATION_GUIDE.md](../../ai-blindspots/TOOL_TRANSLATION_GUIDE.md), [checklists/](../../ai-blindspots/checklists/).

## 3. Acceptance Checks
- [x] Prompt template documented (system prompt + user prompt structure).
- [x] Instructions for assembling context per tool (guide + checklist + canonical content).
- [x] Optional: script or runbook that invokes LLM with template (any language; API-agnostic where possible).
- [x] At least one tool (e.g. Claude) successfully generated using the scaffold.

## 4. Explicit Non-Goals
- Building the full set of tool implementations (BL-017 through BL-020).
- Automated CI integration.
- Schema migration (canonical YAML); existing markdown is acceptable input.
