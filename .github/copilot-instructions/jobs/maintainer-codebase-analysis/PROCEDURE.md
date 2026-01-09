# Codebase Analysis Job - Procedure

**Step-by-step how to analyze the codebase.**

---

## Overview

Follow this procedure to systematically analyze the codebase and identify all discrepancies.

---

## Phase 1: Setup (15 minutes)

### Step 1: Create Workspace
```bash
# Create workspace folder
mkdir Agent_Workspace
cd Agent_Workspace

# Create progress tracking file
cat > README.md << 'EOF'
# Codebase Analysis - Progress

**Status**: In Progress  
**Started**: [TODAY'S DATE]

## Checklist
- [ ] File organization check
- [ ] Code quality check
- [ ] Test verification
- [ ] Documentation review
- [ ] Dependencies check
- [ ] Architecture analysis
- [ ] Findings logged
- [ ] Report created
- [ ] Archive complete

## Progress
Starting analysis...

## Current Work
Reviewing file organization...

## Issues Found So Far
(Updated as I analyze)

## Notes
(Additional notes)
EOF
```

### Step 2: Prepare FINDINGS.md
```bash
cat > FINDINGS.md << 'EOF'
# Codebase Analysis - Findings

**Date**: [TODAY'S DATE]  
**Status**: In Progress  
**Result**: Analyzing...

## Summary
Analyzing Jarvis codebase against desired state specification.

## Issues by Severity
- 🔴 Critical: (TBD)
- 🟠 High: (TBD)
- 🟡 Medium: (TBD)
- 🟢 Low: (TBD)

## Issues Found
(Will add as I discover them)
EOF
```

### Step 3: Review Specification
- Read [SPECIFICATION.md](SPECIFICATION.md) completely
- Understand desired state
- Note all checkpoints

---

## Phase 2: File Organization (30 minutes)

### Check: Directory Structure

For each folder in specification, verify:

```
Desired: src/jarvis/
Actual: src/jarvis/ exists?
  ✓ YES  → Check contents
  ✗ NO   → Issue found

Desired: tests/
Actual: tests/ exists?
  ✓ YES  → Check contents
  ✗ NO   → Issue found
```

### Check: File Placement

For each file type:

| File Type | Should Be In | Actual Location | Status |
|-----------|-------------|-----------------|--------|
| Source code | `src/jarvis/` | ? | OK / Issue |
| Tests | `tests/` | ? | OK / Issue |
| Docs | `docs/` | ? | OK / Issue |
| Config | Root | ? | OK / Issue |

### Check: File Naming

- [ ] Python files: `lowercase_with_underscores.py`
- [ ] Test files: `test_*.py`
- [ ] No files with spaces in name
- [ ] No files with capital letters (except docs)

### Log Issues Found

Add to FINDINGS.md:

```markdown
## File Organization

**Issue #1**: Missing directory structure
- Location: src/jarvis/
- Severity: Critical
- Details: src/jarvis/core/ doesn't exist
- Evidence: Directory listing shows core missing
- Recommendation: Create src/jarvis/core/ directory
```

Update README.md:
```markdown
## Progress
- [x] File organization check
  - Found 3 issues (1 critical, 2 high)
```

---

## Phase 3: Code Quality (1-2 hours)

### Step 1: Review Style Violations

```bash
# Check Python style (if available)
cd [jarvis-repo]
pylint src/jarvis/ --exit-zero > analysis.txt
# OR
flake8 src/jarvis/ > analysis.txt
# OR just review manually
```

For each Python file in `src/jarvis/`:
- [ ] No debug print statements
- [ ] No commented-out code
- [ ] No temp variables
- [ ] Follows naming conventions
- [ ] Max line length appropriate

### Step 2: Check Documentation

For each Python file:
```python
def my_function(x: int) -> str:
    # Does this have a docstring?
    # Does it explain: what, params, return?
    pass
```

For each class:
```python
class MyClass:
    # Does this have a docstring?
    # Does it explain purpose?
    pass
```

### Step 3: Review Code Organization

For each module:
- [ ] Clear separation of concerns
- [ ] Logical grouping
- [ ] No circular dependencies
- [ ] Helper functions properly marked (`_private`)

### Log Issues Found

Add to FINDINGS.md:

