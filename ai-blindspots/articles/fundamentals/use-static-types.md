# Use Static Types

*Updated: February 2026*
*Original: March 2025*

## The Blindspot

LLMs significantly reduce the traditional trade-off between prototyping speed and long-term maintainability in language selection. They excel at handling type system boilerplate, making statically-typed languages more accessible without sacrificing rapid development.

## Why It Happens

The eternal debate between dynamic and static type systems concerns the trade-off between ease of prototyping and long-term maintainability. Statically-typed languages historically required more upfront work but provided better tooling and refactoring support. LLMs shift this calculation by:

- Automatically generating type annotations and boilerplate
- Handling mechanical refactoring across type changes
- Using type errors as feedback to identify affected files
- Converting between type representations efficiently

## Impact

**With LLM Assistance:**
- Type system overhead is dramatically reduced
- Refactoring becomes more reliable (type checker guides the LLM)
- Code quality improves without additional developer burden
- Large-scale changes are easier to execute correctly

**Without Proper Setup:**
- Token costs can be high for type-heavy languages
- Gradual type systems may not provide sufficient feedback
- LLM may not receive type error information to guide fixes

## Mitigation Strategies

### 1. Set Up Type-Aware Workflows
Configure your agent setup so the LLM receives type errors after making changes:
```bash
# Example: Run type checker after changes
mypy src/ --strict
# or
tsc --noEmit
```

This feedback loop helps the LLM understand what other files need updates during refactoring.

### 2. Choose Strong Type Systems When Possible

**Excellent for LLMs (as of 2026):**
- **TypeScript** - Well-supported, strict mode recommended
- **Rust** - Modern LLMs (Claude 4+, GPT-4+) show strong Rust capabilities
- **Go** - Simple type system, excellent LLM performance
- **Kotlin** - Good balance of power and LLM compatibility

**Workable with Configuration:**
- **Python + mypy** - Requires strict mode configuration
- **JavaScript + TypeScript** - Gradual adoption possible

### 3. Configure Strict Mode for Gradual Type Systems

For Python:
```toml
# pyproject.toml
[tool.mypy]
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

For TypeScript:
```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true
  }
}
```

### 4. Monitor Token Costs

Type-heavy code can consume more tokens. Be strategic:
- Use type inference where possible
- Let the LLM handle explicit annotations
- Monitor costs on large refactorings
- Consider batching changes

## Examples

### Example 1: Large-Scale Refactoring

**Scenario:** Changing a function signature across 50+ files

Without types:
```python
# Must manually track every usage
# Runtime errors likely
# Tests might miss edge cases
```

With types + LLM:
```typescript
// 1. LLM changes function signature
function processData(input: DataInput): Promise<Result>

// 2. Type checker identifies all affected call sites
// 3. LLM receives error list and fixes each location
// 4. Type checker verifies correctness
```

### Example 2: Rust Capabilities Evolution

**March 2025:** "LLMs are not as good at generating Rust as they are for Python/JavaScript"

**February 2026:** Modern LLMs (Claude Sonnet 4+, GPT-4o) demonstrate significantly improved Rust capabilities:
- Complex lifetime management
- Trait implementation
- Async/await patterns
- Error handling with Result types

The training corpus has expanded and model architectures have improved.

### Example 3: Python Type Migration

**Before (dynamic Python):**
```python
def process(data):
    # What type is data? What does it return?
    # LLM must guess or explore code
    return transform(data)
```

**After (typed Python):**
```python
def process(data: DataFrame) -> ProcessedResult:
    # Type checker guides LLM refactoring
    # Errors caught immediately
    return transform(data)
```

When refactoring `transform()`, the type checker tells the LLM exactly which files need updates.

## Related Principles

- **Stateless Tools** - Type checkers should be run independently
- **Read the Docs** - Check type system documentation for framework-specific patterns
- **Mise en Place** - Configure type checking before starting development

## Current State (2026)

**Training Corpus Bias:**
- Python and JavaScript still dominate training data
- TypeScript adoption growing rapidly
- Rust representation improving significantly
- Go well-represented in infrastructure code

**LLM Capabilities:**
- Excellent: TypeScript, Go, Java, Kotlin
- Very Good: Rust (major improvement from 2025), Python+types
- Good: C#, Swift, Scala
- Emerging: Zig, Nim, OCaml

**Recommendation:** Choose statically-typed languages when working with LLMs. The overhead is minimal, and the benefits for refactoring and code quality are substantial.
