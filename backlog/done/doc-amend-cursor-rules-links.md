**Completed:** 2026-02-11 — Monorepo vs Standalone instructions and GitHub URLs in rules README and review-checklist.

# Fix Cursor Rules README Links for Standalone Installs

**Phase:** Now

## 1. Outcome
The `implementations/cursor/.cursor/rules/README.md` works in both monorepo and standalone installs. Links to canonical ai-blindspots content either resolve or direct users to a stable source (e.g. GitHub URL). No broken `../../../../`-style paths when the folder is copied out.

## 2. Constraints & References
- Cursor template may be used in "rules-only mode" (copy `.cursor/rules/` only).
- Canonical rules live in `ai-blindspots/` when in monorepo.
- See `implementations/cursor/README.md` for installation modes.

**References:** None.

## 3. Acceptance Checks
- [x] In monorepo layout, links to ai-blindspots content resolve.
- [x] In standalone install (copying only `.cursor/rules/` or full `implementations/cursor/`), links either resolve or are replaced with working references (e.g. GitHub URLs or explicit "copy from" instructions).
- [x] README clearly indicates what works in monorepo vs standalone.
- [x] No `../../../../`-style paths that break when folder is copied out.

## 4. Explicit Non-Goals
- Changing monorepo directory structure.
- Adding documentation for other tools (Claude, Codex, etc.).
- Changing `.mdc` rule content.
