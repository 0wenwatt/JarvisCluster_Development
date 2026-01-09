# Filesystem Rules & Organization

**Rules for keeping both design and production repositories clean and well-organized.**

---

## Core Principle

**ONE FILE, ONE PURPOSE. One location per file type. ZERO duplication.**

Each file serves a single, clear purpose. Files that serve the same purpose live in ONE place, not scattered.

---

## Root-Level Files (Design Repo)

### Allowed at Root

✅ **Documentation files** (.md)
- Main guides, overviews, links
- Top-level instructions
- Examples: README.md, USAGE_GUIDE.md, DESIGN_PLAN.md

✅ **Configuration** (repo-wide)
- .gitignore, .github/, .editorconfig
- Minimal config files affecting entire repo

### NOT Allowed at Root

❌ **Duplicate content** (.md files with overlapping purpose)
- If information exists elsewhere, link to it, don't copy it
- If multiple files explain the same thing, consolidate into one

❌ **Code files** (.py, .js, .ts, etc.)
- Code lives in `src/`, `jarvis/`, or production repo
- Never in root

❌ **Temporary files**
- .tmp, notes.md, scratch.py, etc.
- Create in `Agent_Workspace/` which gets deleted

❌ **Scattered config**
- Don't create config in root unless it affects the entire repo
- Project-specific config goes in `config/`

---

## Design Repo: Folder Organization

### Copilot_Local/ (Instructions for Design Repo)
```
Copilot_Local/
├── README.md                    ← Navigation hub
├── GUIDELINES.md                ← Comprehensive guide
├── RULES.md                     ← Quick reference
├── REPOSITORY_MAINTENANCE.md    ← Maintenance procedures
└── ⚠️ Nothing else!
```

**Rule**: This folder is ONLY for instructions about THIS repo. No code, no clutter.

### Copilot_Development_Instructions/ (Shared Instructions)
```
Copilot_Development_Instructions/
├── .github/
│   └── instruction-sections/    ← REUSABLE SECTIONS
│       ├── FILESYSTEM_RULES.md  ← This file
│       ├── TDD_REQUIREMENTS.md  ← Test-driven development
│       ├── AGENT_WORKSPACE.md   ← Workspace rules
│       └── ...
├── DESIGN_REFERENCE/            ← Shared architecture docs
├── Step_1/ through Step_9/       ← Individual step folders
└── INDEX.md                      ← Navigation
```

**Rule**: Reusable sections in `.github/instruction-sections/`, not duplicated in every step.

### JarvisCluster_Design/ (Product Design)
```
JarvisCluster_Design/
├── README.md                    ← Overview of design
├── Architecture/                ← System architecture
├── Components/                  ← Component designs
├── API/                         ← API specifications
└── Decisions/                   ← Design decisions
```

**Rule**: One location per design topic. No scattered design docs.

### Development_Logs/ (Progress Tracking)
```
Development_Logs/
├── INDEX.md                     ← Navigation
├── STEP_1_SUMMARY.md            ← What was completed
├── Step_1/                      ← Archived workspace
├── STEP_2_SUMMARY.md
├── Step_2/
└── ...
```

**Rule**: One summary per step. Workspaces archived once step is complete.

---

## Step Folder Structure (Copilot_Development_Instructions/Step_X/)

### CORRECT Structure
```
Step_5/
├── .github/
│   └── copilot-instructions.md  ← INCLUDES reusable sections
├── step_5_specification.md      ← UNIQUE content for this step
├── Agent_Workspace/             ← Working notes (DELETED after)
│   └── README.md
└── ⚠️ Nothing else!
```

### INCORRECT Structures (OLD - DO NOT USE)

❌ **Duplicate full instructions in each step**
```
Step_1/.github/copilot-instructions.md    (full 100+ lines)
Step_2/.github/copilot-instructions.md    (full 100+ lines)  ← DUPLICATION!
Step_3/.github/copilot-instructions.md    (full 100+ lines)  ← DUPLICATION!
```

