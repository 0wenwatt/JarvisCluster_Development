---
applyTo: "jarvis/**,tests/**,Diagnostics/**"
---

# START HERE: Copilot Instructions for Jarvis Development Repo

**READ THIS FIRST** if you are a Copilot or AI agent working in the **actual Jarvis development repository**.

---

## What is This?

You are building **Jarvis Cluster v0.1** — the minimum viable product.

This folder contains instructions that guide your actual implementation work. These instructions come from the **design repository** (`JarvisCluster_Development`) where the plan was created.

**Important**: There is a **separate design repository** that prepared this entire plan. You are in the **production/development repository**. Don't go looking for the design repo—just follow these instructions.

---

## Your Mission

Follow the step-by-step development plan **exactly**. Implement one step at a time:

1. **Step 1**: Basic CLI
2. **Step 2**: Graph/Node/Edge
3. **Step 3**: Folder Observation
4. **Step 3.2**: Function Observation
5. **Step 4.1**: Test Functions
6. **Step 4.2**: Execution Engine

When v0.1 is complete, you'll have a working Jarvis that can:
- ✅ Accept CLI commands
- ✅ Represent structures as graphs
- ✅ Observe its own codebase
- ✅ Execute chains of functions

---

## The Workflow for EACH Step

This is critical—follow this process for every single step:

1. **Read** — Read the ENTIRE step file (in `Agent_Workspace/`)
2. **Understand** — Understand all requirements
3. **Design** — Design the data structures and functions
4. **Test First** — Write ALL tests before ANY implementation
5. **Implement** — Write code to pass the tests
6. **Verify** — Run tests locally
7. **Confirm** — Ask Owen to confirm the step is complete
8. **Move** — Don't move to the next step until Owen approves

**TDD is mandatory**: Tests ALWAYS come before implementation.

---

## File Structure

You have been given:

```
Agent_Workspace/
├── step_1_basic_cli.md              (detailed step 1 instructions)
├── step_2_graph_nodes_edges.md      (detailed step 2 instructions)
├── step_3_observation_folders.md    (detailed step 3 instructions)
├── step_3_2_observation_functions.md (detailed step 3.2 instructions)
├── step_4_1_test_functions.md       (detailed step 4.1 instructions)
├── step_4_2_execution_engine.md     (detailed step 4.2 instructions)
├── ode Organization Rules

Your code must follow this **exact** structure:

```
jarvis/
├── __init__.py
├── cli/
│   ├── cli.py
│   ├── cli.metadata.json
│   └── cli_Test.py
├── graph/
│   ├── graph.py
│   ├── graph.metadata.json
│   └── graph_Test.py
├── observers/
│   ├── observers.py
│   ├── observers.metadata.json
│   └── observers_Test.py
├── test_functions/
│   ├── test_functions.py
│   ├── test_functions.metadata.json
│   └── test_functions_Test.py
├── execution/
│   ├── execution.py
│   ├── execution.metadata.json
│   └── execution_Test.py
└── Diagnostics/
    └── test_suit.py
```

**Rules**:
- One main implementation file per folder
- One test file per folder (same folder as implementation)
- One metadata JSON file per module
- Test file name format: `module_name_Test.py`
- Metadata file name format: `module_name.metadata.json`

---

## Testing Approach

Testing is **critical** to v0.1 success:

### Test-Driven Development (TDD)
1. **Write tests first** — Before any implementation
2. **Tests define behavior** — Tests are your specification
3. **Tests must pass** — All tests must pass before moving to next step
4. **No cherry-picking** — Implement everything the tests require, no more, no less

### Running Tests
```bash
# Run all tests
pytest tests/test_step_*.py -v

# Run tests for a specific step
pytest tests/test_step_1.py -v

# Run the master test suite
python Diagnostics/test_suit.py
```

### Test File Location
- Test files live **alongside** implementation files
- Example: `graph.py` and `graph_Test.py` in same folder
- Use pytest framework

---

## Metadata Files

Every module has a `.metadata.json` file describing it:

```json
{
  "general": {
    "name": "module_name",
    "description": "What this module does",
    "version": "0.1",
    "status": "in-development"
  },
  "implementation": {
    "file": "module_name.py",
    "status": "in-progress",
    "completion_percentage": 50
  },
  "testing": {
    "file": "module_name_Test.py",
    "status": "tests-ahead",
    "test_count": 10,
    "passing_tests": 0,
    "failing_tests": 10
  },
  "functions": [],
  "dependencies": [],
  "copilot_notes": ""
}
```

See `DESIGN_REFERENCE/Metadata_Design.md` for full details.

---

## Critical Rules

### ✅ DO
- Write tests before implementation
- Follow the step-by-step plan exactly
- Keep functions small (< 500 lines per file)
- Use only Python stdlib (no external packages unless specified)
- Create METADATA files as specified
- Ask Owen before skipping anything
- Confirm with Owen after each step

### ❌ DON'T
- Skip steps or jump ahead
- Implement "future features"
- Copy code from any Sandbox repo
- Add error handling beyond what's specified
- Create files outside the designed structure
- Assume anything—if unclear, ask Owen
- Move to the next step without Owen approval

---

## The TDD Cycle (Repeat for Each Step)

```
1. READ step file
   ↓
2. WRITE tests (all of them, before any code)
   ↓
3. RUN tests (they will fail—expected)
   ↓
4. IMPLEMENT code to pass tests
   ↓
5. RUN tests again (they should pass)
   ↓
6. MANUAL test via CLI (if applicable)
   ↓
7. ASK OWEN to confirm
   ↓
8. NEXT STEP (only after Owen approves)
```

---

## When You Get Stuck

1. **Re-read the step file** — Very detailed, answer is likely there
2. **Check test requirements** — Tests define expected behavior exactly
3. **Look at design reference** — Folder structure, metadata format, etc.
4. **Ask Owen** — Before proceeding or making assumptions

---

## Success Criteria for v0.1

When all 6 steps are complete:

- [ ] All tests pass
- [ ] All steps confirmed by Owen
- [ ] Code follows all guidelines
- [ ] METADATA files created for all modules
- [ ] CLI works interactively
- [ ] Code is clean and readable
- [ ] No extra features beyond each step's specification
- [ ] No external dependencies (stdlib only)
- [ ] No Sandbox code used

---

## Important Notes

### Zero Time Pressure
- Complete means **100% correct**, not fast
- No rush—quality over speed
- Better to do less perfectly than more poorly

### Tests Are Your Spec
- If tests pass, you're done
- Don't implement beyond what tests require
- Tests stay ahead of implementation (TDD)

### Communication
- Confirm with Owen after each step
- Ask questions before guessing
- Don't move forward without approval

### Code Quality
- One class per file
- < 500 lines per file
- Clear, readable naming
- Docstrings on classes and functions
- Type hints where applicable

---

## Next Steps

1. Open the **first step file** in `Agent_Workspace/`
2. Read it completely
3. Understand all requirements
4. Start the TDD cycle above

Good luck! Remember: **Tests first, implementation second.**

## Next Step

1. Read the current step file
2. Understand the requirements
3. Write tests
4. Implement
5. Confirm with Owen
6. Repeat

Good luck! 🚀

