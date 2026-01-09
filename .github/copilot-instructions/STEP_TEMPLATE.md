# Step Instruction Template

**Template and best practices for creating step-specific copilot-instructions.md files.**

---

## File Location

```
Copilot_Development_Instructions/Step_X/
└── .github/
    └── copilot-instructions.md  ← This file
```

## Instruction File Pattern

Instead of duplicating rules in every step, use the INCLUDE pattern:

```markdown
---
applyTo: "jarvis/**,tests/**"
---

# Step X: [Title] - Copilot Instructions

<!-- INCLUDE REUSABLE SECTIONS -->

<!-- Include shared rules and requirements -->
You may include shared sections like:
- FILESYSTEM_RULES.md
- TDD_REQUIREMENTS.md
- AGENT_WORKSPACE.md

<!-- STEP-SPECIFIC CONTENT ONLY -->

Then add step-specific content:
- What you're building
- Which files to create
- Which functions to implement
- Files in this folder
- Your task
```

---

## Full Template

```markdown
---
applyTo: "jarvis/**,tests/**"
---

# Step X: [Title] - Copilot Instructions

You are implementing **Step X of Jarvis v0.1**.

---

## Your Task

[1-2 sentences on what you're building]

Example:
> Build a **command-line interface** for Jarvis that accepts user input, echoes commands back, and exits gracefully.

---

## Requirements Summary

[Brief overview of requirements]

- Requirement 1
- Requirement 2
- Requirement 3

See [../step_X_specification.md](../step_X_specification.md) for complete details.

---

## What You'll Create

```
jarvis/
├── module1.py       ← NEW/MODIFIED
├── module2.py       ← NEW
└── ...

tests/
├── test_step_X.py   ← NEW: 40+ test cases
└── ...
```

---

## Files in This Folder

- **[../step_X_specification.md](../step_X_specification.md)** — Complete requirements + test specs
- **[../README.md](../README.md)** — Workflow guidance
- **[../DESIGN_REFERENCE/](../DESIGN_REFERENCE/)** — Architecture documentation
- **[Agent_Workspace/](Agent_Workspace/)** — YOUR notes and progress

---

## Test-Driven Development

1. **Write tests FIRST** (all 40+ test cases from specification)
2. Then write code to pass tests
3. Run: `pytest tests/test_step_X.py -v`
4. **All tests must pass** before submitting

See [.github/copilot-instructions/TDD_REQUIREMENTS.md](../../copilot-instructions/TDD_REQUIREMENTS.md) for full TDD rules.

---

## Filesystem Rules

- ✅ Create files in jarvis/ and tests/
- ✅ Follow exact file names from specification
- ❌ NO code files in Agent_Workspace/
- ❌ NO configuration files in step folder
- 🗑️ Agent_Workspace will be deleted when step completes

See [.github/copilot-instructions/FILESYSTEM_RULES.md](../../copilot-instructions/FILESYSTEM_RULES.md) for details.

---

## Agent Workspace

Use Agent_Workspace/README.md to track:
- Your progress and what you've done
- Design decisions and why
- Questions and blockers
- What you learned

See [.github/copilot-instructions/AGENT_WORKSPACE.md](../../copilot-instructions/AGENT_WORKSPACE.md) for guidelines.

---

## Implementation Details

### Functions to Implement

[List each function with signature and description]

Example:
```python
def process_input(user_input: str) -> str:
    """
    Process user input and return result.
    
    Args:
        user_input: String from user
        
    Returns:
        Result string or error message
    """
```

### Key Behaviors

[List 3-5 key behaviors this step should have]

### Design Patterns

[Any specific patterns or approaches to use]

### Integration Points

[How this step connects to previous/future steps]

---

## Success Criteria

- [x] All tests pass
- [x] Code matches specification exactly
- [x] 80%+ code coverage
- [x] Follows REQUIREMENTS.md standards
- [x] No skipped tests
- [x] Agent_Workspace documentation complete

---

## Common Issues

### Issue: Tests are failing
→ Review test requirement carefully, check specification for expected behavior

### Issue: Unclear what to implement
→ Re-read specification, check test cases, review DESIGN_REFERENCE/

### Issue: Need architecture clarification
→ Review [../../DESIGN_PLAN.md](../../DESIGN_PLAN.md) and [../../USE_CASES.md](../../USE_CASES.md)

---

## Next Step

[Brief note about what comes after this step]

---

[Links to related documentation]
```