```markdown
## Code Quality

**Issue #2**: Missing function docstring
- Location: src/jarvis/utils.py, line 42 (function `process_data`)
- Severity: High
- Details: Function `process_data()` has no docstring explaining parameters or return
- Evidence: Function definition on line 42 has no docstring
- Recommendation: Add docstring explaining function purpose, parameters, return value

**Issue #3**: Debug print statement left in code
- Location: src/jarvis/core/engine.py, line 156
- Severity: High
- Details: print("DEBUG: processing...") left in production code
- Evidence: Line 156 contains print statement
- Recommendation: Remove print statement or convert to logging call
```

Update README.md with progress.

---

## Phase 4: Test Verification (30 minutes)

### Step 1: Run Test Suite

```bash
cd [jarvis-repo]
pytest tests/ -v
```

Document:
- [ ] Do all tests pass?
- [ ] How many tests?
- [ ] Which tests fail (if any)?

### Step 2: Check Coverage

```bash
pytest tests/ --cov=src/jarvis --cov-report=term-missing
```

Document:
- [ ] Overall coverage percentage
- [ ] Which files have low coverage
- [ ] Which lines not covered

### Step 3: Verify Test Quality

For test files in `tests/`:
- [ ] Test names follow `test_<function>_<scenario>`
- [ ] Tests are organized by module
- [ ] No skipped tests
- [ ] Good use of fixtures

### Log Issues Found

Add to FINDINGS.md:

```markdown
## Testing

**Issue #4**: Low test coverage
- Location: src/jarvis/
- Severity: High
- Details: Overall coverage is 62%, but spec requires 80%+
- Evidence: `pytest --cov` shows 62% coverage
- Recommendation: Add tests for uncovered lines (see report for details)

**Issue #5**: Test skipped
- Location: tests/unit/test_engine.py, line 45
- Severity: High
- Details: `test_engine_restart()` is marked @pytest.mark.skip
- Evidence: Decorator on line 44
- Recommendation: Fix underlying issue and remove skip
```

Update README.md with progress.

---

## Phase 5: Documentation Review (30 minutes)

### Step 1: Check README.md

Does README.md have:
- [ ] Project description
- [ ] Installation instructions
- [ ] Quick start example
- [ ] Configuration details
- [ ] License info

### Step 2: Check docs/ Folder

Does docs/ have:
- [ ] installation.md
- [ ] usage.md
- [ ] api.md (or similar)
- [ ] README.md

### Step 3: Check Code Comments

Review critical sections:
- [ ] Complex algorithms explained
- [ ] Non-obvious decisions documented
- [ ] Edge cases noted

### Log Issues Found

Add to FINDINGS.md:

```markdown
## Documentation

**Issue #6**: Missing API documentation
- Location: docs/
- Severity: Medium
- Details: No API documentation for public functions in core module
- Evidence: docs/ folder doesn't contain api.md
- Recommendation: Create docs/api.md with API reference

**Issue #7**: README installation section incomplete
- Location: README.md, Installation section
- Severity: Medium
- Details: Instructions don't cover Python version requirements or dependencies
- Evidence: README.md line X-Y
- Recommendation: Add Python version requirement and dependency installation steps
```

Update README.md with progress.

---

## Phase 6: Dependencies Check (15 minutes)

### Step 1: Review requirements.txt

```bash
cat requirements.txt
```

Check:
- [ ] All dependencies pinned to versions
- [ ] No duplicates
- [ ] No conflicting versions

### Step 2: Check for Unused

For each dependency:
- Is it actually imported anywhere?
- Do we use it?

### Log Issues Found

Add to FINDINGS.md:

```markdown
## Dependencies

**Issue #8**: Dependency version not pinned
- Location: requirements.txt, line 3
- Severity: Medium
- Details: `requests` listed as `requests>=2.25.0` without upper bound
- Evidence: requirements.txt shows `requests>=2.25.0`
- Recommendation: Pin to specific version `requests==2.31.0`

**Issue #9**: Unused dependency
- Location: requirements.txt, line 7
- Severity: Low
- Details: `colorama` listed but never imported in codebase
- Evidence: Grep search shows no imports of colorama
- Recommendation: Remove from requirements.txt if not needed
```

Update README.md with progress.

---

## Phase 7: Architecture Analysis (30 minutes)

### Review Module Organization

