**Completed:** 2026-02-11 — Bundled docs added; links updated; READMEs documented.

# BL-022: Add Bundled Docs to Implementations

**Phase:** Later

## 1. Outcome
Each implementation that references ai-blindspots articles now includes a bundled `docs/articles/` copy with those articles. Rule file links use local paths instead of monorepo-relative paths. Stand-alone installs have working links.

## 2. Constraints & References
- Follows design from BL-021.
- Copy (do not symlink) articles from ai-blindspots/ into each implementation.
- Update rule file links to use local paths (e.g. `../docs/articles/security/prompt-injection.md`).

**References:** BL-021, [2026-02-11-bundled-docs-exploration.md](../decisions/2026-02-11-bundled-docs-exploration.md), [ai-blindspots/articles/](../../ai-blindspots/articles/).

## 3. Acceptance Checks
- [x] `implementations/claude/docs/articles/` contains prompt-injection.md, debugging-blindspot.md.
- [x] `implementations/gemini/docs/articles/` contains prompt-injection.md, debugging-blindspot.md.
- [x] `implementations/antigravity/docs/articles/` contains prompt-injection.md, debugging-blindspot.md.
- [x] `implementations/cursor/docs/articles/` contains context-pollution.md.
- [x] Claude, Gemini, Antigravity security.md and debugging.md link to `../docs/articles/...`.
- [x] Cursor workflows.mdc links to `../../../docs/articles/context-management/context-pollution.md`.
- [x] README in each implementation documents bundled docs and source.
- [x] Codex unchanged (AGENTS.md has no inline article refs).

## 4. Explicit Non-Goals
- Sync script (BL-023).
- Bundling additional articles beyond the three referenced.
- Modifying article content.
