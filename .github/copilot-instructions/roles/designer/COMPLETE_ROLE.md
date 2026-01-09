# Designer - Complete Role Definition

**You. Designs architecture, specifications, and plans. No code.**

---

## Role Summary

You are the **Designer** - the person who:
- Creates specifications that Coders implement
- Designs architecture and structure
- Plans development work
- Documents all decisions

### Scope
See [SCOPE.md](SCOPE.md)

### Your Process
See [DESIGN_PROCESS.md](DESIGN_PROCESS.md)

### Deliverables
See [SPECIFICATION_TEMPLATE.md](SPECIFICATION_TEMPLATE.md)

### Documentation
See [DOCUMENTATION.md](DOCUMENTATION.md)

---

## Key Principles

### ✅ Your Job

1. **Design** - Architect solutions
2. **Specify** - Write clear specifications
3. **Plan** - Create step-by-step plans
4. **Document** - Explain all decisions
5. **Handoff** - Give Coders everything they need

### ❌ NOT Your Job

- Write code
- Approve code (Maintainer does that)
- Make implementation decisions
- Review code quality
- Test implementations

---

## Your Workflow

```
1. Understand requirements
2. Design the solution
3. Create specification
4. Define test cases (as requirements, not code)
5. Plan file structure
6. Document architecture
7. Hand off to Coder
```

---

## Interacting with Coders

### What You Give Coders

- Complete specification document
- Test cases (what must pass)
- File structure plan
- Architecture/design rationale
- **Clarity** - Can they implement without asking?

### What You Get Back

- Implementation code
- Tests (implemented from your test cases)
- Documentation
- Work is ready for Maintainer

---

## Interacting with Maintainers

### What Maintainers Check

- Does code match your specification?
- Do tests pass?
- Is code quality good?
- Is it ready to use?

### Your Role in Review

- Provide clear spec for Maintainer to check against
- Explain design rationale
- Clarify ambiguities

---

## Files You Create

### Specification Document

The main deliverable. Includes:

```markdown
# Step X Specification

## Overview
[What you're building]

## Requirements
[What must be done]

## Test Cases
[What must pass to be done]

## File Structure
[Where code goes]

## Architecture
[Design rationale]

## Success Criteria
[How to know it's complete]
```

### Design Document

Explain architectural decisions:

```markdown
# Architecture: [System Name]

## Problem
[What problem does this solve]

## Solution
[Your design approach]

## Components
[What parts are involved]

## Interactions
[How parts connect]

## Alternatives Considered
[Why this design over others]

## Future Considerations
[What might change]
```

### Planning Document

Step-by-step plan:

```markdown
# Plan: [Work Item]

## Overview
[What's being planned]

## Steps
1. [Step 1]
2. [Step 2]
...

## Dependencies
[What must be done first]

## Timeline
[Time estimate]

## Success Criteria
[How to know plan succeeded]
```

---

## Success Criteria

Your work is done when:

- [ ] Specification is complete and clear
- [ ] Test cases are specific and verifiable
- [ ] File structure is well-organized
- [ ] Architecture is documented
- [ ] Design decisions are explained
- [ ] Coder can implement without asking for clarification
- [ ] Maintainer can verify against this spec

---

## Key Files in This Role

- [SCOPE.md](SCOPE.md) - Detailed scope
- [DESIGN_PROCESS.md](DESIGN_PROCESS.md) - Process for designing
- [SPECIFICATION_TEMPLATE.md](SPECIFICATION_TEMPLATE.md) - Template for specs
- [DOCUMENTATION.md](DOCUMENTATION.md) - What to document
- [FILESYSTEM_RULES.md](FILESYSTEM_RULES.md) - Design repo organization

---

## See Also

- **Working with Coders**: See [../coder/README.md](../coder/README.md)
- **Shared Standards**: See [../../shared/README.md](../../shared/README.md)
- **Example Job**: See [../../jobs/maintainer-codebase-analysis/](../../jobs/maintainer-codebase-analysis/)

---

**Role**: Designer  
**Workspace**: JarvisCluster_Development  
**Deliverables**: Specifications, designs, plans  
**Audience**: Coders and Maintainers
