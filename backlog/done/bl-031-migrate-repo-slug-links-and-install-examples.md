**Completed:** 2026-02-11

# BL-031: Migrate Repo Slug Links and Install Examples

**Phase:** Now

## 1. Outcome
All active documentation references to the old repository slug are updated to the new slug, including install commands and degit examples, so copy-paste paths work after renaming.

## 2. Constraints & References
- Keep search-and-replace scoped to active docs; preserve intentional historical mentions in archived/done records unless they are user-facing setup docs.
- Validate both relative links and full GitHub URLs.
- Include install and degit command examples used by readers.

**References:** `implementations/README.md`, `README.md`, `implementations/cursor/README.md`, `backlog/done/bl-024-add-install-implementation-script.md`.

## 3. Acceptance Checks
- [x] All user-facing setup docs no longer use `cursorrules` in clone/degit/path examples.
- [x] Any full GitHub URL references in active docs use the new owner/repo path where applicable.
- [x] `rg -n "cursorrules|WE3io/cursorrules"` over active docs returns no unintended hits.
- [x] Installation examples remain syntactically valid and consistent across docs.

## 4. Explicit Non-Goals
- Changing external repository names not owned by this project.
- Rewriting historical decision records solely for terminology.
- Adding new installation mechanisms.
