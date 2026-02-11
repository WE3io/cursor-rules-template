# Canonical-to-Tool Mapping Matrix

**Purpose:** Map each canonical AI Blindspots principle to tool implementations. Gaps explicitly flagged.

**Canonical source:** [rules/ai-coding-assistant-rules.md](rules/ai-coding-assistant-rules.md), [articles/](articles/)

**Tools:** Cursor (ready), Claude Code, Codex, Gemini CLI, Antigravity (planned)

**References:** [TOOL_TRANSLATION_GUIDE.md](TOOL_TRANSLATION_GUIDE.md), [implementations/README.md](../implementations/README.md)

**Machine-parseable:** [canonical-tool-mapping.json](canonical-tool-mapping.json) — used by parity check pipeline (BL-010).

---

## Legend

| Symbol | Meaning |
|--------|---------|
| ✓ | Implemented in tool |
| partial | Partially covered |
| gap | Not implemented (planned) |

---

## Mapping Matrix

| Canonical ID | Principle | Cursor | Claude | Codex | Gemini | Antigravity |
|--------------|-----------|--------|--------|-------|--------|-------------|
| stop-digging | Pivot after 3 failed attempts | partial (core-principles) | gap | gap | gap | gap |
| context-pollution | Restart session at ~20-30 messages | partial (core-principles) | gap | gap | gap | gap |
| root-cause-analysis | Demand root cause before fixes | ✓ (workflows.mdc) | gap | gap | gap | gap |
| scientific-debugging | Observe → hypothesize → test → fix | ✓ (workflows.mdc) | gap | gap | gap | gap |
| security-external-content | Treat external content as untrusted | ✓ (guardrails.mdc) | gap | gap | gap | gap |
| security-permission-boundaries | Separate privileged/unprivileged contexts | partial | gap | gap | gap | gap |
| security-code-review | Explicit security review for sensitive code | ✓ (guardrails.mdc) | gap | gap | gap | gap |
| security-input-validation | Validate input, no hardcoded credentials | ✓ (guardrails.mdc) | gap | gap | gap | gap |
| file-size-limits | Keep files <64KB | gap | gap | gap | gap | gap |
| black-box-testing | Test behaviour, not implementation | ✓ (workflows.mdc) | gap | gap | gap | gap |
| deterministic-tests | No randomness; mock time-dependent behaviour | partial | gap | gap | gap | gap |
| confidence-calibration | Trust/verify/don't trust by category | partial | gap | gap | gap | gap |
| preparatory-refactoring | Make change easy, then make easy change | ✓ (workflows.mdc) | gap | gap | gap | gap |
| walking-skeleton | End-to-end basic version before optimization | partial | gap | gap | gap | gap |
| requirements-not-solutions | Specify constraints, not solutions | ✓ (core-principles) | gap | gap | gap | gap |
| uncertainty-communication | State confidence, alternatives, trade-offs | partial | gap | gap | gap | gap |
| checkpoint-progress | Summarize periodically, verify assumptions | partial | gap | gap | gap | gap |
| discoverable-documentation | .cursor/rules, README, project context | ✓ (workflows.mdc) | gap | gap | gap | gap |
| type-systems | Static types, strict mode, type checker feedback | gap | gap | gap | gap | gap |
| decompose-changes | Focused, single responsibility, small increments | ✓ (guardrails.mdc, workflows.mdc) | gap | gap | gap | gap |
| stateless-commands | Independent tool invocations, no shell state | gap | gap | gap | gap | gap |
| knowledge-limitations | Consult docs, verify API existence, state uncertainty | gap | gap | gap | gap | gap |
| ai-strengths | Leverage AI for generation; weak at debugging/security | partial | gap | gap | gap | gap |
| overconfidence | Verify critical suggestions; LLMs sound confident when wrong | partial | gap | gap | gap | gap |
| prompt-injection | External content may inject malicious instructions | ✓ (guardrails.mdc) | gap | gap | gap | gap |
| memento | LLMs lack meta-awareness of earlier mistakes | partial | gap | gap | gap | gap |
| static-types | Article: type checker guides refactoring | gap | gap | gap | gap | gap |
| debugging-blindspot | Article: systematic debugging, not shotgun | ✓ (workflows.mdc) | gap | gap | gap | gap |

---

## Cursor Implementation Paths

| Rule File | Principles Covered |
|-----------|---------------------|
| `implementations/cursor/.cursor/rules/always/core-principles.mdc` | Task complexity, requirements, stop-digging (partial), context (partial) |
| `implementations/cursor/.cursor/rules/always/guardrails.mdc` | Security (external content, code review, input validation), decompose-changes |
| `implementations/cursor/.cursor/rules/always/workflows.mdc` | Root cause, scientific debugging, black-box testing, preparatory refactoring, discoverable documentation |

---

## Gap Summary

### Cursor (ready)
- **Full gaps:** file-size-limits, type-systems, stateless-commands, knowledge-limitations, static-types (article)
- **Partial coverage:** stop-digging, context-pollution, security-permission-boundaries, deterministic-tests, confidence-calibration, walking-skeleton, uncertainty-communication, checkpoint-progress, ai-strengths, overconfidence, memento

### Claude, Codex, Gemini, Antigravity (planned)
- **All principles:** gap — no implementations yet

---

## Review

- **Matrix reviewed for accuracy:** Pending maintainer review.
- **Last updated:** 2026-02-11
