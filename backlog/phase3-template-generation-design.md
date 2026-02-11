# Phase 3: Template-Driven Generation — Design Doc

Semi-automated generation of tool formats from canonical schema. Human review before commit required.

**Status:** Design complete. Option D (LLM with custom prompt) preferred. Awaiting maintainer approval.

**Prerequisite:** BL-001 canonical guidance schema (defined; maintainer sign-off pending).

**References:** [canonical-guidance-schema.md](templates/canonical-guidance-schema.md), [TOOL_TRANSLATION_GUIDE.md](../ai-blindspots/TOOL_TRANSLATION_GUIDE.md), [CANONICAL_TOOL_MAPPING.md](../ai-blindspots/CANONICAL_TOOL_MAPPING.md), [checklists/](../ai-blindspots/checklists/).

---

## 1. Architecture Options

### Option A: Template-Based (Jinja2 / Mustache / Handlebars)

**Description:** Canonical schema (YAML/JSON) → template per tool → rendered Markdown/mdc.

**Flow:**
```
canonical/*.yaml → schema validated → tool templates/*.tmpl → render → implementations/{tool}/
```

**Pros:**
- Simple to understand and maintain
- No compilation; templates are readable
- Easy to add new tools (new template)
- Human-readable output

**Cons:**
- Limited logic for complex splits (e.g. security vs. debugging)
- Template syntax can become unwieldy for conditional logic
- May need multiple templates per tool (e.g. Cursor: core-principles.mdc, guardrails.mdc, workflows.mdc)

**Fit:** Best when each tool has a clear 1:1 or 1:few mapping from schema to output files.

---

### Option B: Code-Based Generator (Python/TypeScript)

**Description:** Canonical schema → programmatic transformation → output files.

**Flow:**
```
canonical/*.yaml → schema validated → generator.py (rules) → output files
```

**Pros:**
- Full control over branching, splitting, formatting
- Can implement BL-008 checklists as validation steps
- Easy to add tool-specific heuristics (e.g. "security rules go to guardrails.mdc")
- Testable (unit tests for transformation logic)

**Cons:**
- More code to maintain
- Requires programming to change output structure
- Harder for non-developers to tweak

**Fit:** Best when each tool has non-trivial mapping (multiple files, conditional splits, tool-specific formatting).

---

### Option C: Hybrid (Templates + Thin Orchestrator)

**Description:** Templates for content structure; small script orchestrates which template to use per schema item and tool.

**Flow:**
```
canonical/*.yaml → orchestrator → select template by (tool, principle category) → render → output
```

**Pros:**
- Balance of readability (templates) and flexibility (orchestrator)
- Orchestrator can encode mapping rules (e.g. from CANONICAL_TOOL_MAPPING)
- Templates stay simple

**Cons:**
- Two layers to maintain
- Orchestrator can grow complex

**Fit:** Best when mapping is moderately complex but not arbitrary.

---

### Option D: LLM with Custom Prompt (Preferred)

**Description:** Canonical schema + tool-specific system prompt → LLM generates tool implementation files. Human reviews output before commit.

**Flow:**
```
canonical/*.yaml → schema validated → custom prompt (tool, TOOL_TRANSLATION_GUIDE, checklist) → LLM → implementations/{tool}/
```

**Pros:**
- Uses LLM's natural language and format adaptation (aligns with "translate intent, not mechanism")
- No template or generator code to maintain; prompt is the config
- Easy to refine: adjust prompt, regenerate
- Handles tool-specific nuances (e.g. Cursor .mdc vs Claude CLAUDE.md) via prompt instructions
- Can incorporate BL-008 checklists and TOOL_TRANSLATION_GUIDE directly in prompt context

**Cons:**
- Non-deterministic; may need regeneration for consistency
- Prompt engineering required; prompt versioning matters
- API cost per generation (mitigated by human review cadence)
- Output must be validated (parity check, checklist) every run

**Fit:** Best when semantic translation is primary and tool formats vary significantly. Aligns with existing "translate intent, not mechanism" philosophy.

**Implementation sketch:**
- System prompt: canonical schema + TOOL_TRANSLATION_GUIDE excerpt + tool-specific checklist
- User prompt: "Generate [tool] implementation for principles: [list]. Output file(s) per tool conventions."
- Output: LLM returns markdown; human saves to files, edits if needed, commits

---

## 2. Trade-offs

| Dimension | Template A | Code B | Hybrid C | LLM D |
|-----------|------------|--------|----------|-------|
| **Maintainability** | High (templates only) | Medium (code + schema) | Medium (both) | High (prompt only) |
| **Flexibility** | Low | High | Medium | High |
| **Onboarding** | Low barrier | Medium (programming) | Medium | Low (prompt craft) |
| **Extensibility** | Add template | Add logic | Add template + orchestration rule | Refine prompt |
| **Validation** | Manual / lint | Programmatic | Programmatic | Manual + parity |
| **Human review** | Diff rendered output | Diff generated output | Same | Diff generated output |
| **Determinism** | Yes | Yes | Yes | No (regenerate for consistency) |

**Recommendation:** **Option D (LLM with custom prompt)** — preferred. Aligns with "translate intent, not mechanism"; no code to maintain; prompt captures TOOL_TRANSLATION_GUIDE and checklists. Fallback: Option A if determinism or cost is a concern.

---

## 3. Rollout Plan

### Phase 3.1: Cursor (Pilot)

- **Generator:** LLM with custom prompt (Option D)
- **Input:** Schema-compliant YAML for principles in `canonical-tool-mapping.json` (ok/partial)
- **Prompt context:** TOOL_TRANSLATION_GUIDE, cursor-translation checklist, canonical schema
- **Output:** `implementations/cursor/.cursor/rules/always/*.mdc`
- **Validation:** Parity check (BL-010), Cursor translation checklist (BL-008)
- **Human review:** PR with generated diff; manual adjustment allowed

### Phase 3.2: Claude Code

- **Input:** Same schema
- **Output:** `implementations/claude/CLAUDE.md`, `.claude/rules/*.md`
- **Validation:** Parity check (BL-010), Claude translation checklist
- **Human review:** Same

### Phase 3.3: Codex

- **Input:** Same schema
- **Output:** `implementations/codex/AGENTS.md`, `.codex/` structure
- **Validation:** Parity check, Codex checklist
- **Human review:** Same

### Phase 3.4: Gemini CLI

- **Input:** Same schema
- **Output:** `implementations/gemini/GEMINI.md`, `.agent/rules/`
- **Validation:** Parity check, Gemini checklist
- **Human review:** Same

### Phase 3.5: Antigravity

- **Input:** Same schema
- **Output:** `implementations/antigravity/` (GEMINI.md / AGENT.md)
- **Validation:** Parity check, Antigravity checklist
- **Human review:** Same

### Cadence

- One tool per phase; validate before proceeding
- Between phases: refine schema/templates if needed
- No full automation; human review before every commit

---

## 4. Human Review Gate

**Semi-automated** means:

1. Generator produces output (files or patches)
2. Human reviews diff
3. Human may edit output before commit
4. Human commits

**Not in scope:**

- Auto-commit on CI
- Fully automated releases
- No human in the loop

---

## 5. Dependencies

- Schema (BL-001): Defined; adoption pending
- Mapping matrix (BL-007): Exists
- Checklists (BL-008): Exists per tool
- Parity check (BL-010): Exists

---

## 6. Approval

- [ ] Design doc reviewed
- [x] Architecture option selected: **Option D (LLM with custom prompt)** — preferred
- [ ] Rollout plan approved
- [ ] Maintainer sign-off

**Awaiting maintainer approval.**
