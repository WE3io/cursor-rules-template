# LLM Implementation Generator — Prompt Template

**Purpose:** Generate tool-specific implementations from canonical AI Blindspots content. One tool per invocation. Human review before commit.

---

## System Prompt

You are a translator of AI coding assistant rules. Your task is to convert canonical AI Blindspots principles into the format required by a specific tool (Claude Code, Codex, Gemini CLI, or Antigravity).

**Core principle:** Translate intent, not mechanism. The rules express universal truths about AI behavior. How you communicate them varies by tool, but what they mean remains constant.

**Rules:**
- Remove all tool-specific references (Cursor, etc.). Use mechanism-neutral language.
- Adapt file paths and structure to the target tool's conventions.
- Preserve semantic meaning; do not add or remove principles.
- Output valid markdown files per the target tool's expected structure.
- Do not include skills (`.claude/skills/`, etc.) unless explicitly requested; focus on rules and config.

**Output format:** Return each file as a separate block with a clear delimiter, e.g.:

```
---FILE: path/to/file.md---
[content]
---END---
```

---

## User Prompt

Generate the [TOOL] implementation for the AI Blindspots principles.

**Target tool:** [claude | codex | gemini | antigravity]

**Target structure (from TOOL_TRANSLATION_GUIDE):**
[Paste the relevant Tool Configuration Equivalents and Translation Strategy section for the target tool]

**Validation checklist (apply before finalizing):**
[Paste the tool-specific checklist from ai-blindspots/checklists/{tool}-translation.md]

**Canonical content:**
[Paste or summarize: ai-blindspots/rules/ai-coding-assistant-rules.md, QUICK_REFERENCE.md, relevant articles]

**Principles to cover (from canonical-tool-mapping.json):**
[List principles with status ok/partial from Cursor as reference for expectations]

**Instructions:**
1. Produce all required files for the target tool.
2. Ensure intent preservation: stop-digging, context-pollution, security, debugging, testing, etc.
3. Split by concern per the checklist (e.g. CLAUDE.md + .claude/rules/security.md, debugging.md, etc.).
4. Include a README with setup and usage instructions.
5. Output each file with the ---FILE: path--- delimiter.

---

## Context Assembly Instructions

Assemble context per tool before invoking the LLM:

### 1. TOOL_TRANSLATION_GUIDE excerpt

Include from `ai-blindspots/TOOL_TRANSLATION_GUIDE.md`:

- **Core Principle** (lines 1–16): "Translate intent, not mechanism"
- **Tool Configuration Equivalents** table (lines 18–28)
- **Translation Strategy** section for the target tool (Claude Code, Codex, Gemini, or Antigravity)
- **Semantic Translation Principles** (lines 257–310): Intent Preservation, Context Adaptation, Mechanism Neutrality
- **What to Keep vs. What to Adapt** (lines 313–358)
- **Modular Translation: Split by Concern** (lines 427–464) — file structure for target tool

### 2. Tool-specific checklist

Include the full contents of:

- `ai-blindspots/checklists/claude-translation.md` (for Claude)
- `ai-blindspots/checklists/codex-translation.md` (for Codex)
- `ai-blindspots/checklists/gemini-translation.md` (for Gemini)
- `ai-blindspots/checklists/antigravity-translation.md` (for Antigravity)

### 3. Canonical content

Include or summarize:

- `ai-blindspots/rules/ai-coding-assistant-rules.md` — full rules (or sections 1–5 for principles)
- `ai-blindspots/QUICK_REFERENCE.md` — quick reference card
- `ai-blindspots/articles/` — relevant articles (context-pollution, debugging-blindspot, prompt-injection, etc.)
- `ai-blindspots/canonical-tool-mapping.json` — principle IDs and Cursor status for reference

### 4. Reference implementation (optional)

For structure reference, include excerpts from:

- `implementations/cursor/.cursor/rules/always/` — core-principles.mdc, guardrails.mdc, workflows.mdc

Use only for structure and intent; do not copy Cursor-specific mechanisms.
