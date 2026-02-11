# KPI Dashboard Spec

Effectiveness metrics for the AI Blindspots operational process. Definitions and cadence. Spec only; implementation (dashboard build, automation) is out of scope.

**References:** BL-006 (Change Manifest), BL-010 (Parity Check), BL-012 (Release Workflow).

---

## 1. time-to-update

**Definition:** Elapsed time from intake creation to release containing that change.

**Measurement:**
- **Start:** Intake file creation date (from `backlog/intake/` file mtime or git history; low-friction: use file date or add optional `created` field to intake template)
- **End:** Manifest date for the release that includes the change (from `backlog/manifests/` filename or manifest `date` field)
- **Unit:** Days

**Calculation:** For each accepted intake, find the manifest that lists it in `added` or `changed`; compute days between intake creation and manifest date.

**Cadence:** Compute per release; report as median time-to-update for changes in that release. Optional: monthly aggregate.

---

## 2. translation parity %

**Definition:** Percentage of canonical principles that are implemented (ok or partial) in each tool.

**Measurement:**
- **Source:** BL-010 parity report (`scripts/parity-check.py`, `parity-report.json`)
- **Formula:** For each tool: `(principles with status ok or partial) / (total principles) × 100`
- **Unit:** Percentage (0–100)

**Calculation:** From `parity-report.json`: `gaps_by_tool[tool]` = list of principles with gap. Parity % = `(total - len(gaps)) / total × 100`.

**Cadence:** Run parity check per release; report per tool. Optional: trend over releases.

---

## 3. post-release defects

**Definition:** Rollbacks, hotfixes, or emergency patches applied after a release.

**Measurement:**
- **Rollback:** Release reverted or superseded by immediate follow-up release
- **Hotfix:** Emergency patch (per [release-workflow](release-workflow.md) protocol) within N days of prior release
- **Unit:** Count per release or per period

**Calculation:** Manual or low-friction: count manifests with "Emergency patch" in rationale within 7 days of previous release; or count releases that are superseded by a corrective release.

**Cadence:** Per release; monthly aggregate of post-release defect count.

---

## Cadence Summary

| Metric | When to compute | Report level |
|--------|-----------------|--------------|
| time-to-update | Per release | Median days for changes in release |
| translation parity % | Per release (parity check) | Per tool |
| post-release defects | Per release; monthly | Count |

---

## Data Sources

| Metric | Primary source |
|--------|----------------|
| time-to-update | `backlog/intake/`, `backlog/manifests/`, git log |
| translation parity % | `parity-report.json`, `scripts/parity-check.py` |
| post-release defects | `backlog/manifests/` (rationale text, dates) |

---

## Status

Spec complete. **Awaiting maintainer review and approval.**
