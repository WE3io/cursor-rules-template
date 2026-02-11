# AI Blindspots

Practical insights into AI coding assistant limitations and effective mitigation strategies.

**Source:** Based on [ezyang.github.io/ai-blindspots](https://ezyang.github.io/ai-blindspots/)

---

## Quick Start

**New?** → **[Quick Reference](QUICK_REFERENCE.md)** (5 min)

**Need rules?** → **[AI Coding Assistant Rules](rules/ai-coding-assistant-rules.md)** (30 min)

**Specific topic?** → **[Articles by category](articles/)**

---

## What's Inside

### 📋 [Quick Reference](QUICK_REFERENCE.md)
One-page cheat sheet:
- When things go wrong
- Security red flags
- Debugging decision tree
- Confidence calibration
- Prompting patterns

### 📚 [Rules](rules/)
Comprehensive guidelines:
- [AI Coding Assistant Rules](rules/ai-coding-assistant-rules.md) - Complete ruleset
- [Usage Guide](rules/README.md) - Integration & customization

### 📖 [Articles](articles/)
In-depth coverage by category:

**Fundamentals**
- [Memento](articles/fundamentals/memento.md) - Memory & context limitations
- [Static Types](articles/fundamentals/static-types.md) - Leveraging types

**Security**
- [Prompt Injection](articles/security/prompt-injection.md) - Security vulnerabilities

**Debugging**
- [Debugging Blindspot](articles/debugging/debugging-blindspot.md) - Root cause analysis

**Context Management**
- [Context Pollution](articles/context-management/context-pollution.md) - When to restart
- [Overconfidence](articles/context-management/overconfidence.md) - Calibrating trust

### 📝 [Examples](examples/)
Side-by-side translation examples: [translation-examples.md](examples/translation-examples.md) — same rules in Cursor, Claude, Codex, Gemini, Antigravity formats.

---

## Key Insights

| Issue | Solution |
|-------|----------|
| Persists with failing approach | Restart after 3 failed attempts |
| Vulnerable code generated | Explicit security review |
| Sounds certain but wrong | Verify critical claims |
| Long sessions degrade | Restart at ~20-30 messages |
| Treats symptoms not causes | Demand root cause analysis |

---

## Usage

### Quick Reference
Print [QUICK_REFERENCE.md](QUICK_REFERENCE.md) and keep handy.

### Integrate into Workflow
```markdown
# .cursor/rules or similar
[Copy relevant sections from rules/ai-coding-assistant-rules.md]
[Customize for your project]
```

### Team Adoption
```markdown
# CONTRIBUTING.md
## AI Assistant Guidelines
See: ai-blindspots/rules/ai-coding-assistant-rules.md
Key principles: [list 5-7 most relevant]
```

---

## Reading Paths

**Essentials (30 min):**
1. [Memento](articles/fundamentals/memento.md)
2. [Prompt Injection](articles/security/prompt-injection.md)
3. [Context Pollution](articles/context-management/context-pollution.md)

**Comprehensive (90 min):**
All 6 articles + full rules document

**By Problem:**
- Stuck? → [Context Pollution](articles/context-management/context-pollution.md)
- Security? → [Prompt Injection](articles/security/prompt-injection.md)
- Debugging? → [Debugging Blindspot](articles/debugging/debugging-blindspot.md)
- Trust issues? → [Overconfidence](articles/context-management/overconfidence.md)

---

## Quick Links

- [Quick Reference](QUICK_REFERENCE.md)
- [Complete Rules](rules/ai-coding-assistant-rules.md)
- [All Articles](articles/README.md)
- [Tool Translation Guide](TOOL_TRANSLATION_GUIDE.md) - Adapt rules for Claude Code, Codex, Gemini, Antigravity
- [Translation Examples](examples/translation-examples.md) - Side-by-side rule translations
- [Archive](archive/) (original content)

## Related

- **Source:** [ezyang.github.io/ai-blindspots](https://ezyang.github.io/ai-blindspots/) — Edward Z. Yang's original blog
- **Tool Implementations:** [../implementations/](../implementations/) — Cursor, Claude, Gemini, and more (rules aligned with these principles)
