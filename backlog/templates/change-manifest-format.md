# Change Manifest Format

Standard delta artifact per release. Records what changed in the canonical AI Blindspots collection.

## Format

```yaml
# Change Manifest
version: YYYY-MM-DD or semver
date: YYYY-MM-DD

added:
  - id: guidance-id
    title: Human-readable title
    location: path/to/file.md
    rationale: Brief reason for addition

changed:
  - id: guidance-id
    title: Human-readable title
    location: path/to/file.md
    summary: What changed
    rationale: Why

removed:
  - id: guidance-id
    title: Human-readable title
    rationale: Why removed

deprecated:
  - id: guidance-id
    title: Human-readable title
    location: path/to/file.md
    replacement: id or path of replacement
    rationale: Why deprecated
```

## Fields

- **id** — Aligns with canonical guidance schema (BL-001)
- **title** — Human-readable; helps downstream tool mappers
- **location** — Path within ai-blindspots/
- **rationale** — Required for audit
- **summary** (changed) — Concise description of delta
- **replacement** (deprecated) — Where to find the new guidance

## Usage

1. Create manifest when releasing canonical changes
2. Feeds BL-007 (mapping matrix), BL-008 (translation checklists), BL-010 (parity check)
3. Supports audit and release notes

## Related

- [Canonical guidance schema](canonical-guidance-schema.md)
