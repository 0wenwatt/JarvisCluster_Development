# Codebase Analysis Job - Specification

**Desired state - what you're comparing against.**

---

## Specification: Desired State

This is what the codebase SHOULD have. You're comparing the actual code to this specification.

---

## Directory Structure

### Desired Organization

```
Jarvis/
├── .github/                    (GitHub configuration)
│   └── workflows/             (CI/CD workflows)
├── src/jarvis/                (Source code)
│   ├── __init__.py
│   ├── core/                  (Core modules)
│   ├── utils/                 (Utility modules)
│   ├── services/              (Service modules)
│   └── models/                (Data models)
├── tests/                     (Test files)
│   ├── __init__.py
│   ├── unit/                  (Unit tests)
│   ├── integration/           (Integration tests)
│   └── fixtures/              (Test data)
├── docs/                      (Documentation)
│   ├── README.md
│   ├── installation.md
│   ├── usage.md
│   └── api.md
├── README.md                  (Project readme)
├── CHANGELOG.md               (Version history)
├── LICENSE                    (License file)
├── requirements.txt           (Python dependencies)
├── pyproject.toml            (Project config)
├── pytest.ini                (Test configuration)
├── .gitignore                (Git ignore rules)
├── .env.example              (Environment template)
└── setup.py                  (Setup configuration)
```

---

## Code Standards

### Python Files

#### Organization
- [ ] All code in `src/jarvis/` (not root)
- [ ] Tests in `tests/` (not in source)
- [ ] Documentation in `docs/` (not scattered)
- [ ] Config files in root only

#### Naming Conventions
- [ ] Modules: `lowercase_with_underscores.py`
- [ ] Classes: `PascalCase`
- [ ] Functions: `lowercase_with_underscores()`
- [ ] Constants: `UPPERCASE_WITH_UNDERSCORES`
- [ ] Private methods: `_prefixed_with_underscore()`

#### Code Quality
- [ ] No debug print statements
- [ ] No commented-out code
- [ ] No temporary variables
- [ ] No TODO comments without context
- [ ] Follows PEP 8 style guide
- [ ] Lines max 100 characters
- [ ] 2-4 space indentation (consistent)

#### Documentation
- [ ] Module docstrings (what module does)
- [ ] Class docstrings (what class does)
- [ ] Function docstrings (what function does, params, return)
- [ ] Complex logic documented
- [ ] Type hints present

### Example Good Function

```python
def calculate_distance(point1: tuple, point2: tuple) -> float:
    """
    Calculate Euclidean distance between two points.
    
    Args:
        point1: (x, y) tuple
        point2: (x, y) tuple
        
    Returns:
        float: Distance between points
        
    Raises:
        ValueError: If points invalid
    """
    # Implementation...
```

---

## Test Requirements

### Test Files
- [ ] Named `test_*.py` (not `*_test.py`)
- [ ] Located in `tests/` directory
- [ ] Organized by module
- [ ] Clear test names: `test_<function>_<scenario>()`

### Test Content
- [ ] All public functions have tests
- [ ] All critical paths tested
- [ ] Tests pass 100%
- [ ] Code coverage ≥ 80%
- [ ] No skipped tests
- [ ] Fixtures used for common setup

### Example Good Test

```python
def test_calculate_distance_basic():
    """Test basic distance calculation."""
    result = calculate_distance((0, 0), (3, 4))
    assert result == 5.0

def test_calculate_distance_invalid_input():
    """Test that invalid input raises ValueError."""
    with pytest.raises(ValueError):
        calculate_distance("invalid", (1, 1))
```

### Running Tests
```bash
# All tests pass
pytest tests/ -v

# Coverage >= 80%
pytest tests/ --cov=src/jarvis --cov-report=term-missing
```

---

## Dependencies

### requirements.txt / pyproject.toml
- [ ] All dependencies pinned to specific versions
- [ ] No duplicate entries
- [ ] No unused dependencies
- [ ] No conflicting versions
- [ ] Development dependencies marked (dev, test, etc.)

### Example

```
# requirements.txt
pytest==7.4.0
requests==2.31.0
python-dotenv==1.0.0

# Or in pyproject.toml
[project]
dependencies = [
    "requests>=2.31.0,<3.0",
    "python-dotenv>=1.0.0",
]

[project.optional-dependencies]
dev = ["pytest>=7.4.0"]
```

---

## Documentation

### README.md
- [ ] Project description
- [ ] Installation instructions
- [ ] Quick start / usage example
- [ ] Configuration details
- [ ] Contributing guidelines
- [ ] License information

### docs/ Folder
- [ ] Installation guide
- [ ] API documentation
- [ ] Usage examples
- [ ] Troubleshooting
- [ ] Architecture overview (if complex)

### Code Comments
- [ ] Complex algorithms explained
- [ ] Non-obvious decisions documented
- [ ] Edge cases noted
- [ ] Assumptions stated

---

## Configuration

### .gitignore
- [ ] Virtual environments excluded
- [ ] Pycache excluded
- [ ] IDE folders excluded
- [ ] .env files excluded
- [ ] Build artifacts excluded
- [ ] OS temp files excluded

### .env.example
- [ ] Template for environment variables
- [ ] Shows required variables
- [ ] Shows defaults

### pyproject.toml
- [ ] Project metadata
- [ ] Dependencies listed
- [ ] Build configuration
- [ ] Tool configurations (pytest, etc.)

---

## Version Control

### Git Configuration
- [ ] .gitignore properly configured
- [ ] No large files checked in
- [ ] No binary files in repo
- [ ] No sensitive data in repo
- [ ] Clear commit history

---

## Architecture Quality

### Module Organization
- [ ] Clear separation of concerns
- [ ] No circular dependencies
- [ ] Logical grouping of functionality
- [ ] Reusable components

### Dependencies
- [ ] Minimal external dependencies
- [ ] No version conflicts
- [ ] Well-maintained packages only

### Design Patterns
- [ ] Consistent design patterns
- [ ] No code duplication (DRY)
- [ ] SOLID principles followed where applicable

---

## Issues Severity Guide

Use this to classify issues you find:

### 🔴 Critical
- Code doesn't run
- Tests fail
- Missing core files
- Security issues

### 🟠 High
- Low test coverage
- Undocumented functions
- Style violations
- Missing documentation

### 🟡 Medium
- Optional improvements
- Nice-to-have features
- Future enhancements

### 🟢 Low
- Preferences
- Minor style notes
- Future consideration

---

## Success Criteria

When analyzing, you're looking for:

✅ **Passing**:
- Code runs without errors
- All tests pass
- Coverage >= 80%
- Code follows style guide
- All modules documented
- Files organized correctly
- Dependencies clean
- No debug code

❌ **Issues**:
- Code doesn't run
- Tests fail
- Coverage < 80%
- Style violations
- Missing documentation
- Disorganized files
- Conflicting dependencies
- Debug/temp code present

---

## Comparison Approach

For each area, compare:

```
Desired State
    ↓
Actual State
    ↓
Match? 
    ├─ YES → Note as passing
    └─ NO  → Document issue
```

---

**Specification**: Target state for codebase analysis  
**Use**: Compare actual code to this specification  
**For**: Identifying all discrepancies
