# Debugging

Understanding why AI assistants struggle with debugging and how to work around it.

## Articles in This Category

### [Debugging Blindspot](debugging-blindspot.md)
**Why LLMs are better at generation than debugging**

LLMs tend to treat symptoms rather than identify root causes, make changes without full understanding, and struggle with non-obvious bugs.

**Covers:**
- Generation vs. comprehension asymmetry
- Scientific debugging method (5 steps)
- Root cause analysis
- Avoiding shotgun debugging
- When to restart approach
- 5 debugging failure examples

**Read this when:** Debugging not working, going in circles, getting surface fixes

---

## The Debugging Problem

**LLMs excel at:**
- ✅ Writing new code from specifications
- ✅ Implementing known patterns
- ✅ Generating boilerplate

**LLMs struggle with:**
- ❌ Understanding runtime behavior from static code
- ❌ Identifying non-obvious root causes
- ❌ Systematic hypothesis testing
- ❌ Recognizing when to give up an approach

---

## Scientific Debugging Method

Use this systematic approach instead of hoping AI finds the bug:

```
1. OBSERVE
   - Actual vs. expected behavior?
   - When does it happen/not happen?
   - Error messages/logs?

2. HYPOTHESIZE
   - What could cause this?
   - 2-3 most likely causes?

3. TEST
   - How to verify each hypothesis?
   - Run the test

4. ANALYZE
   - What did test reveal?
   - Confirmed or rejected?

5. FIX
   - Address root cause (not symptom)
   - Verify fix
   - Check for similar issues
```

**You drive the investigation. AI assists.**

---

## Quick Debugging Rules

- 🔬 Require reproduction before fixing
- 📊 Add instrumentation, don't modify code blindly
- 🎯 One change at a time
- 🚫 Stop after 3 failed attempts with same approach
- 📝 Document what works and doesn't

**See full article for details and examples.**

---

**Related:** [../context-management/context-pollution.md](../context-management/context-pollution.md) - When debugging sessions go too long
