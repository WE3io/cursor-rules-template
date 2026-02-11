**Completed:** 2026-02-11

# BL-034: Update Repository URL References After Rename

**Phase:** Now

## 1. Outcome
All active, user-facing repository references are updated to the renamed repository URL `git@github.com:WE3io/ai-assistant-rules.git` (or corresponding HTTPS URL where appropriate), so setup instructions and links resolve correctly.

## 2. Constraints & References
- Scope to active docs/configs used by contributors and consumers; avoid rewriting historical archive content unless it is still presented as current setup guidance.
- Preserve protocol intent:
  - SSH examples use `git@github.com:WE3io/ai-assistant-rules.git`
  - Browser links use `https://github.com/WE3io/ai-assistant-rules`
- Keep changes minimal and link-safe.

**References:** `README.md`, `implementations/README.md`, `implementations/cursor/README.md`, `backlog/active/`, `backlog/done/bl-024-add-install-implementation-script.md`.

## 3. Acceptance Checks
- [x] Active setup instructions no longer reference old repository slug/path.
- [x] SSH clone/remote examples use `git@github.com:WE3io/ai-assistant-rules.git`.
- [x] HTTPS repository links in active docs resolve to `https://github.com/WE3io/ai-assistant-rules`.
- [x] `rg -n "cursorrules|WE3io/cursorrules"` over active docs/config returns no unintended hits.
- [x] Configured CI checks for this change passed; docs QA workflow is PR-only.

## 4. Explicit Non-Goals
- Changing repository content ownership or organization settings.
- Rewriting archival/historical text solely for naming consistency.
- Introducing new installation workflows beyond URL/path updates.
