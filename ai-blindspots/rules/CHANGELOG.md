# Rules Changelog

## v2.0 (February 2026)

### Added

**Security & Safety (New Principle 5)**
- Treat external content as untrusted
- Implement permission boundaries
- Review generated code for security
- Common security blindspots

**Security Practices (New Guideline 7)**
- Input validation patterns
- Credential handling
- Context separation
- Security review checklist

**Decision Trees**
- When to restart session
- Debugging workflow
- File size management

**Domain-Specific Guidance**
- Web Development (Frontend)
- Backend Services
- Data Engineering

**Common Failure Patterns**
- The Endless Dig
- Symptom Whack-a-Mole
- Context Pollution Spiral
- Overconfident Hallucination
- Security Blind Implementation
- Premature Optimization
- Scope Creep

**Quick Reference**
- Action matrix for common problems
- Critical boundaries summary
- Confidence calibration guide

### Enhanced

**Principle 1: Problem-Solving**
- Context pollution awareness (~20-30 message limit)
- Specific "stop digging" trigger (3 failed attempts)
- Root cause vs. symptom distinction

**Principle 2: Context Management**
- File size limits (<64KB)
- Context pollution management
- Stateless operation patterns

**Principle 4: Communication**
- Communicate uncertainty/confidence
- Checkpoint progress regularly
- Explicit confidence levels

**Guideline 4: Debugging** (significantly enhanced)
- Scientific debugging method (5-step process)
- Require reproduction
- Instrumentation before changes
- Avoid shotgun debugging

**Guideline 5: Refactoring**
- Preparatory refactoring workflow
- Evaluate fundamental vs. tactical

### Improved

**Organization**
- De-duplicated repeated guidance (~15 instances)
- Added cross-references between sections
- Better structure: Quick Ref → Principles → Guidelines → Domains → Trees → Patterns

**Content**
- Updated for 2026 AI capabilities
- Current model references
- Modern tool examples
- 50+ examples (vs. 20 in v1.0)

### Removed

- Repeated sections (consolidated)
- Outdated model claims
- Vague guidance without specifics

---

## v1.0 (March 2025)

Initial release from Edward Z. Yang's AI Blindspots blog.

**Core Principles:** 5
**Implementation Guidelines:** 6
**Content:** 218 lines, 20 blindspot insights synthesized

---

## Migration: v1.0 → v2.0

**No breaking changes.** v2.0 is additive.

**Minimal upgrade:**
Add Security section (critical).

**Full upgrade:**
Replace with v2.0 entirely.

**Custom rules:**
Keep your customizations, merge v2.0 additions:
```markdown
## From AI Blindspots v2.0
[New sections]

## Our Custom Rules
[Your additions]

## Overrides
[Where you differ]
```
