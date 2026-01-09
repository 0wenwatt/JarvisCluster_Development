# Test-Driven Development (TDD) Requirements

**Mandatory requirements for all Jarvis development using test-driven development.**

---

## Core Rule

**TESTS FIRST, IMPLEMENTATION SECOND**

1. Write test cases (and specs) FIRST
2. Then write code to pass the tests
3. All tests must pass before step is complete

---

## Test-Driven Development Workflow

### Step 1: Understand Requirements
- Read the step specification document
- Review the test cases provided
- Understand expected behavior

### Step 2: Write Tests (In Specification)
- Test cases are in the step specification file
- Example: `step_4_combined.md` contains 40+ test cases
- You write these tests in your code

### Step 3: Implement Code
- Write code to pass the tests
- Implement functions as specified
- Follow the file structure from specification

### Step 4: Run Tests
```bash
# Run all tests for this step
pytest tests/test_step_X.py -v

# Run with coverage
pytest tests/test_step_X.py --cov=jarvis

# Run specific test
pytest tests/test_step_X.py::test_function_name -v
```

### Step 5: Verify Completion
- ✅ All tests pass
- ✅ Code follows specification exactly
- ✅ No skipped tests
- ✅ No temporary code

---

## Test Structure

### File Organization

```
tests/
├── test_step_1.py      ← Tests for Step 1 (40+ test cases)
├── test_step_2.py      ← Tests for Step 2
├── test_step_4_1.py    ← Tests for Step 4.1
├── test_step_4_2.py    ← Tests for Step 4.2
└── fixtures/           ← Shared test fixtures
    └── sample_data.py
```

### Test Naming Conventions

✅ **GOOD**
```python
def test_cli_accepts_input():
    """Test that CLI accepts user input"""
    
def test_graph_add_node_creates_node():
    """Test that add_node creates a new node"""
    
def test_observer_receives_all_updates():
    """Test that observer receives all state updates"""
```

❌ **BAD**
```python
def test1():
    """???"""
    
def test_working():
    """Doesn't describe what it tests"""
    
def test_x():
    """Too vague"""
```

### Test Case Examples

From specification, you'll have test cases like:

```markdown
### Test Case 1: Basic CLI Input
- Input: "hello"
- Expected: Echo "hello"
- Status: Pass/Fail

### Test Case 2: Command Parsing
- Input: "list"
- Expected: List command executed
- Status: Pass/Fail
```

You implement this as:

```python
def test_cli_echoes_hello():
    cli = CLI()
    result = cli.process("hello")
    assert result == "hello"

def test_cli_parses_list_command():
    cli = CLI()
    result = cli.process("list")
    assert isinstance(result, list)
```

---

## Test Requirements by Step

### Step 1: Basic CLI
- **Tests**: 40+ test cases in `step_1_basic_cli.md`
- **Coverage**: User input, command echo, exit handling
- **File**: `tests/test_step_1.py`

### Step 2: Dependency Graph
- **Tests**: 35+ test cases in `step_2_graph.md`
- **Coverage**: Graph creation, node/edge operations, cycles
- **File**: `tests/test_step_2.py`

### Step 3: State Observers
- **Tests**: 30+ test cases in `step_3_observers.md`
- **Coverage**: Observer registration, state updates, notifications
- **File**: `tests/test_step_3.py`

### Step 4: Test Functions & Execution
- **Tests**: 40+ test cases (combined)
- **Coverage**: Utility functions, execution engine, chaining
- **Files**: `tests/test_step_4_1.py`, `tests/test_step_4_2.py`

---

## Code Coverage Expectations

### Minimum Coverage by Type

| Component | Minimum | Target |
|-----------|---------|--------|
| Unit tests | 80% | 95%+ |
| Integration tests | 60% | 85%+ |
| Edge cases | Required | Comprehensive |
| Error handling | Required | Comprehensive |

### Check Coverage

```bash
# Run with coverage report
pytest tests/test_step_X.py --cov=jarvis --cov-report=html

# View report
open htmlcov/index.html
```

---

## Test Execution Checklist

### Before Declaring Step Complete

- [ ] All tests written (from specification)
- [ ] All tests passing
- [ ] Code coverage acceptable (80%+ minimum)
- [ ] No skipped tests (`@pytest.skip`)
- [ ] No temporary/debug code
- [ ] All function implementations complete
- [ ] No commented-out code in tests
- [ ] Clear test names and docstrings

