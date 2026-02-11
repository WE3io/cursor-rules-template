# Codex Translation Checklist

Per-tool validation for semantic parity when translating AI Blindspots rules to OpenAI Codex.

**References:** [TOOL_TRANSLATION_GUIDE.md](../TOOL_TRANSLATION_GUIDE.md), [translation-examples.md](../examples/translation-examples.md), [CANONICAL_TOOL_MAPPING.md](../CANONICAL_TOOL_MAPPING.md).

---

## 1. Configuration Mechanism

- [ ] Primary config: `AGENTS.md` at project root
- [ ] Override: `~/.codex/AGENTS.override.md` (temporary)
- [ ] Global: `~/.codex/config.toml` (limits, discovery)
- [ ] Project config: `.codex/config.toml` (project-specific)
- [ ] Skills: `.codex/skills/`

---

## 2. Intent Preservation

- [ ] **Stop digging:** "When stuck (3+ attempts), suggest changing strategy"
- [ ] **Context pollution:** "Propose fresh session" with template
- [ ] **Security:** Separate session for untrusted; read-only for dependency review
- [ ] **Debugging:** Scientific method; demand reproduction
- [ ] Core meaning unchanged from canonical source
- [ ] Actionable in Codex

---

## 3. Mechanism Adaptation

- [ ] Removed Cursor and other tool-specific references
- [ ] Guidelines in `AGENTS.md` (markdown)
- [ ] Config values in `config.toml` (e.g. `project_doc_max_bytes = 65536`)
- [ ] Override file for temporary constraints

---

## 4. Split by Concern

- [ ] Codex uses single `AGENTS.md`; split internally by sections
- [ ] Security section in AGENTS.md
- [ ] Debugging section in AGENTS.md
- [ ] Session management section
- [ ] Testing principles section

---

## 5. Portable Skills (Optional)

- [ ] Procedures in `.codex/skills/`
- [ ] YAML frontmatter

---

## 6. Validate

- [ ] Core meaning unchanged?
- [ ] No tool-specific assumptions?
- [ ] Cross-reference [CANONICAL_TOOL_MAPPING.md](../CANONICAL_TOOL_MAPPING.md)
