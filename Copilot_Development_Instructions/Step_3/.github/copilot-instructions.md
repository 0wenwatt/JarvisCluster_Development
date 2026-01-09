---
applyTo: "jarvis/**,tests/**"
---

# Step 3: Code Observation (Folders & Functions) - Copilot Instructions

You are implementing **Step 3 of Jarvis v0.1**.

This step combines two related features:
- **3.1**: Observe folder structure
- **3.2**: Observe Python functions

---

## Your Task

Build observers that teach Jarvis to **understand its own code**:
- Scan folders and create graph nodes for structure
- Parse Python files and extract function definitions
- Create METADATA files to track observations

---

## Test-Driven Development (MANDATORY)

1. **Write tests FIRST** (before any implementation)
2. All test cases are in [../step_3_combined.md](../step_3_combined.md)
3. Run: `pytest tests/test_step_3.py tests/test_step_3_2.py -v`
4. **All tests must pass** before proceeding

---

## What You'll Create

```
jarvis/
├── cli.py          ← (from Step 1)
├── graph.py        ← (from Step 2)
└── observers.py    ← NEW: FolderObserver, PythonObserver

tests/
├── test_step_1.py  ← (from Step 1)
├── test_step_2.py  ← (from Step 2)
├── test_step_3.py  ← NEW: folder observation tests
└── test_step_3_2.py ← NEW: function observation tests
```

---

## Files in This Folder

- **[../step_3_combined.md](../step_3_combined.md)** — Complete requirements + 40+ test specs
- **[../README.md](../README.md)** — Workflow guidance
- **[../DESIGN_REFERENCE/](../DESIGN_REFERENCE/)** — Architecture documentation
- **[Agent_Workspace/](Agent_Workspace/)** — YOUR notes go here

---

## Agent Workspace Rules

⚠️ **Important**: All your working notes go in [Agent_Workspace/](Agent_Workspace/)

- ✅ Create markdown files here (.md files only)
- ✅ Document your progress, design decisions, questions
- ❌ Do NOT create code files here
- 🗑️ **This folder will be deleted when step is done**
- 📦 **Your notes will be copied to the design repo** for knowledge transfer

---

## Workflow

1. **Read** [../step_3_combined.md](../step_3_combined.md) completely
2. **Understand** FolderObserver and PythonObserver requirements
3. **Write** `tests/test_step_3.py` (folder tests)
4. **Write** `tests/test_step_3_2.py` (function tests)
5. **Implement** `jarvis/observers.py` with both classes
6. **Update** `jarvis/cli.py` with `observe` command
7. **Verify** all tests pass
8. **Document** in `Agent_Workspace/`
9. **Tell Owen** — step is complete

---

## Critical Rules

✅ **DO**:
- Write tests FIRST (TDD)
- Keep code < 500 lines
- Use only stdlib (os, ast, json)
- Create METADATA files correctly
- Scan only 1 level deep
- Extract only top-level functions

❌ **DON'T**:
- Skip tests
- Recursively scan all directories
- Parse class methods
- Import external libraries
- Implement Step 4 features
- Look ahead at future steps

---

## Test First Approach

Step 3 requires:
- **20+ test cases** (folder observation)
- **20+ test cases** (function observation)
- Total: **40+ tests** across two test files

Write all tests for BOTH features before implementing.

---

## Confirmation Checklist

When done, verify:
- ✅ `pytest tests/test_step_3.py -v` — all pass
- ✅ `pytest tests/test_step_3_2.py -v` — all pass
- ✅ CLI `observe` command works
- ✅ METADATA files created correctly
- ✅ Function nodes extracted with line numbers
- ✅ Code < 500 lines
- ✅ Notes in `Agent_Workspace/`

Then tell Owen: **"Step 3 complete"**

---

## Next

Once Owen confirms Step 3 is 100% complete:
- ✅ Your code persists (`observers.py`, test files)
- 🗑️ This folder will be cleared
- 📂 You'll get Step 4 folder

Keep notes in `Agent_Workspace/` for knowledge transfer!
