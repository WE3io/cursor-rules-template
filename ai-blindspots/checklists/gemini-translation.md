# Gemini CLI Translation Checklist

Per-tool validation for semantic parity when translating AI Blindspots rules to Gemini CLI.

**References:** [TOOL_TRANSLATION_GUIDE.md](../TOOL_TRANSLATION_GUIDE.md), [translation-examples.md](../examples/translation-examples.md), [CANONICAL_TOOL_MAPPING.md](../CANONICAL_TOOL_MAPPING.md).

---

## 1. Configuration Mechanism

- [ ] Primary config: `GEMINI.md` at project root
- [ ] Modular rules: `.agent/rules/*.md`
- [ ] Settings: `~/.gemini/settings.json` (MCP, tool config)
- [ ] Hierarchy: Project > Workspace > User
- [ ] Skills: `.agent/skills/`

---

## 2. Intent Preservation

- [ ] **Stop digging:** "Pivot approach after 3 unsuccessful iterations"
- [ ] **Context pollution:** "Suggest restart with summary"
- [ ] **Security:** Isolate untrusted content; separate contexts
- [ ] **Debugging:** Scientific method expressed
- [ ] Core meaning unchanged from canonical source
- [ ] Actionable in Gemini CLI

---

## 3. Mechanism Adaptation

- [ ] Removed Cursor and other tool-specific references
- [ ] Core principles in `GEMINI.md`
- [ ] Detailed rules in `.agent/rules/` (e.g. `security.md`, `debugging.md`)
- [ ] File paths use `.agent/rules/`, not `.cursor/rules`

---

## 4. Split by Concern

- [ ] `GEMINI.md` — core principles
- [ ] `.agent/rules/security.md` — security boundaries
- [ ] `.agent/rules/debugging.md` — scientific debugging
- [ ] `.agent/rules/context-management.md` — session restarts
- [ ] `.agent/rules/testing.md` — black box principles
- [ ] `.agent/rules/domain-*.md` — domain-specific (optional)

---

## 5. Portable Skills (Optional)

- [ ] Procedures in `.agent/skills/`
- [ ] YAML frontmatter

---

## 6. Validate

- [ ] Core meaning unchanged?
- [ ] No tool-specific assumptions?
- [ ] Cross-reference [CANONICAL_TOOL_MAPPING.md](../CANONICAL_TOOL_MAPPING.md)
