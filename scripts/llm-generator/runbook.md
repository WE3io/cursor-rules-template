# LLM Implementation Generator — Runbook

Copy-paste steps to generate a tool implementation using the prompt template. API-agnostic; use any LLM (Claude, GPT, Gemini, etc.).

---

## Prerequisites

- Repo checked out at `ai-assistant-rules/`
- Access to an LLM with sufficient context window (~50K+ tokens for full context)

---

## Steps

### 1. Choose target tool

One of: `claude`, `codex`, `gemini`, `antigravity`

### 2. Assemble context

From repo root:

```bash
# Verify paths
ls ai-blindspots/rules/ai-coding-assistant-rules.md
ls ai-blindspots/QUICK_REFERENCE.md
ls ai-blindspots/TOOL_TRANSLATION_GUIDE.md
ls ai-blindspots/checklists/{TOOL}-translation.md   # e.g. claude-translation.md
ls ai-blindspots/canonical-tool-mapping.json
```

Open these files and copy into your prompt context:

| File | Purpose |
|------|---------|
| `ai-blindspots/TOOL_TRANSLATION_GUIDE.md` | Translation principles + target tool section |
| `ai-blindspots/checklists/{TOOL}-translation.md` | Validation checklist |
| `ai-blindspots/rules/ai-coding-assistant-rules.md` | Canonical principles |
| `ai-blindspots/QUICK_REFERENCE.md` | Quick reference |
| `ai-blindspots/canonical-tool-mapping.json` | Principle IDs |

### 3. Build the prompts

**System prompt:** Use [prompt-template.md](prompt-template.md) — System Prompt section.

**User prompt:** Use [prompt-template.md](prompt-template.md) — User Prompt section. Replace:

- `[TOOL]` → target tool name
- `[Paste the relevant...]` → TOOL_TRANSLATION_GUIDE excerpt for that tool
- `[Paste the tool-specific checklist...]` → full checklist content
- `[Paste or summarize...]` → canonical rules + QUICK_REFERENCE
- `[List principles...]` → principles from canonical-tool-mapping.json

### 4. Invoke LLM

1. Paste system prompt into LLM system/context field.
2. Paste user prompt (with assembled context) as user message.
3. Send. LLM should return files with `---FILE: path---` delimiters.

### 5. Extract and save output

1. Parse LLM response for `---FILE: path---` blocks.
2. Create `implementations/{TOOL}/` directory.
3. Write each file to its path under that directory.
4. Ensure structure matches tool conventions (e.g. `.claude/rules/` for Claude).

### 6. Validate

```bash
# Parity check
python3 scripts/parity-check.py

# Apply per-tool checklist manually
# See ai-blindspots/checklists/{TOOL}-translation.md
```

### 7. Human review and commit

- Review all generated files.
- Edit as needed for intent preservation.
- Update `ai-blindspots/canonical-tool-mapping.json` with principle status.
- Update `implementations/README.md` table.
- Commit after review.

---

## Example: Claude

```
Target: claude
Checklist: ai-blindspots/checklists/claude-translation.md
Output: implementations/claude/CLAUDE.md, implementations/claude/.claude/rules/*.md, implementations/claude/README.md
```

---

## Troubleshooting

- **Output missing files:** Re-prompt with explicit file list from checklist.
- **Tool-specific references in output:** Add to system prompt: "Remove Cursor and other tool names."
- **Context too large:** Use summarized canonical rules or fewer articles; prioritize TOOL_TRANSLATION_GUIDE and checklist.
- **Inconsistent structure:** Verify checklist section 4 (Split by Concern) and re-generate.
