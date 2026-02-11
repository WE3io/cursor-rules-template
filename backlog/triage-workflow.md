# Triage Gate Workflow

Weekly 15-minute triage of research intake. Go/no-go decisioning with clear ownership.

## Cadence

- **Frequency:** Weekly
- **Duration:** 15 minutes (timebox)
- **Day/time:** TBD by owner

## Owner

Assigned triage owner: TBD

_Update when owner is assigned._

## Triage Checklist

For each intake in the queue:

1. [ ] **Clarity** — Intent clear? (from [change-acceptance-criteria](templates/change-acceptance-criteria.md))
2. [ ] **Actionability** — Can we act on it?
3. [ ] **Fit** — Does it belong in canonical collection?
4. [ ] **Priority** — Now / Next / Later / Reject
5. [ ] **Decision** — Record in [decision-record](templates/decision-record.md) format

## Input

- [Research intake template](templates/research-intake.md) — Use for new candidates
- Intake queue: `backlog/intake/`

## Output

- Decision record per candidate (accept / reject / defer)
- Accepted → Add to change manifest when released
- Rejected → Record rationale; no canonical change

## Triage Cycle Log

| Date | Intakes | Decisions |
|------|---------|-----------|
| 2026-02-11 | sample-intake-001 | Reject (template validation only) |
| 2026-02-11 | pilot-context-restart-threshold | Accept (BL-014 pilot cycle) |
