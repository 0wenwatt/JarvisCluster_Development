# Step 4: Test Functions & Execution Engine

This step combines **Step 4.1** (Test Functions) and **Step 4.2** (Execution Engine) as they work together—the functions are the building blocks that the execution engine chains together.

---

## Part 1: Step 4.1 - Test Functions

**Status**: Ready to implement  
**Estimated Time**: 1-2 hours  
**Complexity**: Low  
**Prerequisite**: Steps 1-3.2 complete ✅  

### Overview

Step 4.1 creates a set of **simple, reusable functions** that will be used in Step 4.2 to test the execution engine.

These are intentionally basic utility functions—nothing fancy. They serve as building blocks to validate that the execution engine can call functions and chain their outputs together.

### Exact Requirements - Step 4.1

#### 4.1.1 Test Functions Module

**Location**: `jarvis/test_functions.py` (NEW module)

Create a Python module with exactly these 5 functions:

```python
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

def concat(str1: str, str2: str) -> str:
    """Concatenate two strings."""
    return str1 + str2

def uppercase(text: str) -> str:
    """Convert string to uppercase."""
    return text.upper()

def length(text: str) -> int:
    """Return length of string."""
    return len(text)
```

**Constraints**:
- Exactly these 5 functions, no more, no less
- Type hints must be present
- Docstrings must be present
- Each function is simple (1-2 lines of logic)
- No error handling beyond basic types
- No dependencies or imports (stdlib only)

#### 4.1.2 METADATA File

When these functions are observed (by Step 3.2), a METADATA file will be created:

**Location**: `jarvis/test_functions.py.metadata.json`

**Format** (created by observer):
```json
{
  "type": "file",
  "copilot_notes": "",
  "functions": [
    "test_functions.py:add",
    "test_functions.py:multiply",
    "test_functions.py:concat",
    "test_functions.py:uppercase",
    "test_functions.py:length"
  ]
}
```

This will be automatically created in Step 3.2 when the module is observed. You don't create it manually.

#### 4.1.3 Code Organization

```
jarvis/
├── __init__.py
├── test_functions.py        (NEW: test functions module)
├── cli.py
├── graph.py
├── observers.py
└── execution.py
```

**Constraints**:
- File < 500 lines (will be ~30 lines)
- Only stdlib imports (none needed)
- Module-level functions only (no classes)

---

## Part 2: Step 4.2 - Basic Execution Engine

**Status**: Ready to implement  
**Estimated Time**: 3-4 hours  
**Complexity**: Medium  
**Prerequisite**: Steps 1-4.1 complete ✅  

### Overview

Step 4.2 is the **final step for v0.1**. This is where Jarvis learns to **execute** — to take a graph of linked functions and actually run them.

The execution engine will:
- Load a graph containing function nodes and edges
- Execute functions in order (simple linear chain)
- Pass outputs from one function as inputs to the next
- Return final result

This completes the minimum viable product: observe → understand → execute.

### Exact Requirements - Step 4.2

#### 4.2.1 ExecutionEngine Class

**Location**: `jarvis/execution.py` (NEW file)

Create an `ExecutionEngine` class:

```python
class ExecutionEngine:
    
    Methods:
    - __init__()
    
    - execute(graph: Graph, start_node_id: str, initial_input: dict) -> any:
      • Execute a chain of functions defined in the graph
      • Parameters:
        - graph: Graph with function nodes and edges
        - start_node_id: ID of the first node to execute
        - initial_input: dict with input values for first function
          Example: {"a": 2, "b": 3} for add(a, b)
      • Algorithm:
        1. Find start node in graph
        2. Get function to execute from node (via lookup)
        3. Call function with initial_input values (unpacked as **kwargs)
        4. Get output
        5. Follow edge(s) from current node to next node(s)
        6. Use output from previous step as input to next step
        7. Continue until no more edges
        8. Return final output
      
      Constraints:
      - Assume linear chains (one output → one next node)
      - If multiple edges from a node, pick first one (or error)
      - If no edges from node, return output
      - If function not found, raise error (don't silently fail)
      • Return final output (any type)
```

#### 4.2.2 Function Lookup

The execution engine needs to **find and call functions** referenced by nodes.

**Function ID Format** (from Step 4.1):
- Format: `{module}:{function_name}`
- Example: `test_functions.py:add`

**Lookup Process**:
- Parse function ID to get module name and function name
- Dynamically import the module (e.g., `jarvis.test_functions`)
- Get the function from the module (e.g., `getattr(module, "add")`)
- Call the function with provided inputs

**Constraints**:
- Only lookup functions in `jarvis/` package for v0.1
- Don't load arbitrary modules from disk
- Raise error if function not found
- Use `importlib` module (stdlib)

#### 4.2.3 Input/Output Chaining

