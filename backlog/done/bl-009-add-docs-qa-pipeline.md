# BL-009: Add Docs QA Pipeline

**Phase:** Next  
**Completed:** 2026-02-11 — Added `.github/workflows/docs-qa.yml` (markdown lint, link check, required-section check). `.markdownlint.json` and `scripts/check-required-sections.sh` added.

## 1. Outcome
Automated markdown lint, link checks, and required-section checks. Pipeline runs on PRs and blocks on failures.

## 2. Constraints & References
- Scope: `ai-blindspots/`, `implementations/`, root docs.
- Must run in CI (e.g. GitHub Actions).
- Non-blocking checks may be separate from blocking checks.

**References:** None.

## 3. Acceptance Checks
- [x] Markdown lint runs (e.g. markdownlint, mdl).
- [x] Link checks run (internal and optionally external).
- [x] Required-section checks run (if defined).
- [x] Pipeline runs on PRs.
- [x] Pipeline blocks merge on failures.

## 4. Explicit Non-Goals
- Parity check pipeline (BL-010).
- Staleness tracking (BL-011).
- Content quality review (human).
