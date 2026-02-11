# Staleness Manifest

**Purpose:** Track review dates for guidance items in `ai-blindspots/`.

**Threshold:** Stale = `review_date` has passed (YYYY-MM-DD).

**Format:** [staleness-manifest.json](staleness-manifest.json)

**Report:** Run `./scripts/staleness-report.py` (manual) or see CI (Docs QA / Staleness Check workflow).

## Adding Items

Add entries to `staleness-manifest.json`:

```json
{
  "id": "example-id",
  "title": "Human-readable title",
  "location": "ai-blindspots/path/to/file.md",
  "owner": "maintainer",
  "review_date": "2026-12-01"
}
```

## Related

- BL-001 canonical guidance schema (`review_date`, `owner`)
- [scripts/staleness-report.py](../scripts/staleness-report.py)
