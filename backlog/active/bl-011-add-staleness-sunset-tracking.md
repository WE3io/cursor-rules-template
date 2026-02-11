# BL-011: Add Staleness/Sunset Tracking

**Phase:** Next

## 1. Outcome
Alerts for overdue review dates on guidance items. Stale-item report includes owner and due date.

## 2. Constraints & References
- Depends on BL-001 schema (`review_date`, `owner`).
- Guidance items live in `ai-blindspots/` (rules, articles).
- Threshold for "stale" must be defined (e.g. past review_date).

**References:** BL-001.

## 3. Acceptance Checks
- [ ] Stale-item report generated.
- [ ] Report includes owner and due date for each stale item.
- [ ] Report surfaced (e.g. CI, weekly digest, or manual run).
- [ ] Threshold for staleness documented.

## 4. Explicit Non-Goals
- Migrating content to schema (BL-001 prerequisite).
- Automating review process.
- Sunset/decommission workflow.