**Assumption**: Each function returns a single value (not tuple/dict).

**Chaining Logic**:
1. First function receives initial_input as `**kwargs`
2. First function returns a value (e.g., `5`)
3. Next function receives the previous output as a **single positional argument**
4. Continue until no more edges

**Example Chain**:
```
Initial: add(a=2, b=3) → returns 5
Next: multiply(5, 4) → returns 20
Next: length(str(20)) → returns 2
Final: 2
```

**Constraint**: For v0.1, assume each function takes exactly one input (except first function).

#### 4.2.4 Execution Graph Format

**Nodes** contain function references:
- Must have a unique ID matching the function ID (e.g., `test_functions.py:add`)
- Or, node must have metadata with `"function_id"` pointing to the function

For v0.1, **use the node ID directly** as the function ID.

**Edges** define the chain:
- `source_id` → `target_id` means:
  - Execute source function first
  - Pass output to target function

**Example Execution Graph** (JSON):
```json
{
  "nodes": [
    {"id": "test_functions.py:add", "label": "add", "metadata": {}},
    {"id": "test_functions.py:multiply", "label": "multiply", "metadata": {}},
    {"id": "test_functions.py:length", "label": "length", "metadata": {}}
  ],
  "edges": [
    {"source_id": "test_functions.py:add", "target_id": "test_functions.py:multiply", "metadata": {}},
    {"source_id": "test_functions.py:multiply", "target_id": "test_functions.py:length", "metadata": {}}
  ]
}
```

#### 4.2.5 CLI Command

**Location**: Update `jarvis/cli.py`

Add this command:

| Command | Syntax | Behavior |
|---------|--------|----------|
| `run` | `run <graph_file> <start_node_id> <input_json>` | Execute graph |

**Behavior**:
- Load graph from JSON file
- Parse start node ID
- Parse input as JSON (e.g., `'{"a": 2, "b": 3}'`)
- Call `ExecutionEngine.execute()`
- Display result
- Print execution summary

**Example**:
```
jarvis> run execution_graph.json test_functions.py:add '{"a": 2, "b": 3}'
Executing graph...
  Start: test_functions.py:add with input {a: 2, b: 3}
    Result: 5
  Next: test_functions.py:multiply with input 5
    Result: 20
  Next: test_functions.py:length with input "20"
    Result: 2
Final result: 2
```

#### 4.2.6 Error Handling

For v0.1, keep error handling minimal but present:

```python
# Handle these cases gracefully:
- Start node not found in graph → raise ValueError
- Function not found in module → raise ImportError or AttributeError
- Function call fails → let exception propagate (with context message)
- No edges from node → return current output (normal termination)
```

**Constraint**: Print user-friendly error messages, don't crash silently.

#### 4.2.7 Code Organization

```
jarvis/
├── __init__.py
├── cli.py                   (updated)
├── graph.py                 (from Step 2)
├── observers.py             (from Steps 3-3.2)
├── test_functions.py        (from Step 4.1)
└── execution.py             (NEW: ExecutionEngine class)
```

**Constraints**:
- `execution.py` must be < 500 lines
- Use only stdlib (importlib, json, etc.)
- Simple and focused implementation

---

## Example Execution Graphs

You'll need to create test execution graphs. Two examples:

### Example 1: add → multiply

**File**: `tests/graphs/execution_add_multiply.json`

```json
{
  "nodes": [
    {"id": "test_functions.py:add", "label": "add", "metadata": {}},
    {"id": "test_functions.py:multiply", "label": "multiply", "metadata": {}}
  ],
  "edges": [
    {"source_id": "test_functions.py:add", "target_id": "test_functions.py:multiply", "metadata": {}}
  ]
}
```

**Execution**:
- Input: `{"a": 2, "b": 3}` → add → returns 5
- Input: `5` → multiply with hardcoded 4 → returns 20

### Example 2: concat → uppercase

**File**: `tests/graphs/execution_concat_uppercase.json`

```json
{
  "nodes": [
    {"id": "test_functions.py:concat", "label": "concat", "metadata": {}},
    {"id": "test_functions.py:uppercase", "label": "uppercase", "metadata": {}}
  ],
  "edges": [
    {"source_id": "test_functions.py:concat", "target_id": "test_functions.py:uppercase", "metadata": {}}
  ]
}
```

**Execution**:
- Input: `{"str1": "hello", "str2": " world"}` → concat → returns "hello world"
- Input: `"hello world"` → uppercase → returns "HELLO WORLD"

---

## Code Organization

```
jarvis/
├── __init__.py
├── cli.py                   (updated from Steps 1-2)
├── graph.py                 (from Step 2)
├── observers.py             (from Steps 3-3.2)
├── test_functions.py        (NEW: 5 functions for testing)
└── execution.py             (NEW: ExecutionEngine class)
```

