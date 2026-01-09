# Step 1: Basic CLI

**Status**: Ready to implement  
**Estimated Time**: 1-2 hours  
**Complexity**: Low  

---

## Overview

The goal of Step 1 is to establish a **functional input/output channel** for Jarvis. Users (Owen or Copilot) should be able to send commands via CLI, and Jarvis should acknowledge receipt.

This is the **absolute minimum** needed to interact with Jarvis. Nothing fancy—just a command loop that reads input and responds.

---

## Exact Requirements

### 1.1 CLI Interface
- [ ] Create a **command loop** that:
  - Displays a prompt (e.g., `jarvis> `)
  - Reads a single line of text from user input
  - Does NOT crash on empty input
  - Continues looping until user exits

### 1.2 Command Dispatch
- [ ] Parse the input string (strip whitespace)
- [ ] Identify the command (first word)
- [ ] Route to appropriate handler (for now, just echo)
- [ ] Return response to user

### 1.3 Echo Behavior
- [ ] If user types: `hello`
- [ ] Jarvis responds: `Echo: hello` (or similar format)
- [ ] The user can see their command was received and understood

### 1.4 Exit Command
- [ ] Support `exit` command
- [ ] When user types `exit`, Jarvis cleanly exits the loop
- [ ] No crash, no error message—just graceful shutdown

### 1.5 Code Organization
- [ ] Create file: `jarvis/cli.py`
- [ ] File must be < 500 lines
- [ ] Minimal imports (built-in `sys` or similar only)
- [ ] Single class or function for CLI logic (keep it simple)

---

## File Location
```
jarvis/
└── cli.py          ← You create this
```

---

## Tests to Write FIRST

**CRITICAL**: Write these tests **before** implementing `cli.py`. These tests validate your implementation.

### Test File: `tests/test_step_1.py`

This file should contain automated tests using **pytest**.

```python
# Tests you must write (pseudocode below—write real tests):

def test_echo_command():
    # Simulate user typing "hello"
    # Expected: Jarvis responds with "Echo: hello" or similar
    # Verify: response contains the input text

def test_exit_command():
    # Simulate user typing "quit"
    # Expected: CLI loop exits cleanly
    # Verify: no crash, no error

def test_empty_input():
    # Simulate user typing nothing or just whitespace
    # Expected: CLI doesn't crash, re-prompts or handles gracefully
    # Verify: loop continues

def test_multiple_commands():
    # Simulate: "hello" → "world" → "quit"
    # Expected: Each echoed correctly, then clean exit
    # Verify: all three commands processed in order
```

### Test Details

Your tests need to:

1. **Capture stdin/stdout** — Mock or simulate user input, capture CLI output
2. **Verify responses** — Check that input is echoed back correctly
3. **Verify exit behavior** — Confirm `quit` terminates cleanly
4. **Run via pytest** — Command: `pytest tests/test_step_1.py -v`

---

## Implementation Checklist

**REMEMBER**: Write tests first, then implement.

### Phase 1: Write Tests
- [ ] Create `tests/test_step_1.py`
- [ ] Write 4 test cases (echo, exit, empty, multiple)
- [ ] Run tests — they will fail (expected, code doesn't exist yet)
- [ ] Verify test file has no syntax errors

### Phase 2: Implement CLI
- [ ] Create `jarvis/cli.py`
- [ ] Implement `main()` or `run_cli()` function
- [ ] Implement command loop (input → parse → respond → repeat)
- [ ] Implement echo command handler
- [ ] Implement exit command handler
- [ ] Keep file < 500 lines

### Phase 3: Run and Validate Tests
- [ ] Run: `pytest tests/test_step_1.py -v`
- [ ] All tests should pass ✅
- [ ] Run CLI manually and type commands (optional user test)

### Phase 4: Manual Verification
- [ ] Start CLI manually
- [ ] Type `hello` → See echo response
- [ ] Type `world` → See echo response
- [ ] Type `quit` → CLI exits cleanly
- [ ] No crashes or unexpected behavior

---

## How to Confirm This Step Works

### Automated Testing
Run this command in the terminal:
```bash
pytest tests/test_step_1.py -v
```

**Expected output**:
```
tests/test_step_1.py::test_echo_command PASSED
tests/test_step_1.py::test_exit_command PASSED
tests/test_step_1.py::test_empty_input PASSED
tests/test_step_1.py::test_multiple_commands PASSED

====== 4 passed in X.XXs ======
```

### Manual Testing
Run this command:
```bash
python -m jarvis.cli
```
or
```bash
python jarvis/cli.py
```

**Expected behavior**:
1. Prompt appears: `jarvis> `
2. Type `hello` → Response: `Echo: hello` (or similar)
3. Type `world` → Response: `Echo: world`
4. Type `quit` → CLI exits, terminal returns to normal
5. **No errors, no crashes**

### What Owen Will Check
- ✅ All pytest tests pass
- ✅ Manual CLI run works as expected
- ✅ Code is < 500 lines
- ✅ Code is clean and readable
- ✅ No extra features (no validation, help, logging, etc.)

---

## Critical Notes

### DO
- ✅ Write tests first
- ✅ Use only built-in Python modules for now
- ✅ Keep the code minimal and readable
- ✅ Handle `quit`/`exit` commands
- ✅ Echo back user input exactly

### DO NOT
- ❌ Add validation or error checking beyond basics
- ❌ Add help system or documentation
- ❌ Add logging or debug output
- ❌ Add configuration files
- ❌ Add any features not listed above
- ❌ Implement placeholder code for Step 2
- ❌ Import from Sandbox repo

---

## Next Step

Once this step is complete and Owen confirms:
1. All tests pass ✅
2. Manual testing works ✅
3. Code meets all requirements ✅

**Move to Step 2: Graph/Node/Edge**

---

## Questions or Stuck?

1. Re-read the "Exact Requirements" section
2. Check the test examples
3. Verify your tests actually test what they claim to test
4. Ask Owen before proceeding to Step 2

**Do not move forward until both you and Owen confirm this step is 100% complete.**
