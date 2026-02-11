# AI Blindspots — Core Principles

Behavioral guidelines for AI-assisted development. Based on [AI Blindspots](https://ezyang.github.io/ai-blindspots/). Canonical source: `ai-blindspots/` in this repo.

---

## Core Principles

### Problem-Solving

- **Stop digging:** After 3 failed attempts with the same approach, propose an alternative. Do not persist-and-fail.
- **Root cause first:** Demand reproduction steps and root cause analysis before proposing fixes. Debug systematically: observe → hypothesize → test → fix.
- **Context pollution:** After ~20–30 messages without progress, suggest starting a new conversation. Summarize learnings and provide a fresh problem statement.

### Requirements and Communication

- **Specify requirements, not solutions:** Focus on constraints and goals. Unspecified requirements default to training assumptions.
- **Communicate uncertainty:** State confidence level for non-trivial recommendations. List alternatives and trade-offs.
- **Checkpoint progress:** Summarize periodically; verify assumptions early.

### Change Management

- **Decompose changes:** Break into focused, reviewable steps. Single responsibility per change.
- **Preparatory refactoring:** Make the change easy, then make the easy change.
- **Walking skeleton:** Get end-to-end basic version working before optimization.

### AI Strengths and Limitations

- **Leverage strengths:** Code generation, boilerplate, mechanical refactoring.
- **Acknowledge weaknesses:** Debugging non-obvious bugs, root cause identification, security implications.
- **Verify critical items:** LLMs sound confident when wrong.
- **Knowledge limits:** Verify library/API behavior against primary docs before relying on generated claims.

### Type Safety and Execution Hygiene

- **Type systems first:** Prefer static types and strict settings. Treat type-checker failures as blockers.
- **Static-types workflow:** Run type checks before tests and before finalizing refactors.
- **Stateless commands:** Each terminal command should be independently runnable; do not depend on prior shell state.

---

## Project Context

- Work in small, reviewable increments.
- Prioritize correctness and simplicity over cleverness.
- Black box testing: test behavior, not implementation.
- Keep files <64KB for reliable operation.
- Security review for sensitive code.
