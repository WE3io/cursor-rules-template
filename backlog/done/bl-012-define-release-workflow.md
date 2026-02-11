**Completed:** 2026-02-11 — Release workflow in backlog/release-workflow.md (checklist, versioning, emergency protocol); first release executed via backlog/manifests/2026-02-11-later-phase-release-workflow.md.

# BL-012: Define Release Workflow

**Phase:** Later

## 1. Outcome
Lightweight monthly release flow with urgent security patch path. Checklist, versioning policy, and emergency patch protocol documented.

## 2. Constraints & References
- Uses BL-006 Change Manifest for delta tracking.
- Must support both routine and emergency releases.
- Monthly cadence is a target, not a hard constraint.

**References:** BL-006.

## 3. Acceptance Checks
- [x] Release checklist documented.
- [x] Versioning policy documented.
- [x] Emergency patch protocol documented.
- [x] At least one release executed using workflow.

## 4. Explicit Non-Goals
- Automating release steps.
- KPI dashboard (BL-013).
- Template-driven generation (BL-015).
