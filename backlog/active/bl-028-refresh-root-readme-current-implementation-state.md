# BL-028: Refresh Root README for Current Implementation State

**Phase:** Active (Untriaged)

## 1. Outcome
Root `README.md` accurately reflects the repository's current implementation coverage, installation guidance, and structure so first-time readers are not misled by stale project status text.

## 2. Constraints & References
- Preserve existing high-level README intent and navigation structure.
- Update only statements that are now stale or inconsistent with repository reality.
- Keep links valid and relative paths unchanged where possible.

**References:** `README.md`, `implementations/README.md`, `backlog/active/README.md`.

## 3. Acceptance Checks
- [ ] Root README no longer states non-Cursor implementations are "planned" where they are now available.
- [ ] Implementation list in root README aligns with `implementations/README.md`.
- [ ] Installation path in root README points to current recommended flow.
- [ ] Updated README passes markdown lint and link checks in docs QA.

## 4. Explicit Non-Goals
- Redesigning README information architecture.
- Rewriting implementation-specific READMEs.
- Updating content outside root README unless required for broken links.
