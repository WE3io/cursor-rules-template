# Memento

*Updated: February 2026*
*Original: March 2025*

## The Blindspot

LLMs have two distinct memory limitations that affect how they work: no persistent memory across sessions, and limited context within sessions. Understanding both is crucial for effective collaboration.

## Why It Happens

Like the protagonist in the film Memento who cannot form new memories, LLMs operate with constrained memory—but the constraints work differently than many people assume.

**Session Context (What LLMs HAVE):**
- Full conversation history within the current chat
- All previous messages and responses
- Accumulated context and decisions
- Files and information explicitly loaded

**Persistent Memory (What LLMs LACK):**
- No memory across different conversations
- No learned preferences from past sessions
- No accumulated knowledge about your codebase
- Must rebuild understanding from scratch each new chat

This means each new conversation is a "cold start" where the LLM must reconstruct:
- Your project structure and architecture
- Coding conventions and patterns
- Previous decisions and rationale
- Domain knowledge and context

## Impact

**Within a Session:**
- ✅ LLM remembers previous exchanges
- ✅ Can build on earlier work
- ✅ Maintains consistency with decisions made
- ❌ But context can become "polluted" with errors over time
- ❌ Long conversations may lose early context details

**Across Sessions:**
- ❌ Complete loss of previous session context
- ❌ Must re-explain project structure
- ❌ Previous insights and decisions forgotten
- ❌ Code review patterns not retained

**The Marvel and the Fragility:**
> "The marvel is not that the bear dances well, but that the bear dances at all."

It's incredible that LLMs can reconstruct understanding of complex codebases from scratch each request. But this is fragile—if the wrong files enter context or the LLM forms an incorrect mental model, it can quickly go astray.

## Mitigation Strategies

### 1. Provide Persistent Documentation

Since LLMs can't remember across sessions, create documentation they can reference:

**Project Context Files:**
```
.cursor/rules           # Project conventions and patterns
README.md               # Architecture overview
CONTRIBUTING.md         # Development workflow
docs/architecture.md    # System design decisions
docs/conventions.md     # Code standards
```

**Effective .cursor/rules example:**
```markdown
# Project: E-commerce Platform

## Architecture
- Microservices: auth, products, orders, payments
- Event-driven with RabbitMQ
- PostgreSQL for transactional data, Redis for caching

## Conventions
- TypeScript with strict mode
- Test coverage >80%
- All API changes require migration scripts
- Use repository pattern for data access

## Common Patterns
- Authentication: JWT tokens in Authorization header
- Error handling: Custom AppError classes
- Validation: Zod schemas for all inputs
```

### 2. Strategic Session Management

**When to Start a New Session:**
- ✅ After completing a major feature
- ✅ When changing focus to different subsystem
- ✅ If LLM seems confused or stuck
- ✅ When context feels "polluted" with errors

**When to Continue Existing Session:**
- ✅ Iterating on same component
- ✅ Related bug fixes
- ✅ When context is valuable and accurate

### 3. Explicit Context Loading

Help the LLM load the right context upfront:

**Good Prompts:**
```
"I'm working on the payment service. Key files:
- src/services/payment/processor.ts
- src/services/payment/stripe-client.ts
- tests/payment/processor.test.ts"

"This is a React app using Redux Toolkit. Load:
- src/store/userSlice.ts to see state shape
- src/components/UserProfile.tsx for the component I'm modifying"
```

**Avoid:**
```
"Fix the bug" (what bug? where? what context?)
"Make it faster" (make what faster? need performance profile)
```

### 4. Make Information Discoverable

Structure your project so LLMs can find what they need:

**Good Structure:**
```
src/
  features/
    auth/
      README.md          # Feature-specific docs
      auth.service.ts
      auth.test.ts
    products/
      README.md
      products.service.ts
      products.test.ts
```

