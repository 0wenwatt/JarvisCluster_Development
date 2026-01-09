---
applyTo: "jarvis/**,tests/**"
---

# Step 9: Full Interoperability Tests

## Task Overview

Test everything comprehensively. No edge cases left behind. Ensure all components work together perfectly in realistic scenarios.

This step is pure testing and validation — no new code, just comprehensive test coverage of all v0.1 + v0.2 functionality.

**Key Point**: If it's not tested, it doesn't work. Test all combinations.

---

## What You'll Create

### Files to Add/Modify

- `tests/test_step_9_interop.py` — NEW (50+ comprehensive tests)
- `tests/fixtures/` — NEW (test projects: small, medium, large)
- Test documentation and reports

### What's Being Tested

ALL of v0.1 + v0.2:
- CLI (Step 1)
- Graph (Step 2)
- Observation (Step 3)
- Execution (Step 4)
- Folder→Graph conversion (Step 5)
- Functions→Graph conversion (Step 6)
- Metadata management (Step 7)
- Integration workflow (Step 8)

---

## Test Specifications

Write tests FIRST. Test everything.

### Test Cases (50+ total)

**Core Integration Tests**:
- [ ] `test_workflow_end_to_end_single_file` — Single file analysis
- [ ] `test_workflow_end_to_end_small_project` — 10 files, 20 functions
- [ ] `test_workflow_end_to_end_medium_project` — 50 files, 100 functions
- [ ] `test_workflow_end_to_end_large_project` — 200 files, 500+ functions
- [ ] `test_graph_consistency_after_full_analysis` — Graph integrity
- [ ] `test_metadata_consistency_all_nodes` — All nodes have metadata if files exist
- [ ] `test_execution_discovers_all_functions` — All functions discoverable
- [ ] `test_query_performance_large_graph` — Queries < 100ms on large data

**Component Interop Tests**:
- [ ] `test_folder_to_graph_with_function_observation` — Both converters work
- [ ] `test_metadata_attaches_to_folder_nodes` — Metadata on folders
- [ ] `test_metadata_attaches_to_function_nodes` — Metadata on functions
- [ ] `test_graph_serialization_preserves_all_data` — Save/load works
- [ ] `test_cli_all_commands_sequence` — All commands work in sequence
- [ ] `test_query_on_rich_graph` — Queries on full graph

**Scenario Tests** (Realistic workflows):
- [ ] `test_scenario_analyze_python_project` — Real Python repo
- [ ] `test_scenario_find_deprecated_functions` — Query + report
- [ ] `test_scenario_execute_discovered_function` — Observe → Execute chain
- [ ] `test_scenario_update_code_and_reanalyze` — Code changes detected
- [ ] `test_scenario_add_metadata_and_query` — Manual metadata → query
- [ ] `test_scenario_large_monorepo_multiple_modules` — Monorepo analysis

**Error Handling Tests**:
- [ ] `test_missing_files_graceful_recovery` — Deleted files handled
- [ ] `test_permission_errors_dont_crash` — Permission denied handled
- [ ] `test_syntax_errors_in_code_handled` — Bad Python code handled
- [ ] `test_circular_dependencies_handled` — Cycles don't break graph
- [ ] `test_duplicate_nodes_prevented` — No duplicate nodes created
- [ ] `test_invalid_metadata_handled` — Bad metadata files handled
- [ ] `test_concurrent_observations_safe` — Thread safety (if applicable)
- [ ] `test_very_deep_folder_hierarchies` — 50+ level deep folders
- [ ] `test_very_large_files_handled` — 10000+ line files

**Performance Tests**:
- [ ] `test_performance_analyze_1000_files` — Scalability
- [ ] `test_performance_query_500_function_graph` — Query speed
- [ ] `test_performance_metadata_attach_1000_nodes` — Metadata application speed
- [ ] `test_performance_execution_chain_100_functions` — Execution chain speed

**Data Integrity Tests**:
- [ ] `test_folder_structure_preserved_in_graph` — All folders and hierarchy
- [ ] `test_function_signatures_preserved_in_graph` — Parameters, returns
- [ ] `test_metadata_values_preserved_in_save_load` — Metadata survives round-trip
- [ ] `test_execution_results_correct` — Functions return right values
- [ ] `test_graph_edges_correct` — Edges connect right nodes

