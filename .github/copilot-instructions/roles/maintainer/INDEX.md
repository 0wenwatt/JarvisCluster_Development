# Maintainer Snippets Index

**Reusable instruction pieces for Maintainer role.**

---

## Available Snippets

### SCOPE.md
**What a Maintainer does and doesn't do**
- Detailed boundaries and responsibilities
- Decision authority (approve/reject)
- Conflict of interest rules
- When to escalate issues
- Relationship to Designer and Coder

### CONFORMANCE_CHECKLIST.md
**Complete checklist of what to verify**
- Spec compliance checks
- File organization checks
- Code quality checks
- Test coverage checks
- Documentation checks
- Style compliance checks
- All in checklist format

### CODE_REVIEW.md
**How to conduct code review**
- Code style verification
- Readability assessment
- Documentation quality
- Module organization
- Function/class structure
- Common issues to look for
- How to give feedback

### TEST_VERIFICATION.md
**How to run and verify tests**
- Running full test suite
- Checking individual tests
- Code coverage verification
- Coverage report interpretation
- Test naming conventions
- Coverage requirements (80%+)
- How to identify gaps

### FILESYSTEM_CONFORMANCE.md
**How to verify file organization**
- File location checks
- Folder structure verification
- File naming conventions
- Temp file detection
- Debug code detection
- Clean workspace verification

### DOCUMENTATION_REVIEW.md
**How to review documentation**
- Docstring quality
- Code comment quality
- Module documentation
- README updates
- Clarity and completeness
- Technical accuracy

---

## Using Maintainer Snippets

When creating a complete Maintainer job instruction:

```
Base:
+ Designer's specification document
+ Coder's implementation (code)
+ maintainer/SCOPE.md (what Maintainer does)
+ maintainer/CONFORMANCE_CHECKLIST.md (what to check)
+ maintainer/CODE_REVIEW.md (how to review)
+ maintainer/TEST_VERIFICATION.md (how to test)
+ maintainer/FILESYSTEM_CONFORMANCE.md (check files)
+ maintainer/DOCUMENTATION_REVIEW.md (check docs)

= Complete Maintainer job instruction
```

---

## Template: Maintainer Job Instruction

```markdown
# Maintainer Job: Review Step X Implementation

## Your Task
Review Coder's implementation against Designer's specification.

## Specification
See: [Designer's step specification]

## Implementation
See: [Coder's code in Jarvis/ repo]

## Scope
See [.github/copilot-instructions/roles/maintainer/SCOPE.md](...)

## Verification Checklist
See [.github/copilot-instructions/roles/maintainer/CONFORMANCE_CHECKLIST.md](...)

## Code Review
See [.github/copilot-instructions/roles/maintainer/CODE_REVIEW.md](...)

## Test Verification
See [.github/copilot-instructions/roles/maintainer/TEST_VERIFICATION.md](...)

## File Organization
See [.github/copilot-instructions/roles/maintainer/FILESYSTEM_CONFORMANCE.md](...)

## Documentation Review
See [.github/copilot-instructions/roles/maintainer/DOCUMENTATION_REVIEW.md](...)

## Result
Approve ✓ or Request Changes with specific issues listed
```

---

**System**: Role-Based Maintainer Snippets  
**Purpose**: Reusable instruction pieces for Maintainer role
