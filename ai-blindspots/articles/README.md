# AI Blindspot Articles

In-depth exploration of specific AI limitations and mitigation strategies.

---

## Articles by Category

### 🎯 Fundamentals

| Article | Topics | Time | Key Insight |
|---------|--------|------|-------------|
| **[Memento](fundamentals/memento.md)** | Memory, Context, Sessions | 10 min | No persistent memory across sessions |
| **[Use Static Types](fundamentals/use-static-types.md)** | Types, Refactoring | 12 min | Types reduce overhead & guide refactoring |

### 🔒 Security

| Article | Topics | Time | Key Insight |
|---------|--------|------|-------------|
| **[Prompt Injection](security/prompt-injection.md)** | Security, Injection, Validation | 15 min | External content can manipulate AI |

### 🐛 Debugging

| Article | Topics | Time | Key Insight |
|---------|--------|------|-------------|
| **[Debugging Blindspot](debugging/debugging-blindspot.md)** | Debugging, Root Cause | 15 min | LLMs treat symptoms, not causes |

### 🧠 Context Management

| Article | Topics | Time | Key Insight |
|---------|--------|------|-------------|
| **[Context Pollution](context-management/context-pollution.md)** | Context, Sessions, Restarts | 15 min | Long conversations accumulate errors |
| **[Overconfidence](context-management/overconfidence.md)** | Trust, Confidence, Verification | 15 min | LLMs sound confident when wrong |

---

## Reading Paths

### Quick Start (30 min)
1. [Memento](fundamentals/memento.md)
2. [Prompt Injection](security/prompt-injection.md)
3. [Context Pollution](context-management/context-pollution.md)

### Comprehensive (90 min)
All 6 articles in order

### By Problem
- **Stuck?** → [Context Pollution](context-management/context-pollution.md)
- **Security?** → [Prompt Injection](security/prompt-injection.md)
- **Debugging?** → [Debugging Blindspot](debugging/debugging-blindspot.md)
- **Trust issues?** → [Overconfidence](context-management/overconfidence.md)
- **Refactoring?** → [Use Static Types](fundamentals/use-static-types.md)
- **Confused?** → [Memento](fundamentals/memento.md)

---

## Article Format

Each article includes:
- **The Blindspot** - What it is
- **Why It Happens** - Root causes
- **Impact** - What goes wrong
- **Mitigation Strategies** - Concrete solutions
- **Examples** - 3-5 real scenarios
- **Related Principles** - Links to other content
- **Current State** - What's improved/persists

---

## Usage

**During Development**
Keep relevant articles open as references.

**For Learning**
Read fundamentals first, then your focus areas.

**Team Training**
- Everyone: Fundamentals
- Security team: Prompt Injection
- Senior devs: All articles

**As Reference**
Link to articles in code reviews, PRs, documentation.

---

## Archive

Original 20 HTML articles from Edward Z. Yang's blog preserved in [../archive/original-html/](../archive/original-html/)

Topics include: Stop Digging, Black Box Testing, Walking Skeleton, Preparatory Refactoring, Requirements not Solutions, and 15 more.