Write ALL tests in `tests/test_step_9_interop.py`.

---

## Development Rules

**IMPORTANT**: Read `DEVELOPMENT_RULES.md` in the repo root. All rules apply here.

### Folder Structure

```
tests/
├── test_step_9_interop.py           ← NEW (50+ tests)
├── fixtures/
│   ├── small_project/               ← NEW (test fixture)
│   ├── medium_project/              ← NEW (test fixture)
│   └── large_project/               ← NEW (test fixture)
└── (existing tests)
```

### File Creation Rules

✅ **CAN DO** (no permission needed):
- Create `tests/test_step_9_interop.py`
- Create test fixtures in `/tests/fixtures/`
- Create test projects

❌ **CANNOT DO**:
- Create files in repository root
- Create folders in root without permission

### Code Rules

Same as other test files:
- **Type hints**: All functions must have type hints
- **Docstrings**: All functions must have docstrings
- **Line length**: Max 100 characters
- **Assertions**: Clear, specific
- **No skipping**: No `@pytest.mark.skip`

---

## Test Fixtures (Test Projects)

Create 3 realistic test projects:

### Small Project Fixture

```
tests/fixtures/small_project/
├── .metadata.json
├── module.py                 ← 2 simple functions
├── helper.py                 ← 1 function
├── helper.py.metadata.json
├── tests/
│   ├── .metadata.json
│   └── test_module.py       ← 2 test functions
└── tests/.metadata.json
```

Contents:
```python
# module.py
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def greet(name: str) -> str:
    """Greet a person."""
    return f"Hello, {name}"
```

### Medium Project Fixture

```
tests/fixtures/medium_project/
├── .metadata.json
├── src/
│   ├── .metadata.json
│   ├── core.py              ← 10 functions
│   ├── utils.py             ← 10 functions
│   ├── core.py.metadata.json
│   └── utils.py.metadata.json
├── tests/
│   ├── .metadata.json
│   ├── test_core.py         ← 15 test functions
│   ├── test_utils.py        ← 15 test functions
│   └── conftest.py          ← fixtures
└── requirements.txt
```

### Large Project Fixture

```
tests/fixtures/large_project/
├── .metadata.json
├── src/
│   ├── .metadata.json
│   ├── module1/             ← 50 functions
│   │   ├── .metadata.json
│   │   ├── main.py
│   │   ├── utils.py
│   │   └── helpers.py
│   ├── module2/             ← 50 functions
│   ├── module3/             ← 50 functions
│   └── ...
├── tests/
│   ├── .metadata.json
│   ├── test_module1.py      ← 100+ tests
│   ├── test_module2.py
│   ├── test_module3.py
│   └── conftest.py
├── docs/
│   └── README.md
└── .metadata.json
```

---

## Implementation Workflow

### Step 1: Create Test Fixtures

Create realistic test projects in `tests/fixtures/`:

```bash
tests/fixtures/
├── small_project/
│   ├── .metadata.json
│   ├── module.py
│   ├── helper.py
│   └── tests/
│       └── test_module.py
├── medium_project/
│   └── (20-30 files, 100+ functions)
└── large_project/
    └── (100+ files, 500+ functions)
```

Each fixture should:
- Have real folder structure
- Have real Python files with real functions
- Have METADATA files
- Be representative of real projects

### Step 2: Write All Tests

Create `tests/test_step_9_interop.py`:

```python
import pytest
import tempfile
from pathlib import Path
from jarvis.graph import Graph
from jarvis.integration import JarvisWorkflow
from jarvis.cli import JarvisCLI

@pytest.fixture
def small_project():
    """Use small_project fixture."""
    return Path(__file__).parent / "fixtures" / "small_project"

def test_workflow_end_to_end_small_project(small_project):
    """Complete workflow on small project."""
    # Arrange
    workflow = JarvisWorkflow()
    graph = Graph()
    
    # Act
    summary = workflow.analyze(str(small_project), graph)
    
    # Assert
    assert summary["folders"] > 0
    assert summary["functions"] >= 3
    assert len(graph.nodes) > 0

def test_metadata_consistency_all_nodes(small_project):
    """All nodes should have metadata if .metadata.json exists."""
    # Arrange
    workflow = JarvisWorkflow()
    graph = Graph()
    
    # Act
    workflow.analyze(str(small_project), graph)
    
    # Assert
    # Check that nodes with metadata files are enriched
    module_nodes = [n for n in graph.nodes if "helper.py" in n.id]
    for node in module_nodes:
        assert hasattr(node, 'metadata') or node in unobserved_nodes

def test_query_performance_large_graph(large_project):
    """Query on large graph should complete in < 100ms."""
    import time
    
    # Arrange
    workflow = JarvisWorkflow()
    graph = Graph()
    workflow.analyze(str(large_project), graph)
    
    # Act
    start = time.time()
    results = workflow.query(graph, "status:active")
    elapsed = (time.time() - start) * 1000  # ms
    
    # Assert
    assert elapsed < 100, f"Query took {elapsed}ms"
```

### Step 3: Run All Tests

```bash
pytest tests/test_step_9_interop.py -v --tb=short
```

All 50+ tests should pass.

### Step 4: Create Test Report

Document results:

```markdown
# Step 9 Test Report

## Test Execution Summary

- **Total Tests**: 50+
- **Passed**: 50+
- **Failed**: 0
- **Skipped**: 0
- **Duration**: ~30 seconds

## Test Results by Category

### Core Integration Tests (8 tests)
✅ All passed
- Small project analysis
- Medium project analysis
- Large project analysis
- Graph consistency
- Metadata consistency
- Function discovery
- Query performance

### Component Interop Tests (6 tests)
✅ All passed
- Folder + function observation
- Metadata attachment
- Graph serialization
- CLI command sequences
- Rich graph queries

### Scenario Tests (6 tests)
✅ All passed
- Real Python project
- Deprecated function finding
- Execution from discovery
- Code change detection
- Metadata + query
- Monorepo analysis

### Error Handling Tests (9 tests)
✅ All passed
- Missing files
- Permission errors
- Syntax errors
- Circular dependencies
- Duplicate prevention
- Invalid metadata
- Deep hierarchies
- Large files

### Performance Tests (4 tests)
✅ All passed
- 1000 files: 2.3 seconds
- 500 function graph query: 45ms
- 1000 node metadata: 1.2 seconds
- 100 function execution chain: 120ms

### Data Integrity Tests (5 tests)
✅ All passed
- Folder structure preserved
- Function signatures preserved
- Metadata round-trip
- Execution correctness
- Graph edge correctness

## Conclusion

✅ **All v0.2 functionality working correctly**

Ready for production deployment.
```

---

## Deliverables Checklist

- [ ] `tests/test_step_9_interop.py` created (50+ tests)
- [ ] 3 test fixtures created:
  - [ ] `tests/fixtures/small_project/`
  - [ ] `tests/fixtures/medium_project/`
  - [ ] `tests/fixtures/large_project/`
- [ ] All 50+ tests pass
- [ ] Performance tests pass (queries < 100ms)
- [ ] Error handling tests pass
- [ ] Test report created and documented
- [ ] No flaky tests
- [ ] All v0.1 & v0.2 modules tested
- [ ] `Agent_Workspace/Progress.md` documented

---

## Agent_Workspace

Document your work in `Step_9/Agent_Workspace/`:

**Required files**:
- `Progress.md` — What was tested, test coverage
- `Test_Results.md` — Detailed test results
- `Performance_Report.md` — Performance benchmarks
- `Challenges.md` — Any test issues encountered

**Example Progress.md**:
```markdown
# Step 9 Progress

## Completed
- [x] Created 3 test fixtures (small, medium, large projects)
- [x] Wrote 50+ comprehensive interop tests
- [x] All tests passing
- [x] Performance benchmarks verified
- [x] Error handling verified
- [x] Data integrity verified

## Test Coverage

### By Module
- CLI (Step 1): 8 tests
- Graph (Step 2): 6 tests
- Observation (Step 3): 4 tests
- Execution (Step 4): 3 tests
- Folder→Graph (Step 5): 5 tests
- Functions→Graph (Step 6): 5 tests
- Metadata (Step 7): 6 tests
- Integration (Step 8): 8 tests

### By Category
- Core workflows: 8 tests
- Interoperability: 6 tests
- Real scenarios: 6 tests
- Error handling: 9 tests
- Performance: 4 tests
- Data integrity: 5 tests

## Test Results
✅ 50/50 tests passing
✅ No flaky tests
✅ Performance targets met

## Fixtures Created
- small_project: 10 files, 20 functions
- medium_project: 50 files, 100+ functions
- large_project: 200+ files, 500+ functions

## Key Findings
- All components work together seamlessly
- Query performance excellent (< 100ms on 500+ node graph)
- Error handling comprehensive
- Data preserved through all workflows
- Ready for production!
```

