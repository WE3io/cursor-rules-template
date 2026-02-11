# BL-027: Expand Backlog Section QA Coverage

**Phase:** Active (Untriaged)

## 1. Outcome
Backlog required-section QA validates both active and completed work-item files, so checks remain meaningful even when `backlog/active/` is empty.

## 2. Constraints & References
- Maintain current required section conventions used by backlog work items.
- Exclude non-work-item files (such as README files) from validation.
- Keep implementation in shell script and compatible with CI usage.

**References:** `scripts/check-required-sections.sh`, `.github/workflows/docs-qa.yml`, `backlog/README.md`, `backlog/active/README.md`, `backlog/done/`.

## 3. Acceptance Checks
- [ ] `scripts/check-required-sections.sh` validates `backlog/active/*.md` and `backlog/done/*.md` (excluding `README.md`).
- [ ] Script checks for required numbered sections: Outcome, Constraints & References, Acceptance Checks, Explicit Non-Goals.
- [ ] Script checks done items for a `**Completed:** YYYY-MM-DD` marker.
- [ ] Script exits non-zero when any scoped file fails checks.
- [ ] Docs QA workflow continues to execute script without additional dependencies.

## 4. Explicit Non-Goals
- Validating semantic quality of item content.
- Enforcing phase naming conventions.
- Modifying triage or release workflows.
