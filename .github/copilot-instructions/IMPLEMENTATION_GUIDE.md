# Implementation Guide: Modular Instructions

**How to implement the new modular instruction system across existing and future steps.**

---

## Problem We're Solving

### Before (Messy)
```
Step_1/.github/copilot-instructions.md  (100+ lines with all rules)
Step_2/.github/copilot-instructions.md  (100+ lines with same rules) ← DUPLICATION
Step_3/.github/copilot-instructions.md  (100+ lines with same rules) ← DUPLICATION
Step_4/.github/copilot-instructions.md  (100+ lines with same rules) ← DUPLICATION
... etc × 9 steps

Filesystem:
├── Step_1/
│   ├── Agent_Workspace/
│   │   ├── README.md
│   │   ├── notes.md              ← Temporary
│   │   ├── scratch.py            ← Temporary ❌
│   │   ├── old_code.py           ← Temporary ❌
│   │   └── .tmp files            ← Temporary ❌
│   ├── planning.md
│   ├── notes.md
│   └── progress_tracking.md
```

**Issues**:
- ❌ Rules duplicated 9 times
- ❌ Hard to update consistently
- ❌ Messy workspace with temp files
- ❌ Scattered documentation

---

## Solution: Modular Sections

### After (Clean)
```
.github/copilot-instructions/
├── INDEX.md                     ← Navigation
├── FILESYSTEM_RULES.md          ← ONE place for filesystem rules
├── TDD_REQUIREMENTS.md          ← ONE place for testing rules
├── AGENT_WORKSPACE.md           ← ONE place for workspace rules
└── STEP_TEMPLATE.md             ← Pattern for new steps

Step_1/.github/copilot-instructions.md  (40-50 lines, includes shared sections)
Step_2/.github/copilot-instructions.md  (40-50 lines, includes shared sections)
Step_3/.github/copilot-instructions.md  (40-50 lines, includes shared sections)
... etc × 9 steps (all reference shared sections)

Filesystem:
├── Step_1/
│   └── Agent_Workspace/
│       └── README.md            ← Progress notes only
│           (clean, no temp files)
```

**Benefits**:
- ✅ Rules in ONE place (DRY)
- ✅ Easy to update
- ✅ Consistent across steps
- ✅ Clean workspace
- ✅ Professional appearance

---

## Phase 1: Create Shared Sections (DONE ✅)

✅ Created `.github/copilot-instructions/` folder with:
- `INDEX.md` - Navigation guide
- `FILESYSTEM_RULES.md` - Filesystem organization
- `TDD_REQUIREMENTS.md` - Testing requirements
- `AGENT_WORKSPACE.md` - Workspace rules
- `STEP_TEMPLATE.md` - How to write steps

---

## Phase 2: Update Existing Step Instructions

### For Each Step (1-9)

Update: `Copilot_Development_Instructions/Step_X/.github/copilot-instructions.md`

**Current structure** (~130+ lines):
```markdown
# Step X: [Title]

[All rules embedded in the file]
- Filesystem rules
- Workspace rules
- Testing rules
- Step-specific stuff
```

**New structure** (~50-60 lines):
```markdown
# Step X: [Title]

[Only step-specific content]

See [.github/copilot-instructions/FILESYSTEM_RULES.md](../../copilot-instructions/FILESYSTEM_RULES.md)
See [.github/copilot-instructions/TDD_REQUIREMENTS.md](../../copilot-instructions/TDD_REQUIREMENTS.md)
See [.github/copilot-instructions/AGENT_WORKSPACE.md](../../copilot-instructions/AGENT_WORKSPACE.md)
```

### Implementation Steps

For each Step_X folder:

1. **Read** current `.github/copilot-instructions.md`
2. **Extract** step-specific content only
3. **Replace** with references to shared sections
4. **Verify** links work correctly
5. **Test** by reading the file - does it make sense?

### Steps to Update (Priority Order)

