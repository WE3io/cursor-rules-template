**Completed:** 2026-02-11 — Design doc in backlog/phase3-template-generation-design.md. Architecture options, trade-offs, rollout plan documented. Awaiting maintainer approval.

# BL-015: Phase 3 Planning for Template-Driven Generation

**Phase:** Later

## 1. Outcome
Design doc for semi-automated generation of tool formats from canonical schema. Architecture options, trade-offs, and rollout plan approved.

## 2. Constraints & References
- Depends on BL-001 schema being defined and adopted.
- Tools: Cursor, Claude, Codex, Gemini, Antigravity.
- "Semi-automated" = human review before commit; not full automation.

**References:** BL-001, BL-007, BL-008, `ai-blindspots/TOOL_TRANSLATION_GUIDE.md`.

## 3. Acceptance Checks
- [x] Design doc exists.
- [x] Architecture options documented.
- [x] Trade-offs documented.
- [x] Rollout plan documented.
- [ ] Plan approved by maintainer(s) (pending).

## 4. Explicit Non-Goals
- Implementing the generator.
- Migrating existing content to schema.
- Full automation without human review.