❌ **Scattered documentation**
```
Step_1/README.md
Step_1/GUIDELINES.md
Step_1/REQUIREMENTS.md
Step_1/notes.md
Step_1/planning.md              ← Clutter!
```

❌ **Random files in step folders**
```
Step_1/.env
Step_1/config.json
Step_1/scratch.txt
Step_1/old_version.md           ← Temporary files!
```

---

## Instruction File Best Practices

### Pattern: Include + Custom

Instead of duplicating rules, use this pattern:

```markdown
---
applyTo: "jarvis/**,tests/**"
---

# Step X: [Title] - Copilot Instructions

<!-- INCLUDE: FILESYSTEM_RULES -->
<!-- INCLUDE: TDD_REQUIREMENTS -->
<!-- INCLUDE: AGENT_WORKSPACE -->

# Step-Specific Content

Your specific step requirements here...
```

This way:
- ✅ Rules are maintained in ONE place
- ✅ All steps follow consistent rules
- ✅ Updates to rules apply to all steps automatically
- ✅ No duplication

### What Goes in Reusable Sections

✅ **Rules that apply to multiple agents/steps**
- Filesystem organization
- Testing requirements
- Workspace rules
- General practices

❌ **Step-specific details**
- What files to create
- What functions to implement
- Specific requirements for this step
- Step-specific workflows

---

## Agent Workspace Rules

### Purpose
Temporary working area for an agent during a step. DELETED when step completes.

### Structure
```
Agent_Workspace/
├── README.md            ← Your notes and progress
├── TODO.md             ← What you're working on (optional)
├── DECISIONS.md        ← Why you made certain choices
└── ⚠️ Notes ONLY!
```

**MANDATORY RULES**:
1. ✅ `.md` files ONLY (markdown notes)
2. ✅ Document your progress
3. ✅ Document decisions
4. ✅ Document blockers/questions
5. ❌ NO code files (.py, .js, etc.)
6. ❌ NO temporary files (.tmp, .pyc, etc.)
7. ❌ NO config files
8. 🗑️ **This entire folder is DELETED when step completes**

### What Happens to Your Notes
```
Step 5 (during development):
  Agent_Workspace/README.md  ← You write notes here
       ↓
Step 5 (when complete):
  Agent_Workspace/*          → Copied to Development_Logs/Step_5/
       ↓
  Agent_Workspace/           → DELETED (folder cleaned)
```

---

## File Naming Conventions

### Markdown Files

✅ **GOOD NAMING**
- `README.md` - Overview of folder/section
- `STEP_1_SUMMARY.md` - Summary of step 1
- `step_1_specification.md` - Detailed spec for step 1
- `FILESYSTEM_RULES.md` - Rules about filesystems
- `TDD_REQUIREMENTS.md` - TDD rules
- `ADR-0001-use-react.md` - Architecture Decision Record

❌ **BAD NAMING**
- `notes.md` - Too vague
- `TODO.md` - Where? For what?
- `stuff.md` - Meaningless
- `temp_notes.md` - Sounds temporary
- `quick_fix.md` - Sounds temporary
- `PLEASE_READ.md` - Unprofessional

### Code Files

✅ **GOOD STRUCTURE**
```
src/
  module/
    __init__.py
    core.py            ← Core functionality
    utils.py           ← Utilities
    exceptions.py      ← Custom exceptions

tests/
  test_core.py         ← Tests for core.py
  test_utils.py        ← Tests for utils.py
  fixtures/
    sample_data.py     ← Test fixtures
```

❌ **BAD STRUCTURE**
```
src/
  module.py            ← All code in one file
  module_updated.py    ← Versioning (use git!)
  module_backup.py     ← Backups (use git!)

tests/
  all_tests.py         ← Everything together
  test.py              ← Too generic
```

---

## Cleanup Checklist

### After Each Development Session
- [ ] Delete temporary files (.tmp, .pyc, __pycache__)
- [ ] Don't create random notes in code folders
- [ ] Update Agent_Workspace/README.md with progress
- [ ] No stray print statements in code

