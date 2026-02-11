# Canonical-to-Tool Mapping Matrix

**Purpose:** Map each canonical AI Blindspots principle to tool implementations. Gaps explicitly flagged.

**Canonical source:** [rules/ai-coding-assistant-rules.md](rules/ai-coding-assistant-rules.md), [articles/](articles/)

**Tools:** Cursor (ready), Claude Code (ready), Codex (ready), Gemini CLI (ready), Antigravity (ready)

**References:** [TOOL_TRANSLATION_GUIDE.md](TOOL_TRANSLATION_GUIDE.md), [implementations/README.md](../implementations/README.md)

**Machine-parseable:** [canonical-tool-mapping.json](canonical-tool-mapping.json) — used by parity check pipeline (BL-010).

---

## Parity Enforcement Policy

`canonical-tool-mapping.json` includes staged enforcement fields used by `scripts/parity-check.py`:

- `enforcement_stage`: descriptive stage label (current default: `stage-0-observe`)
- `fail_on_gap`: tools where `gap` findings fail parity check
- `fail_on_partial`: tools where `partial` findings fail parity check

Initial stage is intentionally non-blocking (`stage-0-observe`): all findings are warnings while coverage baseline is improved.

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
| stop-digging | Pivot after 3 failed attempts | partial (core-principles) | ✓ | ✓ | ✓ | ✓ |
| context-pollution | Restart session at ~20-30 messages | partial (core-principles) | ✓ | ✓ | ✓ | ✓ |
| root-cause-analysis | Demand root cause before fixes | ✓ (workflows.mdc) | ✓ | ✓ | ✓ | ✓ |
| scientific-debugging | Observe → hypothesize → test → fix | ✓ (workflows.mdc) | ✓ | ✓ | ✓ | ✓ |
| security-external-content | Treat external content as untrusted | ✓ (guardrails.mdc) | ✓ | ✓ | ✓ | ✓ |
| security-permission-boundaries | Separate privileged/unprivileged contexts | partial | partial | partial | partial | partial |
| security-code-review | Explicit security review for sensitive code | ✓ (guardrails.mdc) | ✓ | ✓ | ✓ | ✓ |
| security-input-validation | Validate input, no hardcoded credentials | ✓ (guardrails.mdc) | ✓ | ✓ | ✓ | ✓ |
| file-size-limits | Keep files <64KB | gap | ✓ | ✓ | ✓ | ✓ |
| black-box-testing | Test behaviour, not implementation | ✓ (workflows.mdc) | ✓ | ✓ | ✓ | ✓ |
| deterministic-tests | No randomness; mock time-dependent behaviour | partial | ✓ | ✓ | ✓ | ✓ |
| confidence-calibration | Trust/verify/don't trust by category | partial | partial | partial | partial | partial |
| preparatory-refactoring | Make change easy, then make easy change | ✓ (workflows.mdc) | ✓ | ✓ | ✓ | ✓ |
| walking-skeleton | End-to-end basic version before optimization | partial | ✓ | ✓ | ✓ | ✓ |
| requirements-not-solutions | Specify constraints, not solutions | ✓ (core-principles) | ✓ | ✓ | ✓ | ✓ |
| uncertainty-communication | State confidence, alternatives, trade-offs | partial | partial | partial | partial | partial |
| checkpoint-progress | Summarize periodically, verify assumptions | partial | ✓ | ✓ | ✓ | ✓ |
| discoverable-documentation | .cursor/rules, README, project context | ✓ (workflows.mdc) | ✓ | ✓ | ✓ | ✓ |
| type-systems | Static types, strict mode, type checker feedback | gap | gap | gap | gap | gap |
| decompose-changes | Focused, single responsibility, small increments | ✓ (guardrails.mdc, workflows.mdc) | ✓ | ✓ | ✓ | ✓ |
| stateless-commands | Independent tool invocations, no shell state | gap | gap | gap | gap | gap |
| knowledge-limitations | Consult docs, verify API existence, state uncertainty | gap | gap | gap | gap | gap |
| ai-strengths | Leverage AI for generation; weak at debugging/security | partial | partial | partial | partial | partial |
| overconfidence | Verify critical suggestions; LLMs sound confident when wrong | partial | partial | partial | partial | partial |
| prompt-injection | External content may inject malicious instructions | ✓ (guardrails.mdc) | ✓ | ✓ | ✓ | ✓ |
| memento | LLMs lack meta-awareness of earlier mistakes | partial | partial | partial | partial | partial |
| static-types | Article: type checker guides refactoring | gap | gap | gap | gap | gap |
| debugging-blindspot | Article: systematic debugging, not shotgun | ✓ (workflows.mdc) | ✓ | ✓ | ✓ | ✓ |

