# Bundled Docs Exploration — Detail

**Date:** 2026-02-11  
**Context:** Implementations reference ai-blindspots/ articles via relative paths that break when copied standalone.  
**Option explored:** Bundle referenced docs inside each implementation folder.

---

## 1. Inventory of Referenced Files

### Articles referenced in rule files

| Source (ai-blindspots) | Referenced by | Path from rule file |
|------------------------|---------------|---------------------|
| `articles/security/prompt-injection.md` | Claude, Gemini, Antigravity `security.md` | `../../../../ai-blindspots/articles/security/prompt-injection.md` |
| `articles/debugging/debugging-blindspot.md` | Claude, Gemini, Antigravity `debugging.md` | `../../../../ai-blindspots/articles/debugging/debugging-blindspot.md` |
| `articles/context-management/context-pollution.md` | Cursor `workflows.mdc` | `../../../../ai-blindspots/articles/context-management/context-pollution.md` |

### Other references (README, optional)

| Source | Referenced by | Purpose |
|--------|---------------|---------|
| `ai-blindspots/` (root) | All READMEs | Canonical source link |
| `TOOL_TRANSLATION_GUIDE.md` | All READMEs | Translation approach |
| `QUICK_REFERENCE.md` | Cursor rules README | Optional canonical ref |
| `rules/ai-coding-assistant-rules.md` | Cursor rules README | Optional canonical ref |

**Scope for bundling:** Focus on articles that rule files link to directly. README links to "canonical source" can remain as external URLs (ezyang.github.io or repo URL) for standalone; bundling full ai-blindspots would be excessive.

---

## 2. Proposed Bundle Structure

### Per-implementation folder

```
implementations/<tool>/
├── .claude/rules/   (or .agent/rules/, etc.)
├── docs/            # or references/
│   └── articles/
│       ├── security/
│       │   └── prompt-injection.md
│       ├── debugging/
│       │   └── debugging-blindspot.md
│       └── context-management/
│           └── context-pollution.md
└── README.md
```

**Path from rule file to bundled doc:**
- From `.claude/rules/security.md` → `../docs/articles/security/prompt-injection.md`
- From `.agent/rules/debugging.md` → `../docs/articles/debugging/debugging-blindspot.md`

### Tool-specific needs

| Tool | Articles to bundle | Notes |
|------|-------------------|-------|
| Claude | prompt-injection, debugging-blindspot | security.md, debugging.md |
| Gemini | prompt-injection, debugging-blindspot | Same |
| Antigravity | prompt-injection, debugging-blindspot | Same |
| Codex | None | AGENTS.md has no inline article refs |
| Cursor | context-pollution | workflows.mdc; Cursor already has docs/ |

### Cursor special case

Cursor has `implementations/cursor/docs/` with `aca_usage_guide.md` and `cursor_rules_best_practices.md`. Add:
- `docs/articles/context-management/context-pollution.md`

Path from `workflows.mdc` (in `.cursor/rules/always/`): `../../../docs/articles/context-management/context-pollution.md`

---

## 3. Sync Strategy

**Problem:** Bundled copies will drift from ai-blindspots/ when articles are updated.

**Options:**

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| A. Manual copy | Document in release workflow: "When updating articles, copy to implementations/*/docs/" | Simple | Error-prone, easy to forget |
| B. Copy script | `scripts/sync-bundled-docs.py` copies specified articles to each implementation | Reproducible | Script to maintain |
| C. Symlinks (monorepo) | Use symlinks in implementations; document that standalone install must copy | No duplication in repo | Symlinks don't travel in zip/template; git submodule complexity |
| D. Generator | LLM generator or build step emits implementations with bundled content | Single source | More complex pipeline |

**Recommendation:** Option B — Copy script. Run as part of release or when articles change. Script reads a manifest of (source, dest) pairs.

---

## 4. Manifest Format

```json
{
  "bundled_articles": [
    {
      "source": "ai-blindspots/articles/security/prompt-injection.md",
      "destinations": [
        "implementations/claude/docs/articles/security/prompt-injection.md",
        "implementations/gemini/docs/articles/security/prompt-injection.md",
        "implementations/antigravity/docs/articles/security/prompt-injection.md"
      ]
    },
    {
      "source": "ai-blindspots/articles/debugging/debugging-blindspot.md",
      "destinations": ["..."]
    },
    {
      "source": "ai-blindspots/articles/context-management/context-pollution.md",
      "destinations": ["implementations/cursor/docs/articles/context-management/context-pollution.md"]
    }
  ]
}
```

---

## 5. Rule File Updates

After bundling, update each rule file to use local path:

**Before (security.md):**
```markdown
See: AI Blindspots — [Prompt Injection](../../../../ai-blindspots/articles/security/prompt-injection.md)
```

**After (standalone-safe):**
```markdown
See: AI Blindspots — [Prompt Injection](../docs/articles/security/prompt-injection.md)
```

**Dual-path consideration:** Could support both monorepo and standalone:
```markdown
See: AI Blindspots — [Prompt Injection](../docs/articles/security/prompt-injection.md)
```
This works in both: when folder is copied, docs/ travels with it. In monorepo, the bundled copy is the same content (synced from ai-blindspots).

---

## 6. README Updates

Each implementation README should document:
- `docs/articles/` contains bundled AI Blindspots articles for offline/standalone use
- Source: `ai-blindspots/` in this repo; sync via `scripts/sync-bundled-docs.py`
- For latest, see upstream: https://ezyang.github.io/ai-blindspots/

---

## 7. Dependencies

- BL-020 (Antigravity) complete
- No schema changes
- Release workflow (BL-012) may need step: "Run sync-bundled-docs before release"

---

## 8. Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Bundled copies drift from canonical | Sync script in release checklist; parity-check or staleness check for docs |
| Duplication increases repo size | 3 articles × ~50KB each ≈ 150KB; acceptable |
| Merge conflicts when syncing | Script overwrites; canonical is source of truth |
| User edits bundled copy | README: "Do not edit; overwritten by sync" |

---

## 9. Out of Scope

- Bundling QUICK_REFERENCE, ai-coding-assistant-rules, TOOL_TRANSLATION_GUIDE (large; optional for users)
- Changing Cursor template repo (WE3io/Cursor-Rules-Template) references
- Git submodules or external package approach
