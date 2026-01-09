# Agent Workspace Structure - Updated

## Summary of Changes

All step folders now include **GitHub custom instructions** and **Agent Workspace folders** for agent documentation.

---

## New Folder Structure

```
Copilot_Development_Instructions/
├── STEPS_LIST.md                          ← NEW: Overview of all steps
├── Step_1/
│   ├── .github/
│   │   └── copilot-instructions.md        ← NEW: Specialized for Step 1
│   ├── Agent_Workspace/
│   │   └── README.md                      ← NEW: Agent notes go here
│   ├── README.md
│   └── step_1_basic_cli.md
├── Step_2/
│   ├── .github/
│   │   └── copilot-instructions.md        ← NEW: Specialized for Step 2
│   ├── Agent_Workspace/
│   │   └── README.md                      ← NEW: Agent notes go here
│   ├── README.md
│   └── step_2_graph_nodes_edges.md
├── Step_3/
│   ├── .github/
│   │   └── copilot-instructions.md        ← NEW: Specialized for Step 3
│   ├── Agent_Workspace/
│   │   └── README.md                      ← NEW: Agent notes go here
│   ├── README.md
│   └── step_3_combined.md
├── Step_4/
│   ├── .github/
│   │   └── copilot-instructions.md        ← NEW: Specialized for Step 4
│   ├── Agent_Workspace/
│   │   └── README.md                      ← NEW: Agent notes go here
│   ├── README.md
│   └── step_4_combined.md
└── DESIGN_REFERENCE/
    ├── README.md
    ├── Folder_Structure_Design.md
    └── Metadata_Design.md
```

---

## What Was Added

### 1. GitHub Custom Instructions (`.github/copilot-instructions.md`)

**In each step folder**, a specialized GitHub copilot-instructions.md file with:
- `applyTo: "jarvis/**,tests/**"` — Applies to production repo
- Step-specific task description
- Test requirements (from spec)
- Files to create
- Workflow steps
- Critical rules
- Confirmation checklist

**Example** (Step 1):
- Build CLI with echo/exit
- 4 test cases required
- Create `jarvis/cli.py`
- TDD mandatory

### 2. Agent_Workspace Folder

**In each step folder**, an Agent_Workspace directory with README explaining:

✅ **What agents CAN do**:
- Create .md files (markdown only)
- Document progress, decisions, questions
- Write notes for Owen to review

❌ **What agents CAN'T do**:
- Create code files
- Build/test in this folder
- Create other file types

**Why it exists**:
- Agents document their work
- Workspace is deleted when step completes
- Notes are copied to design repo for knowledge transfer
- Owen reviews notes to prepare next step

---

## STEPS_LIST.md

New file at repo root: [STEPS_LIST.md](STEPS_LIST.md)

Contains:
- **Overview** of all 4 steps
- **Step-by-step breakdown** with deliverables
- **Test cases** for each step (checklist format)
- **Time estimates**
- **Total test count** (100+ cases)
- **Key principles** (TDD, minimal code, stdlib only)

---

## How Agents Use This

### Workflow Per Step

1. **Agent receives Step_X folder**
   - `.github/copilot-instructions.md` — What to do
   - `step_X_*.md` — Complete specifications
   - `Agent_Workspace/README.md` — Rules for notes

2. **Agent reads instructions**
   - Understands task
   - Sees test requirements
   - Knows what to deliver

3. **Agent works**
   - Writes tests first (TDD)
   - Implements code
   - Creates .md files in Agent_Workspace

4. **Agent confirms**
   - All tests pass
   - Notes in Agent_Workspace
   - Tells Owen: "Step X complete"

5. **Owen reviews**
   - Tests pass? ✅
   - Code quality? ✅
   - Notes in Agent_Workspace? ✅
   - Approves step

6. **Step completes**
   - Code persists (cli.py, graph.py, etc.)
   - Agent_Workspace is deleted
   - Notes are copied to design repo
   - Next step folder prepared

---

## Agent_Workspace Rules Explained

### ✅ ALLOWED in Agent_Workspace

- `.md` files (markdown)
- `Progress.md` — What you've done
- `Questions.md` — Ask Owen
- `Decisions.md` — Design choices
- `Challenges.md` — Problems solved
- `Learnings.md` — What you discovered

### ❌ NOT ALLOWED in Agent_Workspace

- Code files (`.py`, `.js`, etc.)
- Binary files
- Test files (go in `/tests`)
- Production code (goes in `/jarvis`)

### Why This Structure?

1. **Clear separation** — Notes vs. code
2. **Knowledge capture** — Document learnings
3. **Temp vs. permanent** — Workspace is temp
4. **Transfer mechanism** — Notes inform next step
5. **Clean handoff** — Code persists, notes copied

---

## For Production Repo

When copying to production:

1. Each agent gets **ONE Step_X folder**
2. They see:
   - `.github/copilot-instructions.md` ← Main guidance
   - `step_X_*.md` ← Specifications
   - `Agent_Workspace/` ← Place for notes
   - `DESIGN_REFERENCE/` ← Architecture docs
3. They work in `/jarvis` and `/tests`
4. They document in `Agent_Workspace/`
5. When done:
   - Code stays
   - Notes are exported
   - Workspace cleared
   - Next step prepared

---

## Key Features

✅ **GitHub Custom Instructions** — Specialized per step  
✅ **Agent Workspace** — Private documentation space  
✅ **Knowledge Transfer** — Notes inform next steps  
✅ **Clear Rules** — What agents can/can't do  
✅ **STEPS_LIST** — Overview of all steps  
✅ **Isolation Model** — One step at a time  
✅ **TDD Focus** — Tests before code  

---

## STEPS_LIST.md Content

File location: [STEPS_LIST.md](../STEPS_LIST.md)

Includes:
- All 4 steps with descriptions
- Test checklist for each step
- Time estimates
- Deliverables
- Key principles
- Summary table
- Future v0.2 ideas

---

## Next: Create Granular Steps

To break down into smaller, more focused steps:

Current structure:
- Step 1: CLI (1 step)
- Step 2: Graph (1 step)
- Step 3: Observation (2 sub-steps: folder + functions)
- Step 4: Execution (2 sub-steps: functions + engine)

Potential granular breakdown:
- Step 1: CLI
- Step 2.1: Node class
- Step 2.2: Edge class
- Step 2.3: Graph class
- Step 2.4: JSON save/load
- Step 3.1: Folder observation
- Step 3.2: Function observation
- Step 4.1: Test functions
- Step 4.2: ExecutionEngine

This would create 9 total steps instead of 4.

---

## Summary

✅ **GitHub custom instructions added** to all steps  
✅ **Agent_Workspace folders created** in all steps  
✅ **STEPS_LIST.md created** with complete overview  
✅ **Agent rules documented** for workspace usage  
✅ **Knowledge transfer mechanism** in place  

**Ready for production deployment!**
