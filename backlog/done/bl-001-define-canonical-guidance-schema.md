**Completed:** 2026-02-11 — Schema documented with all fields; worked example in backlog/templates/canonical-guidance-schema.md. Sign-off blocked: requires verification that rules are implemented correctly across tools (Cursor, Claude, Codex, Gemini, Antigravity) before maintainer can sign off.

# BL-001: Define Canonical Guidance Schema

**Phase:** Now

## 1. Outcome
Standard structure for each rule/guidance item is documented. Schema includes: `id`, `title`, `intent`, `rationale`, `examples`, `risk`, `confidence`, `sources`, `owner`, `review_date`. At least one worked example exists. Maintainer review completed.

## 2. Constraints & References
- Schema must support downstream tool translation (Cursor, Claude, Codex, Gemini, Antigravity).
- Canonical source: `ai-blindspots/rules/`, `ai-blindspots/articles/`.

**References:** None.

## 3. Acceptance Checks
- [x] Schema document exists with all fields defined.
- [x] Worked example(s) demonstrate schema usage.
- [ ] Maintainer review completed and signed off (blocked: verify implementations across tools first).

## 4. Explicit Non-Goals
- Migrating existing content to schema (separate work).
- Implementing tool-specific mappings.
- Automation or tooling to enforce schema.
