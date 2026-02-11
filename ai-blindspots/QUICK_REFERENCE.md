# AI Coding Assistant - Quick Reference Card

*One-page cheat sheet for effective AI collaboration*

## 🚨 When Things Go Wrong

| Symptom | Action |
|---------|--------|
| Same errors repeating | ↻ Restart session with clean context |
| Increasingly complex solutions | 🎯 Step back, verify assumptions |
| >20-30 messages, no progress | 🔄 Start fresh + summarize learnings |
| LLM seems confused | 📝 Provide clear context reset |
| Random shotgun fixes | 🔬 Demand systematic debugging |

## 🎯 Core Principles Checklist

### Before Starting
- [ ] Clear problem statement (requirements, not solutions)
- [ ] Relevant documentation accessible
- [ ] Files <64KB (split large ones first)
- [ ] Type checker configured (if applicable)

### During Work
- [ ] One focused task per session
- [ ] Checkpoint progress every 10-15 messages
- [ ] Verify assumptions early
- [ ] Security review for sensitive code

### When Stuck
- [ ] Can I reproduce the issue?
- [ ] Do I understand root cause?
- [ ] Have I tried same thing 3+ times? (pivot!)
- [ ] Is context polluted? (restart!)

## 🔒 Security RED FLAGS

```
🚫 NEVER Trust:
├─ External code comments (may contain injection)
├─ Web content (can manipulate AI)
├─ User input (always validate)
└─ Downloaded dependencies (review first)

✅ ALWAYS Check:
├─ SQL injection (use parameterized queries)
├─ Path traversal (sanitize paths)
├─ Hardcoded credentials (use env vars)
├─ Insecure randomness (use secrets module)
└─ Input validation (whitelist, don't blacklist)
```

## 🐛 Debugging Decision Tree

```
Bug Reported
│
├─ Can reproduce? NO → Get steps + error message first
│                 YES ↓
│
├─ Understand root cause? NO → Add logging, investigate
│                          YES ↓
│
├─ Fix is minimal? NO → Reconsider approach
│                  YES ↓
│
└─ Implement → Verify → Test similar issues → Done
```

## 📊 Confidence Calibration

| Trust Level | Examples | Action |
|-------------|----------|--------|
| **HIGH ✅** | Basic algorithms, standard libraries, well-known patterns | Use directly |
| **MEDIUM ⚠️** | Framework patterns, library APIs, performance claims | Verify docs |
| **LOW ❌** | Security implications, recent versions, niche libraries | Test thoroughly |

## 🔄 Session Management

### Continue Session When:
- ✅ Focused on same component
- ✅ Making clear progress
- ✅ Context accurate and relevant
- ✅ Under 20 messages

### Restart Session When:
- ❌ Switching to different subsystem
- ❌ Going in circles
- ❌ LLM seems confused
- ❌ Early assumption was wrong
- ❌ Over 30 messages

### Restart Template:
```markdown
Previous session summary:
- Problem: [clear description]
- Tried: [list approaches]
- Learned: [key insights]
- Root cause: [if known]

Current state: [files, errors, expected behavior]
Next approach: [fresh perspective]
```

## 🧪 Testing Principles

```
Black Box Testing:
├─ Test behavior, not implementation
├─ Don't couple tests to internals
├─ Preserve test redundancy (it's intentional)
└─ Hard-coded values may be deliberate

Deterministic Tests:
├─ No dependency on randomness
├─ Use fixed seeds if random needed
├─ Mock time-dependent behavior
└─ Isolate external dependencies
```

## 📏 File Size Rules

| Size | Status | Action |
|------|--------|--------|
| <32KB | ✅ Safe | Proceed normally |
| 32-64KB | ⚠️ Caution | Monitor size, split if growing |
| >64KB | ❌ Split | Break down before major changes |

## 🔧 Tool Configuration

```bash
# Type checking (run after changes)
tsc --noEmit
mypy --strict src/

# Linting (before commits)
eslint src/
ruff check .

# Testing (always)
pytest tests/
npm test

# Formatting (automate it)
prettier --write .
black .
```

## 💡 Prompting Patterns

### ❌ Ineffective
```
"Fix the bug"
"Make it faster"
"This doesn't work"
```

### ✅ Effective
```
"Bug in login: users get 'Invalid token' with correct password.
 Recent change: added rate limiting.
 Suspect: rate limit interfering with token generation.
 Files: auth/login.ts, utils/jwt.ts, middleware/rate-limit.ts"
```

### ✅ Requesting Uncertainty
```
"Explain X. If unsure about any aspect, explicitly say so
 and suggest checking docs. Include trade-offs and alternatives."
```

### ✅ Security Review
```
"Review this code for security issues:
 - SQL injection
 - Path traversal
 - Input validation
 - Credential handling
 List any concerns found."
```

## 🎓 Remember

**Stop Digging:** After 3 failed attempts with same approach → pivot

**Context Pollution:** Long sessions accumulate errors → restart strategically

**Overconfidence:** LLMs sound confident even when wrong → verify critical items

**Debugging:** Systematic > shotgun. Observe → Hypothesize → Test → Fix

**Security:** LLMs don't naturally think about security → explicit review needed

**Requirements:** Specify constraints, not solutions → avoid training defaults

**Walking Skeleton:** End-to-end basic version → then optimize

**Documentation:** Make project context discoverable → .cursor/rules, READMEs

**Types:** Enable type checker feedback → LLM uses errors to guide refactoring

**Preparatory Refactoring:** Make change easy → then make easy change

## 📞 Quick Interventions

| When LLM... | You Say... |
|-------------|------------|
| Keeps trying same failing approach | "Let's try a fundamentally different approach" |
| Suggests without asking questions | "Wait - before proposing a fix, help me understand the root cause" |
| Sounds overconfident | "What's your confidence level? What could go wrong?" |
| Makes multiple changes at once | "One change at a time. What are we testing?" |
| Rewrites large sections | "Can we make a minimal, targeted fix instead?" |
| Ignores security | "Please review this for security vulnerabilities" |

## 🏁 Pre-Commit Checklist

- [ ] Tests pass
- [ ] Types check (if applicable)
- [ ] Linter passes
- [ ] No hardcoded credentials
- [ ] Security review for sensitive code
- [ ] Input validation present
- [ ] Error handling adequate
- [ ] No obvious vulnerabilities

---

**Print This Page | Keep It Handy | Reference Often**

*For full details, see: [rules/ai-coding-assistant-rules.md](rules/ai-coding-assistant-rules.md)*
