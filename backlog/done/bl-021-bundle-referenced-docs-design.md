**Completed:** 2026-02-11 — Design approved; manifest created; sync strategy documented.

# BL-021: Bundle Referenced Docs — Design

**Phase:** Later

## 1. Outcome
Design and manifest for bundling AI Blindspots articles into implementation folders so stand-alone installs have working links. Approve bundled-docs structure, sync strategy, and manifest format.

## 2. Constraints & References
- Implementations are copied into projects; relative paths to `ai-blindspots/` break.
- Bundled content must stay in sync with canonical source (ai-blindspots/articles/).
- Minimal footprint: only articles directly referenced in rule files.

**References:** [2026-02-11-bundled-docs-exploration.md](../decisions/2026-02-11-bundled-docs-exploration.md), BL-012 (release workflow), [implementations/](../../implementations/).

## 3. Acceptance Checks
- [x] Bundled docs structure approved (folder per implementation, e.g. `docs/articles/`).
- [x] Manifest of source → destination pairs for sync documented or in JSON.
- [x] Decision on sync mechanism (manual, script, or release step).
- [x] Rule file path update pattern documented (e.g. `../docs/articles/...`).
- [x] Explicit scope: which articles bundled (prompt-injection, debugging-blindspot, context-pollution).

## 4. Design Appendix

**Structure:** `implementations/<tool>/docs/articles/{security,debugging,context-management}/` per [2026-02-11-bundled-docs-exploration.md](../decisions/2026-02-11-bundled-docs-exploration.md).

**Manifest:** [backlog/manifests/bundled-docs-mapping.json](../manifests/bundled-docs-mapping.json) — source → destinations for each article.

**Sync mechanism:** `scripts/sync-bundled-docs.py` (BL-023) copies articles from ai-blindspots/ into implementation docs folders. Run before release or when ai-blindspots articles change.

**Path pattern:** From `.claude/rules/` or `.agent/rules/` → `../docs/articles/...`; from `.cursor/rules/always/` → `../../../docs/articles/...`.

## 5. Explicit Non-Goals
- Implementing the bundle (BL-022).
- Bundling QUICK_REFERENCE, ai-coding-assistant-rules, or TOOL_TRANSLATION_GUIDE.
- Changing Cursor template repo (WE3io) links.