**Each feature README:**
```markdown
# Auth Feature

## Purpose
Handles user authentication and authorization

## Key Components
- `auth.service.ts` - Core authentication logic
- `jwt.util.ts` - Token management
- `auth.middleware.ts` - Express middleware

## External Dependencies
- bcrypt for password hashing
- jsonwebtoken for JWT creation

## Common Operations
[Examples of typical tasks]
```

### 5. Avoid Misalignment on Major Changes

For significant architectural changes, provide comprehensive context:

**Bad:**
```
"Add end-to-end testing to this project"
```

**Good:**
```
"Add end-to-end testing to this project.

Current state:
- Express REST API
- Postgres database
- Unit tests with Jest
- No E2E tests yet

Goal:
- Add Playwright for E2E testing
- Test critical user flows: signup, login, checkout
- Integrate with CI pipeline
- Keep tests fast (<5min total runtime)
```

## Examples

### Example 1: The README Rewrite

**Scenario:** Asked Sonnet 3.7 to create E2E testing plan for existing project.

**What Happened:** Sonnet interpreted "testing" as the entire purpose of the repository and rewrote the README to focus exclusively on testing, removing all information about the actual application.

**Root Cause:** Without sufficient context about the project's actual purpose, the LLM latched onto "testing" as the primary concern.

**Fix:** Provide broader context: "This is a production web app that handles X. We want to ADD E2E testing to our existing test suite."

### Example 2: Context Pollution in Long Session

**Scenario:** 50-message conversation debugging a complex issue.

**What Happened:**
- Message 10: LLM formed incorrect hypothesis
- Messages 11-25: Changes based on wrong assumption
- Messages 26-50: Trying to fix symptoms, not root cause
- Confusion compounding with each iteration

**Fix:** Started fresh session with:
```
"Starting fresh. The issue is: [clear description]
Root cause analysis from previous session: [summary]
Already tried: [list of failed attempts]
Next approach: [what to try]"
```

Result: Fixed in 5 messages with clear context.

### Example 3: Cross-Session Knowledge Loss

**Session 1 (Tuesday):**
```
User: "We use Factory pattern for all service creation"
LLM: "Understood. I'll use ServiceFactory for the new feature."
[Implements correctly]
```

**Session 2 (Wednesday):**
```
User: "Add another service"
LLM: [Uses direct instantiation, not factory pattern]
```

**Fix:** Add to .cursor/rules:
```markdown
## Service Creation Pattern
Always use ServiceFactory for service instantiation.
Never use `new Service()` directly.

Example:
const userService = ServiceFactory.create('UserService');
```

### Example 4: Effective Context Priming

**Ineffective:**
```
"There's a bug in the login"
```

**Effective:**
```
"Bug in login flow:

Symptom: Users can't log in with valid credentials
Affected file: src/auth/login.controller.ts
Recent changes: Added rate limiting last week
Error: 'Invalid token' but password is correct

Relevant context:
- JWT signing in src/utils/jwt.ts
- User model in src/models/user.model.ts
- Rate limit config in src/middleware/rate-limit.ts

I suspect the rate limiting is interfering with token generation."
```

## Related Principles

- **Mise en Place** - Prepare context before starting
- **Know Your Limits** - Understand what information the LLM needs
- **Requirements, not Solutions** - Specify the problem context clearly
- **Read the Docs** - Provide documentation the LLM can reference

## Current State (2026)

**Improvements:**
- Longer context windows (200K+ tokens) allow more information
- Better retrieval mechanisms (MCP, RAG) improve context loading
- Agentic modes proactively load relevant files

**Persistent Limitations:**
- Still no persistent memory across sessions
- Still need to rebuild understanding each conversation
- Context pollution still occurs in very long sessions

**Best Practices:**
1. Invest in good project documentation
2. Use .cursor/rules or equivalent for persistent guidance
3. Be strategic about session boundaries
4. Provide explicit context for complex tasks
5. Restart sessions when confusion sets in

**Remember:** The LLM is speed-running understanding your entire codebase from scratch every time you start a new chat. Help it succeed by making critical information easy to find and understand.
