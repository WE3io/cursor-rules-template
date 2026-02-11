# Context Management

Understanding and managing AI conversation context effectively.

## Articles in This Category

### [Context Pollution](context-pollution.md)
**When and how long conversations degrade**

Long conversations accumulate errors and misconceptions. Early mistakes compound over time, making later responses progressively less reliable.

**Covers:**
- How context pollutes over time
- Symptoms of pollution
- When to restart (decision tree)
- Fresh start strategies
- Checkpoint patterns
- 5 pollution spiral examples

**Read this when:** Past 20 messages, going in circles, AI seems confused

---

### [Overconfidence](overconfidence.md)
**Why LLMs sound certain even when wrong**

LLMs consistently express high confidence regardless of actual knowledge, making it difficult to calibrate trust.

**Covers:**
- Why overconfidence happens
- Trust hierarchy (high/medium/low)
- Red flags for overconfidence
- Verification checklist
- Calibration techniques
- 5 overconfident failure examples

**Read this when:** Uncertain about AI suggestions, critical decisions, security-sensitive code

---

## The Context Management Challenge

**Within a session:**
- ✅ AI remembers previous messages
- ✅ Builds on earlier work
- ❌ Accumulates errors over time
- ❌ Can't self-correct polluted context

**Across sessions:**
- ❌ No memory of previous conversations
- ❌ Must rebuild understanding from scratch
- ✅ Clean slate (can be advantage!)

---

## When to Restart Session

```
Message count > 20?
├─ No → Continue
└─ Yes → Making clear progress?
    ├─ Yes → Continue (checkpoint)
    └─ No → Errors repeating?
        ├─ Yes → RESTART NOW
        └─ No → Complexity increasing?
            ├─ Yes → RESTART NOW
            └─ No → Continue with caution
```

**See [context-pollution.md](context-pollution.md) for full decision tree.**

---

## Trust Calibration

| Trust Level | Examples | Action |
|-------------|----------|--------|
| **High** | Standard algorithms, basic language features | Use directly |
| **Medium** | Framework patterns, library APIs | Verify docs |
| **Low** | Security implications, recent versions | Test thoroughly |

**See [overconfidence.md](overconfidence.md) for detailed calibration guide.**

---

## Quick Rules

**Context Pollution:**
- ↻ Restart after ~20-30 messages without progress
- 📝 Checkpoint progress every 10-15 messages
- 🔄 Fresh start template for new sessions

**Overconfidence:**
- ✅ Verify critical claims
- ⚠️ Watch for absolutist language ("always", "never")
- 🔬 Demand evidence for important decisions

---

**Related:**
- [../fundamentals/memento.md](../fundamentals/memento.md) - Memory limitations
- [../debugging/debugging-blindspot.md](../debugging/debugging-blindspot.md) - When debugging pollutes context
- [../../rules/](../../rules/) - Complete rules with more detail