---

## Key Testing Patterns

### Scenario Testing

Test real-world workflows:

```python
def test_scenario_find_deprecated():
    """Real scenario: Find all deprecated functions."""
    # Analyze project
    workflow = JarvisWorkflow()
    graph = Graph()
    workflow.analyze("tests/fixtures/medium_project", graph)
    
    # Query for deprecated
    deprecated = workflow.query(graph, "status:deprecated")
    
    # Assert we found them
    assert len(deprecated) > 0
    for node in deprecated:
        assert node.metadata['status'] == 'deprecated'
```

### Performance Testing

Test scalability:

```python
def test_performance_1000_files():
    """System should handle 1000 files efficiently."""
    import time
    
    # Create large test set
    graph = create_large_graph(1000)  # 1000 files, 5000+ functions
    
    # Time various operations
    start = time.time()
    results = workflow.query(graph, "tag:core")
    elapsed = time.time() - start
    
    # Should be fast
    assert elapsed < 0.1, f"Query took {elapsed}s"
```

### Error Recovery Testing

Test graceful failure:

```python
def test_permission_error_recovery():
    """System should recover from permission errors."""
    # Create a read-only folder
    readonly = tmp_path / "readonly"
    readonly.mkdir()
    readonly.chmod(0o000)
    
    # Analyzing should not crash
    try:
        workflow.analyze(str(tmp_path), graph)
    finally:
        readonly.chmod(0o755)  # Restore permissions
    
    # Should have analyzed other folders
    assert len(graph.nodes) > 0
```

---

## Test Coverage Goals

### By Module

| Module | Test Count | Coverage |
|--------|-----------|----------|
| CLI | 8 | All commands |
| Graph | 6 | Nodes, edges, queries |
| Observation | 4 | Folders, functions |
| Execution | 3 | Function execution |
| Converters | 10 | Both converters |
| Metadata | 6 | Load, save, query |
| Integration | 8 | Full workflows |
| **Total** | **50+** | **Complete** |

### By Scenario

| Scenario | Tests |
|----------|-------|
| Single file | 1 |
| Small project | 3 |
| Medium project | 3 |
| Large project | 3 |
| Monorepo | 1 |
| Error cases | 9 |
| Performance | 4 |
| Data integrity | 5 |
| **Total** | **50+** |

---

## Confirmation Checklist

Before telling Owen "Step 9 complete":

- [ ] All 50+ tests pass (`pytest tests/test_step_9_interop.py -v`)
- [ ] No flaky tests (run twice, same results)
- [ ] No linting errors
- [ ] All 3 test fixtures created
- [ ] Performance tests pass (< 100ms for queries)
- [ ] Error handling tests pass
- [ ] Data integrity tests pass
- [ ] Test report created
- [ ] `Agent_Workspace/` fully documented
- [ ] All v0.1 & v0.2 functionality tested

Run before confirming:
```bash
pytest tests/test_step_9_interop.py -v
pytest tests/ --cov=jarvis --cov-report=html
```

All should pass with high coverage.

---

## Questions?

If stuck:
1. Check previous step tests for patterns
2. Check fixture structure
3. Refer to `DEVELOPMENT_RULES.md`
4. Document questions in `Agent_Workspace/Questions.md`

---

## Next Steps (v0.3+)

After Step 9:
- ✅ v0.1 complete (CLI + Graph + Observation + Execution)
- ✅ v0.2 complete (Integration + Metadata + Full workflows)
- ✅ All tested and verified

Options for v0.3:
- Advanced graph queries
- Code analysis (complexity, coverage)
- Reporting and visualization
- Workflow optimization
- Performance enhancements

But for now: **Step 9 validates everything. v0.1 & v0.2 are DONE.**
