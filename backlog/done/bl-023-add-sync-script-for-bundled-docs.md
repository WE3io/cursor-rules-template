**Completed:** 2026-02-11 — Sync script added; release workflow updated.

# BL-023: Add Sync Script for Bundled Docs

**Phase:** Later

## 1. Outcome
Script or runbook that copies ai-blindspots articles into implementation `docs/articles/` folders. Ensures bundled copies stay in sync with canonical source when articles change.

## 2. Constraints & References
- Depends on BL-022 (bundled docs structure exists).
- Script idempotent; overwrites destination files.
- Manifest or hardcoded mapping defines source → destination pairs.

**References:** BL-021, BL-022, [2026-02-11-bundled-docs-exploration.md](../decisions/2026-02-11-bundled-docs-exploration.md), [scripts/](../../scripts/).

## 3. Acceptance Checks
- [x] Script exists (e.g. `scripts/sync-bundled-docs.py` or `.sh`).
- [x] Script copies prompt-injection.md, debugging-blindspot.md, context-pollution.md to correct implementation paths.
- [x] Script runnable from repo root; no external deps beyond Python stdlib or shell.
- [x] Release workflow or README documents when to run (e.g. before release, when articles change).
- [x] Optional: manifest JSON (e.g. `backlog/manifests/bundled-docs-mapping.json`) drives copy logic.

## 4. Explicit Non-Goals
- Auto-run on CI (manual/scheduled only).
- Validating content parity (e.g. diff check).
- Syncing to external repos (Cursor template).