1. **Step_1** - Simple, good starting point
2. **Step_2** - Similar pattern
3. **Step_3** - Similar pattern
4. **Step_4** - More complex (split into 4.1, 4.2)
5. **Steps 5-9** - Follow same pattern

---

## Phase 3: Clean Up Workspaces

### For Each Step

Review: `Copilot_Development_Instructions/Step_X/Agent_Workspace/`

**Current issues**:
```
Agent_Workspace/
├── README.md           ← Good ✅
├── notes.md            ← Might be temp
├── scratch.md          ← Temporary ❌
├── old_code.py         ← Code not allowed ❌
├── temp_notes.txt      ← Temporary ❌
└── .tmp files          ← Temporary ❌
```

**Cleanup process**:

1. Keep: `README.md` with progress tracking
2. Delete: `.md` files with redundant info
3. Delete: Any `.py` files
4. Delete: Any temp/scratch files
5. Keep: Only useful notes for knowledge transfer

**After cleanup**:
```
Agent_Workspace/
└── README.md           ← Progress and decisions only
```

---

## Phase 4: Create Clean Templates

### Agent_Workspace Template

For new steps, provide clean template:

```
Agent_Workspace/
└── README.md           ← Template with headings:
    - Status
    - What I Did
    - Blockers
    - Lessons Learned
    - Next Steps
```

### Step Instruction Template

For new steps, use `STEP_TEMPLATE.md`:

1. Copy structure from template
2. Fill in step-specific content
3. Reference shared sections
4. ~50 lines maximum

---

## Implementation Checklist

### Phase 2: Update Step Instructions

- [ ] Step_1/.github/copilot-instructions.md
  - [ ] Keep only step-specific content
  - [ ] Add references to shared sections
  - [ ] Verify all links work
  - [ ] Test by reading full file

- [ ] Step_2/.github/copilot-instructions.md
  - [ ] Same as Step_1

- [ ] Step_3/.github/copilot-instructions.md
  - [ ] Same as Step_1

- [ ] Step_4/.github/copilot-instructions.md
  - [ ] Update for 4.1 and 4.2
  - [ ] Same reference pattern

- [ ] Steps 5-9
  - [ ] Apply same pattern
  - [ ] Verify each one

### Phase 3: Cleanup Workspaces

- [ ] Step_1/Agent_Workspace/
  - [ ] Keep README.md only
  - [ ] Delete redundant files
  - [ ] Delete temporary files
  - [ ] Update README.md with final summary

- [ ] Steps 2-4
  - [ ] Same cleanup

- [ ] Steps 5-9
  - [ ] Same cleanup

### Phase 4: Template Setup

- [ ] Agent_Workspace template in shared sections
- [ ] Step instruction template ready
- [ ] Index documentation complete
- [ ] All links verified

---

## How to Update Step Instructions

### Example: Updating Step_1

**Current** (`Copilot_Development_Instructions/Step_1/.github/copilot-instructions.md`):

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

---

## Test-Driven Development (MANDATORY)

1. **Write tests FIRST** (before any implementation)
2. All test cases are in [../step_1_basic_cli.md](../step_1_basic_cli.md)
3. Run: `pytest tests/test_step_1.py -v`
4. **All tests must pass** before proceeding

[...more duplicated content...]

---

## Agent Workspace Rules

⚠️ **Important**: All your working notes go in [Agent_Workspace/](Agent_Workspace/)

- ✅ Create markdown files here (.md files only)
- ✅ Document your progress, decisions, questions
- ❌ Do NOT create code files here
- 🗑️ **This folder will be deleted when step is done**

