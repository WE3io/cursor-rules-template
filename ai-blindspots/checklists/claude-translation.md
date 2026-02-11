# Claude Code Translation Checklist

Per-tool validation for semantic parity when translating AI Blindspots rules to Claude Code.

**References:** [TOOL_TRANSLATION_GUIDE.md](../TOOL_TRANSLATION_GUIDE.md), [translation-examples.md](../examples/translation-examples.md), [CANONICAL_TOOL_MAPPING.md](../CANONICAL_TOOL_MAPPING.md).

---

## 1. Configuration Mechanism

- [ ] Primary config: `CLAUDE.md` at project root (hierarchy: Enterprise > Project > User)
- [ ] Supplemental: `.claude/rules/*.md` (auto-loaded)
- [ ] Skills: `.claude/skills/*/SKILL.md`
- [ ] Hierarchy understood: Project CLAUDE.md overrides User; Enterprise overrides all

---

## 2. Intent Preservation

- [ ] **Stop digging:** "After 3 failures, propose alternative approach" (not Cursor-specific)
- [ ] **Context pollution:** "Suggest starting new conversation" (mechanism-neutral)
- [ ] **Security:** External content untrusted; separate contexts for privileged/unprivileged
- [ ] **Debugging:** Scientific method expressed
- [ ] Core meaning unchanged from canonical source
- [ ] Actionable in Claude Code

---

## 3. Mechanism Adaptation

- [ ] Removed Cursor and other tool-specific references
- [ ] Core principles in `CLAUDE.md` (concise)
- [ ] Detailed guidance in `.claude/rules/` (e.g. `security.md`, `debugging.md`)
- [ ] File paths use `.claude/rules/`, not `.cursor/rules`

---

## 4. Split by Concern

- [ ] `CLAUDE.md` — high-level principles only
- [ ] `.claude/rules/security.md` — security boundaries
- [ ] `.claude/rules/debugging.md` — scientific debugging
- [ ] `.claude/rules/context-management.md` — session restarts
- [ ] `.claude/rules/testing.md` — black box principles
- [ ] `.claude/rules/domain-*.md` — domain-specific (optional)

---

## 5. Portable Skills (Optional)

- [ ] Procedures in `.claude/skills/*/SKILL.md`
- [ ] YAML frontmatter with name, description

---

## 6. Validate

- [ ] Core meaning unchanged?
- [ ] No tool-specific assumptions?
- [ ] Cross-reference [CANONICAL_TOOL_MAPPING.md](../CANONICAL_TOOL_MAPPING.md)
