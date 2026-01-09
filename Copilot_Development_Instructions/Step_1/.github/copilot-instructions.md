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
2. All test cases are in [../step_1_basic_cli.md](../step_1_basic_cli.md)
3. Run: `pytest tests/test_step_1.py -v`
4. **All tests must pass** before proceeding

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

- **[../step_1_basic_cli.md](../step_1_basic_cli.md)** — Complete requirements + test specs
- **[../README.md](../README.md)** — Workflow guidance
- **[../DESIGN_REFERENCE/](../DESIGN_REFERENCE/)** — Architecture documentation
- **[Agent_Workspace/](Agent_Workspace/)** — YOUR notes go here

---

## Agent Workspace Rules

⚠️ **Important**: All your working notes go in [Agent_Workspace/](Agent_Workspace/)

- ✅ Create markdown files here (.md files only)
- ✅ Document your progress, decisions, questions
- ❌ Do NOT create code files here
- 🗑️ **This folder will be deleted when step is done**
- 📦 **Your notes will be copied to the design repo** for knowledge transfer

**Example**:
- `Agent_Workspace/Progress.md` — What you've done
- `Agent_Workspace/Questions.md` — Questions for Owen
- `Agent_Workspace/Decisions.md` — Design decisions made

---

## Workflow

1. **Read** [../step_1_basic_cli.md](../step_1_basic_cli.md) completely
2. **Understand** all requirements
3. **Write** `tests/test_step_1.py` (tests first!)
4. **Implement** `jarvis/cli.py`
5. **Verify** all tests pass
6. **Document** in `Agent_Workspace/` (what you learned, any issues)
7. **Tell Owen** — step is complete

---

## Critical Rules

✅ **DO**:
- Write tests FIRST (TDD)
- Keep code minimal (< 500 lines)
- Use only Python stdlib
- Handle edge cases (empty input)
- Document your work in Agent_Workspace

❌ **DON'T**:
- Skip tests
- Add extra features
- Import external libraries
- Look at future steps
- Create code in Agent_Workspace

---

## Test First Approach

Step 1 requires:
- **4 test cases** (from spec file)
- All specified in [../step_1_basic_cli.md](../step_1_basic_cli.md)

Write these tests before implementing `cli.py`.

---

## Confirmation Checklist

When done, verify:
- ✅ `pytest tests/test_step_1.py -v` — all pass
- ✅ Manual CLI test works (type commands, see echoes)
- ✅ No crashes on edge cases
- ✅ Code is < 500 lines
- ✅ Notes in `Agent_Workspace/`

Then tell Owen: **"Step 1 complete"**

---

## Next

Once Owen confirms Step 1 is 100% complete:
- ✅ Your code persists (`cli.py`, `test_step_1.py`)
- 🗑️ This folder will be cleared
- 📂 You'll get Step 2 folder

Keep your notes in `Agent_Workspace/` so Owen can review them!
