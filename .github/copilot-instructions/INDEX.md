# Copilot Instruction Sections - Index

**Reusable sections for creating copilot instructions across design and production repositories.**

---

## Overview

Instead of duplicating rules in every `.github/copilot-instructions.md` file, we use **reusable sections**:

- ✅ **One source of truth** for each rule
- ✅ **Automatic updates** when rules change
- ✅ **Consistent enforcement** across all steps
- ✅ **Less maintenance** (change once, affects all)
- ✅ **Clear organization** of related rules

---

## Available Sections

### 1. FILESYSTEM_RULES.md

**Purpose**: How to organize files and folders across both repos

**Covers**:
- What files are allowed at each location
- Root directory rules
- Step folder structure
- Production repo organization
- Design repo organization
- File naming conventions
- Cleanup procedures
- How to avoid messy filesystem

**Location**: `.github/copilot-instructions/FILESYSTEM_RULES.md`

**Use When**: 
- Creating new step instructions
- Need filesystem organization guidelines
- Discussing where a file should go

**Size**: Comprehensive (~300 lines)

---

### 2. TDD_REQUIREMENTS.md

**Purpose**: Test-driven development workflow and standards

**Covers**:
- Write tests FIRST workflow
- Test structure and organization
- Test naming conventions
- Test execution checklist
- Code coverage expectations
- Common test patterns
- Specification document structure
- Success criteria for completion

**Location**: `.github/copilot-instructions/TDD_REQUIREMENTS.md`

**Use When**:
- Need TDD process guidelines
- Explaining how to write tests
- Defining test requirements for a step
- Checking if tests meet standards

**Size**: Comprehensive (~250 lines)

---

### 3. AGENT_WORKSPACE.md

**Purpose**: Rules for the temporary Agent_Workspace folder

**Covers**:
- What Agent_Workspace is and why
- Folder structure and files
- What's allowed/not allowed
- File purposes (README, TODO, DECISIONS)
- Best practices for progress notes
- What happens to your notes
- Common patterns for documentation
- Cleanup before finishing

**Location**: `.github/copilot-instructions/AGENT_WORKSPACE.md`

**Use When**:
- Explaining workspace rules
- Guiding agents on progress tracking
- Defining what goes in workspace
- Preparing for step completion

**Size**: Comprehensive (~250 lines)

---

### 4. STEP_TEMPLATE.md

**Purpose**: Template and pattern for creating step-specific instructions

