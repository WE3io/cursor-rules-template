**Completed:** 2026-02-11

# BL-030: Rebrand Repository Identity and Core Docs

**Phase:** Now

## 1. Outcome
Repository identity is updated from a Cursor-centric brand to a tool-agnostic name across core project docs, so project purpose is accurately communicated as multi-tool AI assistant guidance.

## 2. Constraints & References
- Preserve existing repository structure and technical behavior; this is a naming/positioning update only.
- Keep source attribution to external projects where historically relevant.
- Update only docs that define project identity (not historical records).

**References:** `README.md`, `implementations/README.md`, `ai-blindspots/README.md`, `backlog/active/README.md`, `implementations/cursor/README.md`.

## 3. Acceptance Checks
- [x] Root `README.md` title and intro use the new repository identity.
- [x] Core layout and "Where to Start" sections remain accurate after renaming.
- [x] `implementations/README.md` no longer frames the monorepo as `cursorrules` specifically.
- [x] Tool-specific docs are positioned as implementations under the new project identity.
- [x] No broken relative links introduced in updated core docs.

## 4. Explicit Non-Goals
- Changing implementation rule content semantics.
- Modifying historical completed backlog records for archival consistency.
- Enforcing SEO/metadata updates outside repository files.