---

## Key Principles

### ✅ DO

1. **Include reusable sections** - Don't duplicate rules
2. **Keep it concise** - 50-80 lines maximum
3. **Be specific** - Say exactly what to implement
4. **Reference specs** - Link to detailed requirements
5. **Use templates** - Follow this structure

### ❌ DON'T

1. **Duplicate full rules** - Include/reference instead
2. **Make it too long** - Put details in specification file
3. **Be vague** - Say exactly what's needed
4. **Create new sections** - Use existing shared sections
5. **Leave commented code** - Remove debug code

---

## INCLUDE Pattern

If you need to reference shared sections, use:

```markdown
[Link to the shared section]

See [.github/copilot-instructions/FILESYSTEM_RULES.md](../../copilot-instructions/FILESYSTEM_RULES.md) for filesystem organization requirements.

See [.github/copilot-instructions/TDD_REQUIREMENTS.md](../../copilot-instructions/TDD_REQUIREMENTS.md) for test-driven development requirements.

See [.github/copilot-instructions/AGENT_WORKSPACE.md](../../copilot-instructions/AGENT_WORKSPACE.md) for workspace organization.
```

---

## Example: Step 1 Using This Template

```markdown
---
applyTo: "jarvis/**,tests/**"
---

# Step 1: Basic CLI - Copilot Instructions

You are implementing **Step 1 of Jarvis v0.1**.

---

## Your Task

Build a **command-line interface** for Jarvis that:
- Accepts user input
- Echoes commands back
- Exits gracefully

Nothing fancy—just input/output.

---

## Test-Driven Development (MANDATORY)

1. **Write tests FIRST** (before any implementation)
2. All test cases are in [../step_1_specification.md](../step_1_specification.md)
3. Run: `pytest tests/test_step_1.py -v`
4. **All tests must pass** before proceeding

See [.github/copilot-instructions/TDD_REQUIREMENTS.md](../../copilot-instructions/TDD_REQUIREMENTS.md) for full TDD requirements.

---

## What You'll Create

```
jarvis/
└── cli.py          ← Basic CLI with command loop

tests/
└── test_step_1.py  ← Tests (40+ test cases from spec)
```

---

## Files in This Folder

- **[../step_1_specification.md](../step_1_specification.md)** — Complete requirements + test specs
- **[../README.md](../README.md)** — Workflow guidance
- **[../DESIGN_REFERENCE/](../DESIGN_REFERENCE/)** — Architecture documentation
- **[Agent_Workspace/](Agent_Workspace/)** — YOUR notes go here

---

## Filesystem Rules

See [.github/copilot-instructions/FILESYSTEM_RULES.md](../../copilot-instructions/FILESYSTEM_RULES.md) for:
- ✅ What's allowed
- ❌ What's not
- 📋 Folder structure

---

## Agent Workspace

Use [Agent_Workspace/README.md](Agent_Workspace/README.md) to track your progress. See [.github/copilot-instructions/AGENT_WORKSPACE.md](../../copilot-instructions/AGENT_WORKSPACE.md) for guidelines.

---

## Success Criteria

- [ ] All 40+ tests pass
- [ ] Code matches specification
- [ ] 80%+ code coverage
- [ ] Follows REQUIREMENTS.md standards

---

## Next Step

[Brief note about Step 2]
```

---

## Maintenance

### When Creating New Step Instructions

1. Copy this template
2. Fill in step-specific content (title, task, files)
3. Add links to shared sections
4. Add success criteria
5. Remove/update example sections

### When Updating Shared Rules

1. Update the shared section file
2. All steps automatically reference it
3. No need to update every step file

### When a Rule Changes

1. Update ONE shared section file
2. All steps that reference it get the change automatically
3. No duplication = no inconsistency

---

**This template ensures consistency across all steps.**  
**Use INCLUDE pattern to avoid duplication.**  
**Keep step instructions focused on step-specific details.**

**Last Updated**: January 9, 2026