**Covers**:
- How to structure step instructions
- INCLUDE pattern to avoid duplication
- Template with all sections
- Example usage from Step 1
- Key principles (DO/DON'T)
- How to use shared sections
- Maintenance guidelines
- When to create vs. update

**Location**: `.github/copilot-instructions/STEP_TEMPLATE.md`

**Use When**:
- Creating new step instructions
- Updating existing step instructions
- Explaining how to include shared rules
- Reviewing instruction quality

**Size**: Comprehensive (~250 lines)

---

## How to Use These Sections

### Pattern: Include in Instruction File

In any `.github/copilot-instructions.md`, reference shared sections:

```markdown
---
applyTo: "jarvis/**,tests/**"
---

# Step X: Title - Copilot Instructions

Your task: [specific to this step]

---

## Filesystem Organization

See [.github/copilot-instructions/FILESYSTEM_RULES.md](../../copilot-instructions/FILESYSTEM_RULES.md) for:
- File organization rules
- Folder structure
- What's allowed/not allowed

---

## Testing Requirements

See [.github/copilot-instructions/TDD_REQUIREMENTS.md](../../copilot-instructions/TDD_REQUIREMENTS.md) for:
- Test-driven development workflow
- Test structure
- Success criteria

---

## Workspace Organization

See [.github/copilot-instructions/AGENT_WORKSPACE.md](../../copilot-instructions/AGENT_WORKSPACE.md) for:
- How to use Agent_Workspace
- Progress documentation
- Cleanup procedures

---

# Step-Specific Content

[Only include what's unique to this step]
- What files to create
- Which functions to implement
- Specific requirements
```

### Benefits of This Pattern

| Benefit | Impact |
|---------|--------|
| **No duplication** | Rules live in one place |
| **Automatic updates** | Change rule once, all steps updated |
| **Consistency** | All steps follow same rules |
| **Easier maintenance** | Less files to update |
| **Clear organization** | Rules grouped by topic |

---

## Navigation

### By Purpose

**I want to know about:**

**Filesystem organization**
→ [FILESYSTEM_RULES.md](FILESYSTEM_RULES.md)

**Testing and TDD**
→ [TDD_REQUIREMENTS.md](TDD_REQUIREMENTS.md)

**Agent workspace usage**
→ [AGENT_WORKSPACE.md](AGENT_WORKSPACE.md)

**How to write instructions**
→ [STEP_TEMPLATE.md](STEP_TEMPLATE.md)

### By Audience

**For Agents**:
- [FILESYSTEM_RULES.md](FILESYSTEM_RULES.md) - Where files go
- [TDD_REQUIREMENTS.md](TDD_REQUIREMENTS.md) - How to test
- [AGENT_WORKSPACE.md](AGENT_WORKSPACE.md) - How to track progress

**For Instruction Writers**:
- [STEP_TEMPLATE.md](STEP_TEMPLATE.md) - How to write instructions
- [FILESYSTEM_RULES.md](FILESYSTEM_RULES.md) - What rules to reference
- [TDD_REQUIREMENTS.md](TDD_REQUIREMENTS.md) - Testing requirements

**For Repository Maintainers**:
- All files - Understand all rules
- [FILESYSTEM_RULES.md](FILESYSTEM_RULES.md) - Enforce organization
- [STEP_TEMPLATE.md](STEP_TEMPLATE.md) - Create consistency

---

## Maintenance

### When to Create New Section

Create a new section when:
- Rule applies to multiple steps/contexts
- Rule would be duplicated otherwise
- Rule might change in future

### When to Update Section

Update an existing section when:
- Rule changes or clarification needed
- Better examples discovered
- New patterns emerge
- Feedback received

### Update Procedure

1. Update the `.md` file in `.github/copilot-instructions/`
2. All files that reference it automatically get the change
3. No need to update every instruction file
4. Update takes effect immediately

---

## Current Sections

| Section | Purpose | Status |
|---------|---------|--------|
| FILESYSTEM_RULES.md | File organization | ✅ Created |
| TDD_REQUIREMENTS.md | Testing standards | ✅ Created |
| AGENT_WORKSPACE.md | Workspace rules | ✅ Created |
| STEP_TEMPLATE.md | How to write steps | ✅ Created |

---

## Future Sections

Sections to create as needs emerge:

- [ ] **CODE_STANDARDS.md** - Python style, imports, docstrings
- [ ] **DOCUMENTATION.md** - How to document code
- [ ] **ERROR_HANDLING.md** - Exception handling patterns
- [ ] **PERFORMANCE.md** - Performance expectations
- [ ] **SECURITY.md** - Security guidelines
- [ ] **CI_CD.md** - Continuous integration/deployment

---

## Example: Using Sections

### Step 1 Instructions (AFTER)

```markdown
---
applyTo: "jarvis/**,tests/**"
---

# Step 1: Basic CLI - Copilot Instructions

You are implementing **Step 1 of Jarvis v0.1**.

Build a **command-line interface** that accepts input, echoes commands, and exits gracefully.

---

## Requirements

See [../step_1_specification.md](../step_1_specification.md) for complete details and 40+ test cases.

---

## Testing (TDD Required)

See [.github/copilot-instructions/TDD_REQUIREMENTS.md](../../copilot-instructions/TDD_REQUIREMENTS.md)

Key points:
- Write tests FIRST
- All tests in tests/test_step_1.py
- Run: `pytest tests/test_step_1.py -v`

---

## Filesystem Organization

See [.github/copilot-instructions/FILESYSTEM_RULES.md](../../copilot-instructions/FILESYSTEM_RULES.md)

Key points:
- Create jarvis/cli.py
- Create tests/test_step_1.py
- Use Agent_Workspace for notes only

---

## Agent Workspace

See [.github/copilot-instructions/AGENT_WORKSPACE.md](../../copilot-instructions/AGENT_WORKSPACE.md)

Use Agent_Workspace/README.md to track progress.

---

## Files to Create

```
jarvis/
└── cli.py           ← New CLI class

tests/
└── test_step_1.py   ← New tests (40+ cases)
```

---

## Success Criteria

- [ ] All 40+ tests pass
- [ ] 80%+ code coverage
- [ ] Follows REQUIREMENTS.md standards
- [ ] Agent_Workspace documented
```

### Old Approach (BEFORE)

Every step had 100+ lines of duplicated rules:
- Step_1/.github/copilot-instructions.md (full rules)
- Step_2/.github/copilot-instructions.md (same rules repeated)
- Step_3/.github/copilot-instructions.md (same rules repeated)
- ... etc for 9 steps = 9 copies of same rules

---

## Benefits Realized

### Organization
- ✅ Filesystem rules consolidated to ONE place
- ✅ TDD requirements in ONE place
- ✅ Workspace rules in ONE place
- ✅ Instruction template in ONE place

### Maintenance
- ✅ Change rule once, affects all
- ✅ No more scattered duplicates
- ✅ Easy to find where rules are defined
- ✅ Easy to update consistency

### Consistency
- ✅ All steps follow same rules
- ✅ No conflicting guidance
- ✅ Clear enforcement
- ✅ Professional appearance

### Scalability
- ✅ Easy to add new sections
- ✅ Easy to create new steps
- ✅ Minimal duplication
- ✅ Maintainable long-term

---

## Summary

**Reusable sections enable:**
1. **DRY Principle** - Don't Repeat Yourself
2. **Single Source of Truth** - One place per rule
3. **Consistency** - All steps follow same rules
4. **Maintainability** - Change once, affects all
5. **Scalability** - Easy to grow

**Use the INCLUDE pattern:**
- Reference shared sections in step instructions
- Keep step instructions focused on step-specific content
- Update shared sections when rules change

---

**This system eliminates filesystem mess and instruction duplication.**  
**All rules live in ONE place, referenced everywhere.**  
**Easy to maintain, consistent across all steps.**

**Last Updated**: January 9, 2026
