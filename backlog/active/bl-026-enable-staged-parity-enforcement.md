# BL-026: Enable Staged Parity Enforcement

**Phase:** Active (Untriaged)

## 1. Outcome
Parity check supports staged enforcement so selected tools/statuses fail CI while others remain warnings, enabling gradual tightening without blocking all translation work at once.

## 2. Constraints & References
- Reuse existing parity configuration model in `ai-blindspots/canonical-tool-mapping.json`.
- Any new policy fields must be documented in code comments or README-level docs where parity behavior is described.
- Enforcement behavior must be deterministic and visible in report output.

**References:** `scripts/parity-check.py`, `ai-blindspots/canonical-tool-mapping.json`, `.github/workflows/parity-check.yml`, `backlog/done/bl-010-add-parity-check-pipeline.md`.

## 3. Acceptance Checks
- [ ] Config supports staged policy (for example, fail-on-gap per tool and optional fail-on-partial per tool).
- [ ] Script exit code reflects configured staged policy.
- [ ] Report output clearly shows which findings are warnings vs failures under current config.
- [ ] Default config in repo is set to a documented initial stage (not all-or-nothing).
- [ ] CI parity workflow remains green when repository state matches chosen stage policy.

## 4. Explicit Non-Goals
- Writing or translating missing guidance content.
- Changing docs QA or staleness workflows.
- Defining long-term roadmap for future enforcement stages.
