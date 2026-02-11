# Antigravity Translation Checklist

Per-tool validation for semantic parity when translating AI Blindspots rules to Antigravity.

**References:** [TOOL_TRANSLATION_GUIDE.md](../TOOL_TRANSLATION_GUIDE.md), [translation-examples.md](../examples/translation-examples.md), [CANONICAL_TOOL_MAPPING.md](../CANONICAL_TOOL_MAPPING.md).

---

## 1. Configuration Mechanism

- [ ] File-based: `GEMINI.md` or `AGENT.md` at project root
- [ ] Modular rules: `.agent/rules/*.md`
- [ ] User Rules (UI): Customizable, project-specific
- [ ] System Rules (UI): Immutable, core identity
- [ ] Terminal policies: Allow/Deny lists, Auto-execution vs Ask vs Restricted
- [ ] Skills: `.agent/skills/`

---

## 2. Intent Preservation

- [ ] **Stop digging:** "Escalate to user after 3 failed attempts"
- [ ] **Context pollution:** User Rule + "Suggest fresh session with summary template"
- [ ] **Security:** User Rule + Terminal policy (Allow/Deny lists)
- [ ] **Debugging:** Scientific method in `.agent/rules/debugging.md` or User Rule
- [ ] Core meaning unchanged from canonical source
- [ ] Actionable in Antigravity

---

## 3. Mechanism Adaptation

- [ ] Removed Cursor and other tool-specific references
- [ ] System Rules → foundational (immutable)
- [ ] User Rules → project-specific adaptations
- [ ] File rules → version-controlled guidance
- [ ] Terminal policies → execution boundaries (Antigravity-specific)

---

## 4. Split by Concern

- [ ] `GEMINI.md` or `AGENT.md` — core principles
- [ ] `.agent/rules/security.md` — security boundaries
- [ ] `.agent/rules/debugging.md` — scientific debugging
- [ ] User Rule for context refresh
- [ ] Terminal policy for command control (Allow/Deny)

---

## 5. Antigravity-Specific: Terminal Policy

- [ ] Security rules adapt to terminal execution policies
- [ ] Allow list for safe commands (e.g. `npm test`, `git status`)
- [ ] Deny list for dangerous commands (e.g. `rm -rf`, `sudo *`)

---

## 6. Validate

- [ ] Core meaning unchanged?
- [ ] No tool-specific assumptions from other tools?
- [ ] Terminal policy aligns with security intent?
- [ ] Cross-reference [CANONICAL_TOOL_MAPPING.md](../CANONICAL_TOOL_MAPPING.md)
