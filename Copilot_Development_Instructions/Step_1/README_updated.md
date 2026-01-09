# Step 1: Basic CLI - Agent Workspace

You are working on **Step 1 of the Jarvis v0.1 development plan**.

---

## What's in This Folder?

This folder contains **everything you need** to complete Step 1:

- **[step_1_basic_cli.md](step_1_basic_cli.md)** — Detailed requirements, tests, and instructions
- **[DESIGN_REFERENCE/](../DESIGN_REFERENCE/)** — Architectural documentation (shared across all steps)

---

## Your Workflow

### 1. READ THE STEP FILE
Start here: **[step_1_basic_cli.md](step_1_basic_cli.md)**

Read the entire file completely. Understand:
- Overview of the step
- Exact requirements (1.1 - 1.5)
- Test specifications
- How to confirm it's complete

### 2. WRITE TESTS FIRST
Create `tests/test_step_1.py` with all test cases from the step file.

**This is mandatory** — tests before implementation (TDD).

Run tests (they will fail, that's expected):
```bash
pytest tests/test_step_1.py -v
```

### 3. IMPLEMENT
Create `jarvis/cli.py` and implement the CLI to pass all tests.

Run tests again:
```bash
pytest tests/test_step_1.py -v
```

**All tests must pass ✅**

### 4. MANUAL VERIFICATION
Run the CLI manually and test commands:
```bash
python -m jarvis.cli
jarvis> hello
jarvis> world
jarvis> quit
```

Verify it works as expected with no crashes.

### 5. CONFIRM WITH OWEN
When done, tell Owen:
- "Step 1 is complete"
- All tests pass
- Manual testing works

Owen will verify:
- ✅ All pytest tests pass
- ✅ Manual CLI run works
- ✅ Code is < 500 lines
- ✅ Code is clean and readable

---

## Important Rules

✅ **DO:**
- Write tests first (TDD mandatory)
- Read step file completely before starting
- Keep code minimal and focused
- Use only Python stdlib (no external libraries)
- Test with edge cases (empty input, etc.)

❌ **DON'T:**
- Skip the test file
- Implement without tests
- Add extra features ("for future use")
- Use external libraries
- Move to next step until Owen approves

---

## Architecture Context

Read [DESIGN_REFERENCE/README.md](../DESIGN_REFERENCE/README.md) to understand:
- Overall Jarvis architecture
- Folder structure for v0.1
- How modules relate to each other

---

## Files You'll Create

During this step, create:

```
jarvis/
└── cli.py              ← You create this (should be < 500 lines)

tests/
└── test_step_1.py      ← You create this (20+ test cases)
```

The `cli.metadata.json` file will be created automatically in a later step when the code is observed.

---

## Step Isolation Model (Important!)

After you complete this step:

1. ✅ You finish implementation and testing
2. 📋 You create agent notes/logs about what you did
3. 👤 Owen reviews your code and logs
4. ✅ Owen approves Step 1
5. 🗑️ **All workspace files are deleted** (step instructions, DESIGN_REFERENCE, etc.)
6. 📦 Your **produced code** (cli.py, test_step_1.py) persists in the production repo
7. 📂 You get fresh Step 2 folder with its own instructions

This keeps each step focused and prevents looking ahead at future steps.

---

## Next Step

Once Owen confirms Step 1 is 100% complete:
→ Move to **Step 2: Basic Graph, Nodes, Edges**

---

## Questions?

1. Re-read [step_1_basic_cli.md](step_1_basic_cli.md) — it's detailed
2. Check [DESIGN_REFERENCE/](../DESIGN_REFERENCE/) for architecture context
3. Ask Owen for clarification

**Do not proceed to Step 2 until Step 1 is 100% approved.**
