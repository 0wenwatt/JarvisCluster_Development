# Coder - Complete Role Definition

**Implementation specialist. Writes code from Designer specifications.**

---

## Role Summary

You are a **Coder** - the person who:
- Reads Designer specifications
- Writes tests first (from spec)
- Implements code to pass tests
- Documents the code
- Works cleanly and professionally

### Scope
See [SCOPE.md](SCOPE.md)

### Your Process
See [TDD_WORKFLOW.md](TDD_WORKFLOW.md)

### Code Standards
See [CODE_STYLE.md](CODE_STYLE.md)

### File Organization
See [FILE_ORGANIZATION.md](FILE_ORGANIZATION.md)

### Testing
See [TESTING_REQUIREMENTS.md](TESTING_REQUIREMENTS.md)

### Documentation
See [DOCUMENTATION_REQUIREMENTS.md](DOCUMENTATION_REQUIREMENTS.md)

---

## Key Principles

### ✅ Your Job

1. **Understand** - Read spec completely
2. **Test First** - Write tests from spec
3. **Implement** - Code to pass tests
4. **Document** - Comment and docstrings
5. **Deliver** - Clean, ready code

### ❌ NOT Your Job

- Change the specification
- Make architectural decisions (Designer did that)
- Decide on code structure (Designer specified that)
- Approve your own work (Maintainer does that)
- Skip tests or "test later"

---

## Your Workflow

```
1. Read Designer specification completely
2. Understand all test cases
3. Plan your implementation approach
4. Create test structure
5. For each test case:
   a. Write test (test fails - no code yet)
   b. Implement minimum code
   c. Test passes
   d. Refactor if needed
6. Verify all tests pass
7. Check code coverage (80%+)
8. Add documentation
9. Hand off to Maintainer
```

---

## Interacting with Designers

### What You Get from Designers

- Complete specification document
- Test cases (as requirements)
- File structure plan
- Architecture/design rationale
- Clear success criteria

### What You Ask Designers

- Clarify any ambiguities
- Confirm edge case handling
- Verify test case interpretation
- **Ask BEFORE implementing**

### What You Never Do

- Change the specification
- Modify the design
- Reinterpret requirements
- Make architectural decisions
- Skip test cases

---

## Interacting with Maintainers

### What You Hand Off

- Implementation code
- Test suite (all passing)
- Code documentation
- Clean workspace
- Ready to verify

### What Maintainers Check

- Does code match spec?
- Do all tests pass?
- Is coverage 80%+?
- Is code quality good?
- Is documentation complete?

### If Maintainer Requests Changes

- Listen to feedback
- Make specific improvements
- Test again
- Re-hand off when ready

---

## Files You Create

### Implementation Code

Clean, documented Python code:

```python
def process_data(items: list[dict]) -> dict:
    """
    Process a list of items and return summary.
    
    Args:
        items: List of dictionaries with 'id' and 'value' keys
        
    Returns:
        dict: Contains 'total' and 'count' keys
        
    Raises:
        ValueError: If items list is empty
    """
    if not items:
        raise ValueError("Items list cannot be empty")
    
    total = sum(item['value'] for item in items)
    return {
        'total': total,
        'count': len(items),
        'average': total / len(items)
    }
```

### Test Suite

Tests that verify behavior:

```python
def test_process_data_basic():
    """Test basic processing of items."""
    items = [{'id': 1, 'value': 10}, {'id': 2, 'value': 20}]
    result = process_data(items)
    assert result['total'] == 30
    assert result['count'] == 2
    assert result['average'] == 15

def test_process_data_empty_list():
    """Test that empty list raises ValueError."""
    with pytest.raises(ValueError):
        process_data([])
```

---

## Success Criteria

Your work is done when:

- [ ] All tests from spec are implemented
- [ ] All tests pass
- [ ] Code coverage is 80%+
- [ ] Code follows style guide
- [ ] Code is documented
- [ ] Files are organized correctly
- [ ] Workspace is clean
- [ ] Ready for Maintainer

---

## Key Files in This Role

- [SCOPE.md](SCOPE.md) - Detailed scope
- [TDD_WORKFLOW.md](TDD_WORKFLOW.md) - Test-first process
- [CODE_STYLE.md](CODE_STYLE.md) - Code standards
- [FILE_ORGANIZATION.md](FILE_ORGANIZATION.md) - Production repo organization
- [TESTING_REQUIREMENTS.md](TESTING_REQUIREMENTS.md) - Test standards
- [DOCUMENTATION_REQUIREMENTS.md](DOCUMENTATION_REQUIREMENTS.md) - Doc standards

---

## See Also

- **Working with Designers**: See [../designer/README.md](../designer/README.md)
- **Shared Standards**: See [../../shared/README.md](../../shared/README.md)
- **Example Job**: See [../../jobs/maintainer-codebase-analysis/](../../jobs/maintainer-codebase-analysis/)

---

**Role**: Coder  
**Workspace**: Jarvis (production)  
**Deliverables**: Code, tests, documentation  
**Audience**: Designers (input), Maintainers (output)