[...more duplicated content...]
```

**New** (`Copilot_Development_Instructions/Step_1/.github/copilot-instructions.md`):

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

## Requirements

See [../step_1_basic_cli.md](../step_1_basic_cli.md) for complete specifications and 40+ test cases.

---

## Testing (TDD Required)

See [.github/copilot-instructions/TDD_REQUIREMENTS.md](../../copilot-instructions/TDD_REQUIREMENTS.md) for:
- Test-driven development workflow
- Test structure and organization
- Success criteria for completion

Key summary:
1. Write tests FIRST (all in specification)
2. Implement code to pass tests
3. Run: `pytest tests/test_step_1.py -v`
4. All tests must pass

---

## Filesystem Organization

See [.github/copilot-instructions/FILESYSTEM_RULES.md](../../copilot-instructions/FILESYSTEM_RULES.md) for:
- File organization rules
- What's allowed in each folder
- Cleanup procedures

Quick summary:
- Create: `jarvis/cli.py`
- Create: `tests/test_step_1.py`
- Notes go: `Agent_Workspace/README.md` only

---

## Agent Workspace

See [.github/copilot-instructions/AGENT_WORKSPACE.md](../../copilot-instructions/AGENT_WORKSPACE.md) for:
- How to use Agent_Workspace
- What files to create
- Progress tracking guidelines
- What happens to your notes

Use `Agent_Workspace/README.md` to document your progress.

---

## Files in This Folder

- **[../step_1_basic_cli.md](../step_1_basic_cli.md)** — Complete requirements + test specs
- **[../README.md](../README.md)** — Workflow guidance
- **[../DESIGN_REFERENCE/](../DESIGN_REFERENCE/)** — Architecture documentation
- **[Agent_Workspace/](Agent_Workspace/)** — YOUR progress notes

---

## What You'll Create

```
jarvis/
└── cli.py           ← Basic CLI with command loop

tests/
└── test_step_1.py   ← Tests (40+ test cases from spec)
```

---

## Success Criteria

- [ ] All 40+ tests pass
- [ ] Code matches specification exactly
- [ ] 80%+ code coverage
- [ ] Follows REQUIREMENTS.md standards
- [ ] Agent_Workspace/README.md completed
```

**Savings**: 70+ lines removed (referenced instead)

---

## Timeline

### Week 1
- ✅ Create shared instruction sections
- Create index documentation
- Prepare update plan

### Week 2
- Update Step_1 instructions
- Update Step_2 instructions
- Update Step_3 instructions

### Week 3
- Update Step_4 instructions
- Update Steps_5-6 instructions

### Week 4
- Update Steps_7-9 instructions
- Complete workspace cleanup
- Final verification

---

## Verification

After completing all phases:

### Check 1: No Duplication
```bash
# All filesystem rules should point to ONE file
grep -r "FILESYSTEM_RULES.md" Copilot_Development_Instructions/
# Should show 9 references (one per step)
```

### Check 2: Clean Workspaces
```bash
# No .py files in workspaces
find Copilot_Development_Instructions/*/Agent_Workspace/ -name "*.py"
# Should find nothing

# Only README.md in workspaces
ls Copilot_Development_Instructions/Step_*/Agent_Workspace/
# Should only show README.md
```

### Check 3: Link Verification
- All `.github/copilot-instructions/` links work
- All references resolve correctly
- No broken links

### Check 4: Consistency
- All steps follow same pattern
- All steps use shared sections
- All workspace formats consistent

---

## Future: New Steps

When creating Step_X (future):

1. **Copy pattern** from STEP_TEMPLATE.md
2. **Reference shared** sections
3. **Add step-specific** content only
4. **Keep length** under 60 lines
5. **Include** template for Agent_Workspace

---

## Benefits After Implementation

### For Agents
- ✅ Clear, focused instructions
- ✅ Easy to find rules
- ✅ Clean workspace template
- ✅ Consistent experience

### For Maintainers
- ✅ One place to update rules
- ✅ All steps stay consistent
- ✅ Easy to add new steps
- ✅ Professional appearance

### For Project
- ✅ DRY principle applied
- ✅ Better organization
- ✅ Reduced clutter
- ✅ Scalable system

---

**This implementation transforms the instruction system from scattered and duplicated to organized and modular.**

**Last Updated**: January 9, 2026
