# Security

Critical security considerations when working with AI coding assistants.

## Articles in This Category

### [Prompt Injection](prompt-injection.md)
**Understanding and preventing AI manipulation**

LLMs can be manipulated through crafted inputs to perform unintended actions, leak sensitive information, or bypass security controls.

**Covers:**
- How prompt injection works
- Attack vectors (code comments, web content, dependencies)
- Input validation strategies
- Credential handling
- Context separation
- 5 detailed attack scenarios with prevention

**Read this when:** Working with sensitive data, processing external content, before production deployment

**Criticality:** ⚠️ HIGH - Required reading for all developers

---

## Why Security Is Critical

AI assistants don't naturally consider security implications. They will:
- ❌ Suggest vulnerable patterns that "work"
- ❌ Miss injection vulnerabilities
- ❌ Not flag insecure credential handling
- ❌ Overlook access control issues

**Your vigilance is the primary defense.**

---

## Security Checklist

Before deploying AI-assisted code:
- [ ] Reviewed for SQL injection (parameterized queries?)
- [ ] Checked credential handling (no hardcoded secrets?)
- [ ] Validated input/output (sanitization present?)
- [ ] Assessed authentication/authorization (proper checks?)
- [ ] Tested with malicious input (injection attempts?)

See [prompt-injection.md](prompt-injection.md) for detailed guidance.

---

**Coming:** More security articles as new patterns emerge.

**Related:** [../../rules/ai-coding-assistant-rules.md](../../rules/ai-coding-assistant-rules.md) - Security-Specific Practices section
