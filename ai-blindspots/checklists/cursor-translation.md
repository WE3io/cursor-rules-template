# Cursor Translation Checklist

Per-tool validation for semantic parity when translating AI Blindspots rules to Cursor.

**References:** [TOOL_TRANSLATION_GUIDE.md](../TOOL_TRANSLATION_GUIDE.md), [translation-examples.md](../examples/translation-examples.md), [CANONICAL_TOOL_MAPPING.md](../CANONICAL_TOOL_MAPPING.md).

---

## 1. Configuration Mechanism

- [ ] Primary config: `.cursor/rules/` (or project `.cursor/rules/`)
- [ ] Rule types: `always/`, `agent-requested/`, `auto-attached/`, `manual/`
- [ ] File format: `.mdc` (Markdown with optional frontmatter)

---

## 2. Intent Preservation

- [ ] **Stop digging:** Pivot after 3 failures expressed (not "Click restart in Cursor")
- [ ] **Context pollution:** Restart at 20-30 messages expressed (mechanism-neutral)
- [ ] **Security:** External content untrusted, validation required
- [ ] **Debugging:** Scientific method (observe → hypothesize → test → fix)
- [ ] **Root cause:** Demand reproduction, minimal fixes
- [ ] Core meaning unchanged from canonical source
- [ ] Actionable in Cursor; no assumptions about other tools

---

## 3. Mechanism Adaptation

- [ ] Removed references to other tools (Claude, Codex, Gemini, Antigravity)
- [ ] Cursor-specific paths use `.cursor/rules` or equivalent
- [ ] No UI-specific instructions (e.g. "Click New Chat") — use mechanism-neutral language
- [ ] Rules placed in correct directory: `always/` for universal, `agent-requested/` for on-demand

---

## 4. Split by Concern (Optional)

- [ ] Security rules in dedicated file or section
- [ ] Debugging method in dedicated file or section
- [ ] Context management guidance included
- [ ] Testing principles included

---

## 5. Validate

- [ ] Run Cursor with rules loaded; verify behaviour matches intent
- [ ] Cross-reference [CANONICAL_TOOL_MAPPING.md](../CANONICAL_TOOL_MAPPING.md) for coverage
