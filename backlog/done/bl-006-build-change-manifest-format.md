**Completed:** 2026-02-11 — Format in backlog/templates/change-manifest-format.md; manifest 2026-02-11-now-phase created.

# BL-006: Build Change Manifest Format

**Phase:** Now

## 1. Outcome
Standard delta artifact per release. Manifest records added/changed/removed/deprecated guidance items.

## 2. Constraints & References
- Must align with BL-001 schema (ids, review dates).
- Feeds downstream tool translation (BL-007, BL-008) and parity checks (BL-010).

**References:** None.

## 3. Acceptance Checks
- [x] Manifest format documented.
- [x] Format supports: added, changed, removed, deprecated.
- [x] Used in at least one release cycle.

## 4. Explicit Non-Goals
- Implementing release workflow (BL-012).
- Automated manifest generation.
- Parity check pipeline (BL-010).