### When Step is Complete
- [ ] Copy Agent_Workspace/ to Development_Logs/Step_X/
- [ ] Delete Agent_Workspace/ folder
- [ ] Remove any .env files (use .env.example instead)
- [ ] Clean up any debug files
- [ ] Verify folder structure matches specification

### Monthly Repository Cleanup
- [ ] No orphaned folders
- [ ] No duplicate content
- [ ] All links still work
- [ ] No temporary files
- [ ] Clear structure

---

## Production Repo Filesystem

### Jarvis Repository Structure

```
jarvis/
├── src/
│   └── jarvis/
│       ├── __init__.py
│       ├── cli.py               ← Command-line interface
│       ├── graph.py             ← Dependency graph
│       ├── observers.py         ← Event observers
│       ├── execution.py         ← Execution engine
│       ├── test_functions.py    ← Test utility functions
│       └── ...
├── tests/
│   ├── test_cli.py
│   ├── test_graph.py
│   ├── test_observers.py
│   ├── test_execution.py
│   └── ...
├── docs/
│   ├── api.md
│   ├── architecture.md
│   └── ...
├── README.md
├── requirements.txt
├── setup.py
└── .gitignore
```

**Rules**:
- ✅ Code in `src/jarvis/`
- ✅ Tests mirror `src/` structure
- ✅ Docs in `docs/`
- ✅ Config files in root only if repo-wide
- ❌ No duplicate code
- ❌ No temp files in commit
- ❌ No scattered documentation

---

## Repository-Specific Rules

### Design Repo (JarvisCluster_Development)

**Purpose**: Planning, design, coordination

**Structure Principles**:
- Design docs in ONE place (JarvisCluster_Design/)
- Instructions in ONE place (Copilot_Development_Instructions/)
- Reusable sections centralized (.github/copilot-instructions/)
- Progress tracked in Development_Logs/
- No production code

**Key Rules**:
- ✅ Link to production repo, don't duplicate its content
- ✅ Instruction sections are SHARED, not duplicated
- ✅ Agent workspaces are temporary and cleaned up
- ❌ No code implementation
- ❌ No scattered documentation

### Production Repo (Jarvis)

**Purpose**: Implementation, testing, code

**Structure Principles**:
- Code follows file tree specification
- Tests mirror code structure
- Documentation updated alongside code
- Clean, focused, minimal

**Key Rules**:
- ✅ Follow file tree structure exactly
- ✅ Tests for every function
- ✅ Documentation in docstrings
- ✅ Clean git history
- ❌ No design decision-making
- ❌ No scattered notes
- ❌ No commented-out code

---

## Enforcement Strategy

### For Agents
1. **Check before creating**: Does this file/folder exist elsewhere?
2. **Reuse first**: Link to existing content instead of copying
3. **Consolidate**: If scattered files exist, gather them
4. **Clean up**: Delete temporary files before finishing

### For Reviewers
1. **Spot duplication**: Flag files with overlapping purpose
2. **Enforce structure**: Point to correct location
3. **Cleanup focus**: Delete clutter before merging
4. **Guidelines check**: Verify new files follow rules

### For Repository Maintainers
1. **Regular audits**: Monthly check for scattered files
2. **Consolidation**: Merge overlapping documentation
3. **Structure review**: Ensure organization matches spec
4. **Link verification**: Update references when moving files

---

## Summary

| Principle | Rule | Violation |
|-----------|------|-----------|
| **One Purpose** | One file per function | Multiple files doing same thing |
| **One Location** | Rules in centralized sections | Rules scattered in every step |
| **Clear Structure** | Folders organized logically | Random files everywhere |
| **No Duplication** | Link to content, don't copy | Copy-paste instruction files |
| **Temporary Cleanup** | Delete Agent_Workspace when done | Leave old workspaces lingering |
| **Reusable Sections** | INCLUDE directive | Duplicate full instructions |

---

**This file is the source of truth for filesystem organization.**  
**All other files should link to it, not redefine rules.**

**Last Updated**: January 9, 2026
