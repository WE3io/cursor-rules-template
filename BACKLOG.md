# Backlog

Work items to operationalize periodic research updates for canonical AI guidance and downstream tool-specific translations.

## Now

1. **BL-001: Define Canonical Guidance Schema**
- Outcome: Standard structure for each rule/guidance item (`id`, `title`, `intent`, `rationale`, `examples`, `risk`, `confidence`, `sources`, `owner`, `review_date`).
- Acceptance criteria: Schema documented with examples and maintainer review completed.

2. **BL-002: Add Change Acceptance Criteria**
- Outcome: Explicit quality gate for canonical updates.
- Acceptance criteria: Checklist covers clarity, actionability, testability, portability, and evidence quality.

3. **BL-003: Create Research Intake Template**
- Outcome: Consistent capture format for candidate updates.
- Acceptance criteria: Template includes source links, summary, category, confidence, and expected impact.

4. **BL-004: Create Canonical Decision Record Template**
- Outcome: Lightweight decision log for accepted/rejected changes.
- Acceptance criteria: Record captures decision, rationale, alternatives, and risk of no-change.

5. **BL-005: Establish Triage Gate Workflow**
- Outcome: Weekly 15-minute triage cadence with clear go/no-go decisioning.
- Acceptance criteria: Cadence, owner, and triage checklist documented.

6. **BL-006: Build Change Manifest Format**
- Outcome: Standard delta artifact per release (added/changed/removed/deprecated).
- Acceptance criteria: Manifest format documented and used in at least one cycle.

## Next

1. **BL-007: Define Canonical-to-Tool Mapping Matrix**
- Outcome: Mapping of each canonical principle to Cursor, Codex, Claude, Gemini, and Antigravity.
- Acceptance criteria: Coverage complete for current principles; gaps explicitly flagged.

2. **BL-008: Create Tool Translation Checklists**
- Outcome: Per-tool validation checklist for semantic parity.
- Acceptance criteria: Each tool has a checklist that verifies intent preservation and mechanism adaptation.

3. **BL-009: Add Docs QA Pipeline**
- Outcome: Automated markdown lint, link checks, and required-section checks.
- Acceptance criteria: Pipeline runs on PRs and blocks on failures.

4. **BL-010: Add Parity Check Pipeline**
- Outcome: Automated canonical-to-tool coverage/parity report.
- Acceptance criteria: Report generated in CI; missing mappings surfaced as failures or warnings.

5. **BL-011: Add Staleness/Sunset Tracking**
- Outcome: Alerts for overdue review dates on guidance items.
- Acceptance criteria: Stale-item report includes owner and due date.

## Later

1. **BL-012: Define Release Workflow**
- Outcome: Lightweight monthly release flow with urgent security patch path.
- Acceptance criteria: Checklist, versioning policy, and emergency patch protocol documented.

2. **BL-013: Add KPI Dashboard Spec**
- Outcome: Effectiveness metrics for the process.
- Acceptance criteria: Definitions and cadence for `time-to-update`, `translation parity %`, and `post-release defects`.

3. **BL-014: Pilot One End-to-End Cycle**
- Outcome: Trial run across intake, canonical edits, translation, validation, and release.
- Acceptance criteria: Retrospective completed and follow-up backlog refinements captured.

4. **BL-015: Phase 3 Planning for Template-Driven Generation**
- Outcome: Design doc for semi-automated generation of tool formats from canonical schema.
- Acceptance criteria: Architecture options, trade-offs, and rollout plan approved.
