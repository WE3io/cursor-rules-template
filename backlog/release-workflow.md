# Release Workflow

Lightweight monthly release flow with urgent security patch path. Uses [Change Manifest Format](templates/change-manifest-format.md) (BL-006) for delta tracking.

---

## Versioning Policy

- **Format:** `YYYY-MM-DD` (date-based)
- **When to bump:** Each release gets a new version = release date
- **Example:** Release on 2026-02-11 → version `2026-02-11`
- **Cadence:** Monthly target; release when changes warrant (not a hard constraint)

---

## Release Checklist (Routine)

Before each routine release:

1. [ ] **QA passed** — Run docs-qa, parity-check, staleness-check
2. [ ] **Manifest drafted** — List added/changed/removed/deprecated items
3. [ ] **Links validated** — No broken references
4. [ ] **Manifest finalized** — Save to `backlog/manifests/YYYY-MM-DD-*.md`
5. [ ] **Tag or announce** — Optional; version is date-based

---

## Emergency Patch Protocol

For urgent security or critical fixes:

1. **Assess** — Confirm severity; decide if routine cycle is acceptable
2. **Minimal change** — Only the fix; no unrelated edits
3. **Apply fix** — Canonical edit + translation as needed
4. **Run checks** — QA, parity (abbreviated is acceptable; do not skip critical path)
5. **Release** — Create manifest with version = patch date; note "Emergency patch" in rationale
6. **Follow-up** — Include in next routine release manifest if not already covered

---

## Related

- [Change Manifest Format](templates/change-manifest-format.md)
- [Triage Gate Workflow](triage-workflow.md)