**Constraints**:
- Each module < 500 lines
- Use only stdlib imports
- Simple and focused

---

## Tests to Write FIRST

**CRITICAL**: Write ALL these tests **before** implementing anything.

### Test File: `tests/test_step_4_1.py` (Functions)

```python
# Tests you must write:

def test_add_basic():
    # Import add from jarvis.test_functions
    # Call add(2, 3)
    # Verify: result is 5

def test_add_floats():
    # Call add(2.5, 3.5)
    # Verify: result is 6.0

def test_add_negative():
    # Call add(10, -3)
    # Verify: result is 7

def test_multiply_basic():
    # Call multiply(4, 5)
    # Verify: result is 20

def test_multiply_by_zero():
    # Call multiply(100, 0)
    # Verify: result is 0

def test_multiply_floats():
    # Call multiply(2.5, 4)
    # Verify: result is 10.0

def test_concat_basic():
    # Call concat("hello", "world")
    # Verify: result is "helloworld"

def test_concat_empty_strings():
    # Call concat("", "test")
    # Verify: result is "test"

def test_concat_spaces():
    # Call concat("hello", " world")
    # Verify: result is "hello world"

def test_uppercase_basic():
    # Call uppercase("jarvis")
    # Verify: result is "JARVIS"

def test_uppercase_mixed():
    # Call uppercase("JaRvIs")
    # Verify: result is "JARVIS"

def test_uppercase_with_numbers():
    # Call uppercase("test123")
    # Verify: result is "TEST123"

def test_length_basic():
    # Call length("hello")
    # Verify: result is 5

def test_length_empty():
    # Call length("")
    # Verify: result is 0

def test_length_with_spaces():
    # Call length("hello world")
    # Verify: result is 11

def test_function_signatures():
    # Import all 5 functions
    # Verify: each is callable
    # Verify: each has type hints
    # Verify: each has docstring

def test_return_types():
    # Verify each function returns correct type
```

### Test File: `tests/test_step_4_2.py` (Execution)

```python
# Tests you must write:

def test_execution_engine_simple_add():
    # Create engine
    # Create graph with single add node
    # Execute with input {a: 2, b: 3}
    # Verify: result is 5

def test_execution_engine_two_step_chain():
    # Create graph: add → multiply
    # Execute: add(2, 3)=5, multiply(5, 4)=20
    # Verify: final result is 20

def test_execution_engine_three_step_chain():
    # Create graph: add → multiply → length(str(result))
    # Execute: add(2,3)=5, multiply(5,4)=20, length("20")=2
    # Verify: final result is 2

def test_execution_engine_string_chain():
    # Create graph: concat → uppercase
    # Execute: concat("hello", " world") → uppercase
    # Verify: final result is "HELLO WORLD"

def test_execution_engine_load_graph():
    # Load execution graph from JSON file
    # Execute it
    # Verify: executes correctly

def test_execution_engine_single_node_no_edges():
    # Create graph with 1 node, 0 edges
    # Execute it
    # Verify: function executed, result returned

def test_execution_engine_missing_start_node():
    # Try to execute with non-existent start node ID
    # Verify: raises error

def test_execution_engine_missing_function():
    # Create graph with invalid function ID
    # Try to execute
    # Verify: raises error

def test_execution_engine_correct_input_passing():
    # Create chain: add(2,3) → multiply(?,4)
    # Verify: output of add (5) is passed to multiply
    # Verify: result is 5 * 4 = 20

def test_execution_engine_string_input_passing():
    # Create chain: concat("a", "b") → uppercase(?)
    # Verify: output "ab" passed to uppercase
    # Verify: result is "AB"

def test_cli_run_command():
    # Simulate CLI: "run tests/graphs/execution_add_multiply.json test_functions.py:add '{"a": 2, "b": 3}'"
    # Verify: executes and result displayed

def test_cli_run_with_string_input():
    # Simulate CLI with string operations
    # Verify: chain executes correctly

def test_function_lookup_correct_module():
    # Create node with id "test_functions.py:add"
    # Verify: correct module and function loaded

def test_execution_result_type():
    # Verify results have correct types
```

---

## Implementation Checklist

### Phase 1: Write All Tests
- [ ] Create `tests/test_step_4_1.py` with 18 test cases
- [ ] Create `tests/test_step_4_2.py` with 20+ test cases
- [ ] Run tests — they will fail (expected)
- [ ] Verify no syntax errors

### Phase 2: Create Test Functions
- [ ] Create `jarvis/test_functions.py`
- [ ] Add exactly 5 functions (code provided above)
- [ ] Include type hints and docstrings
- [ ] Keep logic simple

### Phase 3: Run Step 4.1 Tests
- [ ] Run: `pytest tests/test_step_4_1.py -v`
- [ ] All tests pass ✅