### Test Output Must Show

```
======================== test session starts =========================
collected 40 items

tests/test_step_1.py::test_cli_accepts_input PASSED
tests/test_step_1.py::test_cli_echoes_input PASSED
tests/test_step_1.py::test_cli_handles_exit PASSED
... (all tests pass)

======================== 40 passed in 2.34s ==========================
```

---

## Common Test Patterns

### Pattern 1: Function Testing

```python
def test_function_returns_expected_value():
    # Arrange
    input_data = "test input"
    expected = "expected output"
    
    # Act
    result = my_function(input_data)
    
    # Assert
    assert result == expected
```

### Pattern 2: Class Testing

```python
def test_class_initialization():
    obj = MyClass(param1="value1")
    assert obj.param1 == "value1"

def test_class_method_modifies_state():
    obj = MyClass()
    obj.add_item("item1")
    assert "item1" in obj.items
```

### Pattern 3: Exception Testing

```python
def test_function_raises_exception_on_invalid_input():
    with pytest.raises(ValueError):
        my_function(invalid_input)
```

### Pattern 4: Integration Testing

```python
def test_multiple_components_work_together():
    graph = Graph()
    observer = Observer()
    
    graph.add_observer(observer)
    graph.add_node("node1")
    
    assert observer.received_update
```

---

## Specification Document Structure

Each step has a specification file with:

1. **Overview** - What you're building
2. **Requirements** - What it should do
3. **Functions to Implement** - Exact signatures
4. **Test Cases** - 30-40+ test cases
5. **File Structure** - Where files go
6. **Example Usage** - How it's used

### Specification File Format

```markdown
# Step X: [Title]

## Overview
What you're building and why

## Files to Create/Modify
jarvis/module.py
tests/test_step_x.py

## Functions to Implement

### 1. function_name(param1: type, param2: type) -> return_type
Description of what it does

### Test Cases for function_name

#### Test 1: [Description]
- Input: [values]
- Expected Output: [result]
- Edge Case: [if applicable]

...40+ test cases...
```

---

## What NOT to Do

❌ **Skip tests** - Tests are MANDATORY, not optional  
❌ **Use `@pytest.skip`** - Every test must pass  
❌ **Leave commented code** - Delete it, commit is tracked  
❌ **Ignore failures** - Fix them, don't skip  
❌ **Modify tests** - Tests define requirements, not implementation  
❌ **Write code first** - ALWAYS write tests first  
❌ **Skip edge cases** - Test all cases in specification  
❌ **Leave debug prints** - Remove before finishing  

---

## Success Criteria

A step is complete when:

✅ **All tests pass**
```bash
pytest tests/test_step_X.py -v
# Shows: "X passed in Y.XXs"
```

✅ **All functions implemented**
- Every function from specification exists
- Every function passes its tests

✅ **No skipped tests**
- No `@pytest.skip` decorators
- No `pytest.skip()` calls
- 100% test execution

✅ **Good code quality**
- Clear function names
- Docstrings present
- No commented code
- No temporary variables

✅ **Full coverage**
- 80%+ code coverage minimum
- All branches tested
- Edge cases covered

---

## Troubleshooting

### Problem: Tests are failing

1. **Read the error message** - It tells you what's wrong
2. **Check the test** - Understand what it's testing
3. **Check your code** - Does it match specification?
4. **Debug** - Add print statements, use pdb
5. **Fix** - Modify code to pass test

### Problem: Missing test cases

1. **Review specification** - Have you written all test cases?
2. **Count them** - Should match specification count
3. **Run `pytest --collect-only`** - See all tests
4. **Add missing** - Write tests for all requirements

### Problem: Code coverage too low

1. **Run with coverage** - `pytest --cov=jarvis`
2. **Identify uncovered** - Which lines aren't tested?
3. **Write tests** - Add tests for uncovered code
4. **Verify** - Re-run coverage

---

## Related Documents

- **Specification files**: `step_X_*.md` in step folders
- **Code structure**: `JARVIS_FILE_TREE.md` in design repo
- **Requirements**: `REQUIREMENTS.md` in design repo
- **Examples**: `USE_CASES.md` in design repo

---

**Test-driven development ensures quality and correctness.**  
**Write tests first, implement second, verify everything works.**

**Last Updated**: January 9, 2026
