---
applyTo: "jarvis/**,tests/**"
---

# Step 4: Test Functions & Execution Engine - Copilot Instructions

You are implementing **Step 4 of Jarvis v0.1** — the final step!

This step combines two related features:
- **4.1**: Create test utility functions
- **4.2**: Build execution engine to chain functions

---

## Your Task

Build the **execution pipeline** for Jarvis:
- Create 5 simple utility functions
- Build ExecutionEngine to chain functions together
- Execute function chains via CLI

This completes the MVP: observe → understand → **execute**

---

## Test-Driven Development (MANDATORY)

1. **Write tests FIRST** (before any implementation)
2. All test cases are in [../step_4_combined.md](../step_4_combined.md)
3. Run: `pytest tests/test_step_4_1.py tests/test_step_4_2.py -v`
4. **All tests must pass** before proceeding

---

## What You'll Create

```
jarvis/
├── cli.py          ← (updated from Steps 1-3)
├── graph.py        ← (from Step 2)
├── observers.py    ← (from Step 3)
├── test_functions.py ← NEW: 5 utility functions
└── execution.py    ← NEW: ExecutionEngine class

tests/
├── test_step_*.py  ← (from previous steps)
├── test_step_4_1.py ← NEW: function tests
└── test_step_4_2.py ← NEW: execution tests
```

---

## Files in This Folder

- **[../step_4_combined.md](../step_4_combined.md)** — Complete requirements + 40+ test specs
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

1. **Read** [../step_4_combined.md](../step_4_combined.md) completely
2. **Understand** test functions and execution engine requirements
3. **Write** `tests/test_step_4_1.py` (function tests)
4. **Write** `tests/test_step_4_2.py` (execution tests)
5. **Implement** `jarvis/test_functions.py` (5 functions)
6. **Implement** `jarvis/execution.py` (ExecutionEngine class)
7. **Update** `jarvis/cli.py` with `run` command
8. **Verify** all tests pass
9. **Document** in `Agent_Workspace/`
10. **Tell Owen** — Step 4 complete (v0.1 MVP DONE!)

---

## Critical Rules

✅ **DO**:
- Write tests FIRST (TDD)
- Keep each file < 500 lines
- Use only stdlib (importlib, json, ast)
- Create exactly 5 functions with type hints
- Chain function outputs to next function inputs
- Handle execution errors gracefully

❌ **DON'T**:
- Skip tests
- Add extra functions
- Import external libraries
- Implement complex branching
- Look ahead at future features
- Skip error handling

---

## Test First Approach

Step 4 requires:
- **18 test cases** (test functions)
- **20+ test cases** (execution engine)
- Total: **40+ tests** across two test files

Write all tests for BOTH features before implementing.

---

## Confirmation Checklist

When done, verify:
- ✅ `pytest tests/test_step_4_1.py -v` — all pass
- ✅ `pytest tests/test_step_4_2.py -v` — all pass
- ✅ All 5 functions callable with correct signatures
- ✅ CLI `run` command executes function chains
- ✅ Functions chain outputs correctly
- ✅ Code < 500 lines per file
- ✅ Notes in `Agent_Workspace/`

Then tell Owen: **"Step 4 complete — v0.1 MVP is DONE!"**

---

## v0.1 Completion!

When Step 4 is complete, **Jarvis v0.1 is finished!**

Your MVP can:
- ✅ Accept CLI commands
- ✅ Represent structures as graphs
- ✅ Observe folder structure
- ✅ Observe Python functions
- ✅ Execute chains of functions

Ready for v0.2 planning!

---

## Next

Once Owen confirms Step 4 is 100% complete:
- ✅ Your code persists (all modules and tests)
- 🗑️ This folder will be cleared
- 📂 Begin v0.2 planning

Keep notes in `Agent_Workspace/` for knowledge transfer!
