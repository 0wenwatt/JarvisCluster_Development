# Folder Structure Design for Jarvis v0.1

**Purpose**: This document describes the **target folder structure** for the final Jarvis codebase (in the actual development repo).

---

## Overview

Jarvis uses a **module-based structure** where each logical component is a folder containing:
- Implementation file(s)
- Metadata file
- Test file
- (Later) Additional supporting files as needed

**Principle**: Each folder is self-contained and represents a single concern.

---

## v0.1 Target Structure

```
jarvis/                           # Main package
│
├── __init__.py
│
├── cli/                          # Step 1: Command-line interface
│   ├── cli.py
│   ├── cli.metadata.json
│   └── cli_Test.py
│
├── graph/                        # Step 2: Core graph data structure
│   ├── graph.py
│   ├── graph.metadata.json
│   └── graph_Test.py
│
├── observers/                    # Steps 3 & 3.2: File and function observation
│   ├── observers.py
│   ├── observers.metadata.json
│   └── observers_Test.py
│
├── test_functions/               # Step 4.1: Test/utility functions
│   ├── test_functions.py
│   ├── test_functions.metadata.json
│   └── test_functions_Test.py
│
├── execution/                    # Step 4.2: Execution engine
│   ├── execution.py
│   ├── execution.metadata.json
│   └── execution_Test.py
│
└── Diagnostics/                  # Testing and self-diagnostics
    ├── test_suit.py
    └── (expansion: test_diagnostics.py, performance_checker.py, etc.)



---

## Folder Contents Explained

### Each Module Folder

**Standard files** (one per module):

- **`module_name.py`** — Implementation code
- **`module_name.metadata.json`** — Metadata (see Metadata_Design/)
- **`module_name_Test.py`** — Test code for this module

**Rules**:
- One main Python file per folder (keep focused)
- Tests are in the same folder (easy to find)
- Metadata lives alongside the implementation

### Diagnostics Folder

- **`test_suit.py`** — Master test runner (runs all tests in order)
- (Future) Additional diagnostic/testing utilities

### tests/ Folder

- Shared test data (example folder structures, graph files, etc.)
- Not implementation code; purely test fixtures

---

## Why This Structure?

1. **Self-contained modules** — Each folder is independent
2. **Tests with code** — Test file immediately visible next to implementation
3. **Metadata centralized** — All metadata about a module in one JSON file
4. **Easy to navigate** — Clear naming convention (module_name, module_name_Test, module_name.metadata.json)
5. **Scalable** — New modules follow same pattern

---

## Evolution Beyond v0.1

As Jarvis grows, this structure will expand:

- **More modules** — graph, cli, execution, etc. each get submodules
- **Utility functions** — Shared helpers in `utils/`
- **Configuration** — Config files in `config/`
- **API layer** — REST/gRPC endpoints in `api/`
- **Performance** — Benchmarking in `perf/`

But the basic principle remains: **module folder → code + test + metadata**.

---

## Summary

| Item | Location | Purpose |
|------|----------|---------|
| Implementation | `module_name/module_name.py` | Actual code |
| Tests | `module_name/module_name_Test.py` | Test code (always alongside implementation) |
| Metadata | `module_name/module_name.metadata.json` | Module info, test status, Copilot notes |
| Test Data | `tests/` | Example graphs, folders, fixtures |
| Diagnostics | `Diagnostics/test_suit.py` | Run all tests, health checks |