For each module in `src/jarvis/`:
- [ ] Clear purpose
- [ ] Logical grouping
- [ ] Appropriate dependencies
- [ ] No circular imports

### Check Design Patterns

- Are patterns used consistently?
- Is code DRY (not repeated)?
- Is code reusable?

### Log Issues Found

Add to FINDINGS.md:

```markdown
## Architecture

**Issue #10**: Code duplication
- Location: src/jarvis/utils.py and src/jarvis/services/data.py
- Severity: Medium
- Details: Function `parse_config()` implemented identically in two places
- Evidence: Both files have identical 15-line function
- Recommendation: Move to shared utils and import in both places
```

---

## Phase 8: Consolidate Findings (1 hour)

### Review All Issues

Go through FINDINGS.md and:
- [ ] All issues documented
- [ ] Categorized properly
- [ ] Severity assigned correctly
- [ ] Evidence clear
- [ ] Recommendations actionable

### Organize by Category

Make sure organized like:
```markdown
## File Organization (N issues)
- Issue 1
- Issue 2

## Code Quality (N issues)
- Issue 3
- Issue 4

## Testing (N issues)
- Issue 5
```

### Count by Severity

Count and update:
- 🔴 Critical: X
- 🟠 High: Y
- 🟡 Medium: Z
- 🟢 Low: W

---

## Phase 9: Create Report (30 minutes)

Create `REPORT.md`:

```markdown
# Codebase Analysis Report

**Date**: [TODAY]  
**Status**: Complete  
**Result**: Issues found - see below

## Summary
Analysis of Jarvis codebase against specification complete. Found [N] issues across [categories].

**Decision**: Recommend fixes before proceeding

## Issues by Severity

**🔴 Critical ([N])**
1. Issue 1
2. Issue 2

**🟠 High ([N])**
1. Issue 3
2. Issue 4

**🟡 Medium ([N])**
1. Issue 5

**🟢 Low ([N])**
1. Issue 6

## Issues by Category

### File Organization
[Issues...]

### Code Quality
[Issues...]

### Testing
[Issues...]

### Documentation
[Issues...]

### Dependencies
[Issues...]

### Architecture
[Issues...]

## Positive Findings

What's working well:
- [Good thing 1]
- [Good thing 2]

## Recommendations

**Priority 1 (Critical)**
- Fix [issue 1]
- Fix [issue 2]

**Priority 2 (High)**
- Fix [issue 3]
- ...

## Next Steps

1. Coder fixes issues from Critical list
2. Coder fixes issues from High list
3. Coder adds tests for issues found
4. Maintainer re-checks conformance
5. Loop until all issues resolved
```

---

## Phase 10: Archive & Close (15 minutes)

### Finalize Workspace

In `Agent_Workspace/README.md`, update:
```markdown
**Status**: Complete  
**Finished**: [TODAY]

## Checklist
- [x] File organization check
- [x] Code quality check
- [x] Test verification
- [x] Documentation review
- [x] Dependencies check
- [x] Architecture analysis
- [x] Findings logged
- [x] Report created
- [ ] Archive complete

## Final Summary
Found 10 issues: 2 critical, 3 high, 4 medium, 1 low
See REPORT.md for details.
```

### Archive Workspace

Copy to Development_Logs:
```bash
mkdir -p Development_Logs/maintainer-codebase-analysis
cp Agent_Workspace/* Development_Logs/maintainer-codebase-analysis/
```

### Clean Up

```bash
# Remove Agent_Workspace
rm -r Agent_Workspace
```

### Notify

Inform Owen:
```
Codebase analysis complete.

Found:
- 2 critical issues (must fix)
- 3 high issues (should fix)
- 4 medium issues (nice to fix)
- 1 low issue

See Development_Logs/maintainer-codebase-analysis/REPORT.md for details.
```

---

## Checklist: Completion

Before marking complete:

- [ ] All 6 phases completed
- [ ] FINDINGS.md has all issues
- [ ] Issues categorized
- [ ] Severity assigned
- [ ] Evidence provided
- [ ] Recommendations given
- [ ] REPORT.md created
- [ ] Workspace archived
- [ ] Owen notified

---

**Procedure**: Step-by-step analysis workflow  
**Duration**: ~4-5 hours  
**Output**: Detailed findings and report
