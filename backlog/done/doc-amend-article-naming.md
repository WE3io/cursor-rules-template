**Completed:** 2026-02-11 — topic-noun.md convention in articles/README.md; use-static-types.md renamed to static-types.md; links updated.

# Standardize Article Filename Naming Convention

**Phase:** Now

## 1. Outcome
Article filenames in `ai-blindspots/articles/` follow a documented convention. Existing articles are renamed to match it; all references are updated; no broken links.

## 2. Constraints & References
- Current articles: `context-pollution.md`, `overconfidence.md`, `prompt-injection.md`, `debugging-blindspot.md`, `memento.md`, `use-static-types.md`.
- Proposed convention: `topic-noun.md` (e.g. `context-pollution`, `prompt-injection`).
- Category READMEs, `articles/README.md`, and cross-links must be updated.

**References:** None.

## 3. Acceptance Checks
- [x] Naming convention documented (e.g. in `articles/README.md` or a style guide).
- [x] All 6 article files comply with the convention (rename if needed).
- [x] All internal links to articles updated (category READMEs, parent README, cross-references).
- [x] Root README and "Where to Start" links still work.
- [x] No broken links verified (manual or automated).

## 4. Explicit Non-Goals
- Changing article content or structure.
- Changing naming of non-article docs (e.g. `QUICK_REFERENCE.md`, `TOOL_TRANSLATION_GUIDE.md`).
- Renaming rule files (`.mdc`) or implementation docs.