---

## Cursor Implementation Paths

| Rule File | Principles Covered |
|-----------|---------------------|
| `implementations/cursor/.cursor/rules/always/core-principles.mdc` | Task complexity, requirements, stop-digging (partial), context (partial) |
| `implementations/cursor/.cursor/rules/always/guardrails.mdc` | Security (external content, code review, input validation), decompose-changes |
| `implementations/cursor/.cursor/rules/always/workflows.mdc` | Root cause, scientific debugging, black-box testing, preparatory refactoring, discoverable documentation |

---

## Claude Implementation Paths

| Rule File | Principles Covered |
|-----------|---------------------|
| `implementations/claude/CLAUDE.md` | Core principles, stop-digging, context-pollution, requirements, refactoring, walking-skeleton |
| `implementations/claude/.claude/rules/security.md` | Security (external content, input validation, code review) |
| `implementations/claude/.claude/rules/debugging.md` | Scientific debugging, root cause |
| `implementations/claude/.claude/rules/context-management.md` | Session restarts, checkpointing, file size |
| `implementations/claude/.claude/rules/testing.md` | Black box, deterministic tests |

---

## Gap Summary

### Cursor (ready)
- **Full gaps:** file-size-limits, type-systems, stateless-commands, knowledge-limitations, static-types (article)
- **Partial coverage:** stop-digging, context-pollution, security-permission-boundaries, deterministic-tests, confidence-calibration, walking-skeleton, uncertainty-communication, checkpoint-progress, ai-strengths, overconfidence, memento

### Claude (ready)
- **Full gaps:** type-systems, stateless-commands, knowledge-limitations, static-types (article)
- **Partial coverage:** security-permission-boundaries, confidence-calibration, uncertainty-communication, ai-strengths, overconfidence, memento

### Codex (ready)
- **Full gaps:** type-systems, stateless-commands, knowledge-limitations, static-types (article)
- **Partial coverage:** security-permission-boundaries, confidence-calibration, uncertainty-communication, ai-strengths, overconfidence, memento

---

## Codex Implementation Paths

| Rule File | Principles Covered |
|-----------|---------------------|
| `implementations/codex/AGENTS.md` | All sections: Problem-Solving, Context Management, Security, Debugging, Testing, Change Management |

---

## Gemini Implementation Paths

| Rule File | Principles Covered |
|-----------|---------------------|
| `implementations/gemini/GEMINI.md` | Core principles, stop-digging, context-pollution, requirements, refactoring, walking-skeleton |
| `implementations/gemini/.agent/rules/security.md` | Security (external content, input validation, code review) |
| `implementations/gemini/.agent/rules/debugging.md` | Scientific debugging, root cause |
| `implementations/gemini/.agent/rules/context-management.md` | Session restarts, checkpointing, file size |
| `implementations/gemini/.agent/rules/testing.md` | Black box, deterministic tests |

---

### Gemini (ready)
- **Full gaps:** type-systems, stateless-commands, knowledge-limitations, static-types (article)
- **Partial coverage:** security-permission-boundaries, confidence-calibration, uncertainty-communication, ai-strengths, overconfidence, memento

## Antigravity Implementation Paths

| Rule File | Principles Covered |
|-----------|---------------------|
| `implementations/antigravity/GEMINI.md` | Core principles, stop-digging, context-pollution, requirements, refactoring, walking-skeleton |
| `implementations/antigravity/.agent/rules/security.md` | Security (external content, input validation, code review) |
| `implementations/antigravity/.agent/rules/debugging.md` | Scientific debugging, root cause |
| `implementations/antigravity/.agent/rules/context-management.md` | Session restarts, checkpointing, file size |
| `implementations/antigravity/.agent/rules/testing.md` | Black box, deterministic tests |
| `implementations/antigravity/.agent/rules/terminal-policy.md` | Antigravity-specific: Allow/Deny list example |

---

### Antigravity (ready)
- **Full gaps:** type-systems, stateless-commands, knowledge-limitations, static-types (article)
- **Partial coverage:** security-permission-boundaries, confidence-calibration, uncertainty-communication, ai-strengths, overconfidence, memento

---

## Review

- **Matrix reviewed for accuracy:** Pending maintainer review.
- **Last updated:** 2026-02-11