### Phase 4: Create Example Execution Graphs
- [ ] Create `tests/graphs/execution_add_multiply.json`
- [ ] Create `tests/graphs/execution_concat_uppercase.json`
- [ ] Verify JSON format is valid

### Phase 5: Implement ExecutionEngine
- [ ] Create `jarvis/execution.py`
- [ ] Implement `ExecutionEngine` class with `execute()` method
- [ ] Implement function lookup using importlib
- [ ] Implement input/output chaining
- [ ] Add error handling
- [ ] Keep file < 500 lines

### Phase 6: Update CLI
- [ ] Update `jarvis/cli.py`
- [ ] Add `run` command
- [ ] Parse JSON input arguments
- [ ] Display execution results with summary

### Phase 7: Run Step 4.2 Tests
- [ ] Run: `pytest tests/test_step_4_2.py -v`
- [ ] All tests pass ✅

### Phase 8: Manual Testing
- [ ] Test Step 4.1: Call all 5 functions directly
- [ ] Test Step 4.2: Execute example graphs via CLI
- [ ] Verify output correctness
- [ ] Test error cases (missing node, invalid function, etc.)

---

## How to Confirm This Step Works

### Automated Testing

**Step 4.1**:
```bash
pytest tests/test_step_4_1.py -v
```

**Step 4.2**:
```bash
pytest tests/test_step_4_2.py -v
```

**Expected**: All tests pass ✅

### Manual Testing - Step 4.1

```python
from jarvis.test_functions import add, multiply, concat, uppercase, length

assert add(2, 3) == 5
assert multiply(4, 5) == 20
assert concat("hello", "world") == "helloworld"
assert uppercase("jarvis") == "JARVIS"
assert length("hello") == 5
```

### Manual Testing - Step 4.2

**Test 1**:
```
jarvis> run tests/graphs/execution_add_multiply.json test_functions.py:add '{"a": 2, "b": 3}'
```

**Expected**:
```
Executing graph...
  Start: test_functions.py:add with input {a: 2, b: 3}
    Result: 5
  Next: test_functions.py:multiply with input 5
    Result: 20
Final result: 20
```

**Test 2**:
```
jarvis> run tests/graphs/execution_concat_uppercase.json test_functions.py:concat '{"str1": "hello", "str2": " world"}'
```

**Expected**:
```
Executing graph...
  Start: test_functions.py:concat with input {str1: hello, str2:  world}
    Result: hello world
  Next: test_functions.py:uppercase with input hello world
    Result: HELLO WORLD
Final result: HELLO WORLD
```

### What Owen Will Check

**Step 4.1**:
- ✅ All pytest tests pass
- ✅ All 5 functions present and callable
- ✅ Type hints and docstrings present
- ✅ Functions return correct types and values
- ✅ Observation extracts all 5 functions

**Step 4.2**:
- ✅ All pytest tests pass
- ✅ CLI `run` command works
- ✅ Functions executed in correct order
- ✅ Outputs chained correctly
- ✅ Results are accurate
- ✅ Error handling is present
- ✅ Code < 500 lines each

---

## Critical Notes

### DO
- ✅ Write ALL tests first (both test_step_4_1 and test_step_4_2)
- ✅ Use type hints and docstrings in test functions
- ✅ Keep function logic simple
- ✅ Use importlib for dynamic function loading
- ✅ Pass outputs as kwargs/args correctly
- ✅ Handle errors gracefully
- ✅ Test with multiple function types

### DO NOT
- ❌ Add extra functions beyond the 5
- ❌ Hard-code functions to call
- ❌ Skip error handling
- ❌ Load functions from outside `jarvis/` package
- ❌ Try to handle complex branching/loops
- ❌ Add performance optimizations
- ❌ Implement features for v0.2+

---

## v0.1 Completion Summary

When Step 4 is complete, **Jarvis v0.1 is DONE!**

Your Jarvis MVP will:

1. ✅ **Accept CLI commands** (Step 1)
2. ✅ **Represent any structure as Graphs** with Nodes and Edges (Step 2)
3. ✅ **Observe folder structure** (Step 3)
4. ✅ **Observe Python functions** in code files (Step 3.2)
5. ✅ **Execute chains of linked functions** (Step 4.2)

**Complete observation → execution pipeline!**

Ready for v0.2 development.

---

## Next Steps (After v0.1)

Once v0.1 is complete:
- Plan v0.2 features
- Expand to handle more complex graphs
- Add more sophisticated function chaining
- Implement proper return value handling for multi-argument functions

---

## Questions or Stuck?

1. Re-read "Exact Requirements"
2. Check test examples for expected behavior
3. Verify function signatures and types
4. Test execution with simple examples first
5. Ask Owen before concluding Step 4

**Do not mark this step complete until both you and Owen confirm v0.1 is 100% working.**
