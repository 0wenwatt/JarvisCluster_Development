---
applyTo: "jarvis/**,tests/**"
---

# Step 8: Integration Layer (Combine Everything)

## Task Overview

Make everything work TOGETHER. Create a central workflow where all components work as one unit.

Users run ONE command: `analyze <path>`. Jarvis observes, enriches with metadata, builds the graph, and makes everything queryable.

**Key Point**: No isolated features. Everything integrates. Graph is central database.

---

## What You'll Create

### Files to Add/Modify

- `jarvis/integration.py` — NEW (JarvisWorkflow class, < 400 lines)
- `tests/test_step_8.py` — NEW (18+ test cases)
- `jarvis/cli.py` — MODIFY (add `analyze`, `query`, `execute` commands)

### Classes/Functions

**jarvis/integration.py**:
```python
class JarvisWorkflow:
    """Orchestrate all Jarvis components."""
    
    def analyze(self, path: str, graph: Graph) -> None:
        """Complete analysis: observe + enrich + prepare."""
        pass
    
    def query(self, graph: Graph, query_str: str) -> list:
        """Query the graph."""
        pass
    
    def execute(self, graph: Graph, start_node_id: str) -> any:
        """Execute function chain from graph."""
        pass
```

---

## Test Specifications

Write tests FIRST before implementing. All tests must pass.

### Test Cases (18+ total)

- [ ] `test_workflow_observe_folders_and_functions` — Single `analyze` scans both
- [ ] `test_workflow_metadata_attached` — Observed data includes metadata
- [ ] `test_workflow_graph_central_database` — Graph has all data
- [ ] `test_workflow_query_folder_structure` — Query folders via graph
- [ ] `test_workflow_query_functions_by_tag` — Find functions by metadata tag
- [ ] `test_workflow_query_functions_by_file` — Find functions in specific file
- [ ] `test_workflow_query_by_owner` — Find nodes owned by person
- [ ] `test_workflow_query_by_status` — Find deprecated/planned functions
- [ ] `test_workflow_execution_chain_function_lookup` — Execute functions found via observation
- [ ] `test_workflow_execution_with_metadata` — Execute with metadata context
- [ ] `test_workflow_execution_error_recovery` — Execution handles missing functions
- [ ] `test_workflow_full_cycle_single_command` — `analyze <path>` does everything
- [ ] `test_workflow_persistence` — Save/load full state
- [ ] `test_workflow_incremental_update` — Re-run analyze on modified code
- [ ] `test_workflow_large_project` — 200+ files, 500+ functions
- [ ] `test_cli_analyze_command` — Single `analyze` command works
- [ ] `test_cli_query_command` — Query graph via CLI
- [ ] `test_cli_execute_command` — Execute via graph via CLI

Write ALL tests in `tests/test_step_8.py`.

---

## Development Rules

**IMPORTANT**: Read `DEVELOPMENT_RULES.md` in the repo root. All rules apply here.

### Folder Structure

```
jarvis/
├── integration.py               ← NEW (this step)
└── (existing files)

tests/
├── test_step_8.py               ← NEW (all 18+ tests)
└── (existing tests)
```

### File Creation Rules

✅ **CAN DO** (no permission needed):
- Create `jarvis/integration.py`
- Create subfolders in `/jarvis`
- Create test fixtures

❌ **CANNOT DO**:
- Create files in repository root
- Create folders in root without permission
- Create `.md` files in code directories

### Code Rules

- **Type hints**: All functions must have type hints
- **Docstrings**: All functions must have docstrings
- **Line length**: Max 100 characters
- **File size**: Keep < 400 lines
- **Dependencies**: stdlib only (no pip packages)
- **Python**: 3.7+ compatible

### Test Rules

- **TDD**: Write tests FIRST, then implement
- **Coverage**: Each test one specific behavior
- **Naming**: `test_<what_it_tests>`
- **Assertions**: Clear, specific
- **No skipping**: No `@pytest.mark.skip`

---

## The Complete Workflow

### Before (Steps 1-7)

User had to run 4 separate commands:
```bash
observe_folder <path>
observe_functions <path>
load_metadata <path>
display_graph
```

### After (Step 8)

User runs ONE command:
```bash
analyze <path>
```

Internally, `analyze` does:
1. **Observe folders** → Graph nodes
2. **Observe functions** → Graph nodes  
3. **Load metadata** → Enrich nodes
4. **Report** → Show what was found

Then user can:
- **Query**: `query <property> <value>`
- **Execute**: `execute <start_node_id>`

---

## Implementation Workflow

### Step 1: Write All Tests

Create `tests/test_step_8.py` with all 18+ test cases:

```python
import pytest
from jarvis.graph import Graph
from jarvis.integration import JarvisWorkflow

def test_workflow_analyze_single_folder():
    """Complete analysis of single folder."""
    # Arrange
    workflow = JarvisWorkflow()
    graph = Graph()
    test_folder = "tests/fixtures/sample"
    
    # Act
    workflow.analyze(test_folder, graph)
    
    # Assert
    assert len(graph.nodes) > 0
    assert any("folder:" in n.id for n in graph.nodes)
    assert any("function:" in n.id for n in graph.nodes)
```

Write all 18+ tests before implementing.

### Step 2: Implement JarvisWorkflow

Create `jarvis/integration.py`:

```python
class JarvisWorkflow:
    """Orchestrate all Jarvis components into unified workflow."""
    
    def __init__(self):
        self.folder_converter = FolderToGraphConverter()
        self.function_converter = FunctionToGraphConverter()
        self.metadata_manager = MetadataManager()
        self.observer = PythonObserver()
    
    def analyze(self, path: str, graph: Graph) -> dict:
        """
        Complete analysis: observe folders + functions + metadata.
        
        Returns dict with summary:
        {
            "folders_observed": 10,
            "files_observed": 25,
            "functions_found": 150,
            "metadata_loaded": 5,
            "total_nodes": 185
        }
        """
        # 1. Observe folder structure
        self.folder_converter.convert_folder_to_graph(path, graph)
        
        # 2. Observe functions
        for file_path in find_python_files(path):
            functions = self.observer.observe_file(file_path)
            self.function_converter.convert_functions_to_graph(
                file_path, graph, functions
            )
        
        # 3. Load and attach metadata
        self._load_and_attach_metadata(path, graph)
        
        # 4. Return summary
        return self._summarize(graph, path)
    
    def query(self, graph: Graph, query_str: str) -> list:
        """
        Query graph by various criteria.
        
        Examples:
        - "tag:core" → Find all nodes tagged "core"
        - "status:deprecated" → Find all deprecated nodes
        - "owner:Owen" → Find all nodes owned by Owen
        - "file:jarvis/graph.py" → Find all in this file
        - "folder:jarvis" → Find all in this folder
        """
        # Parse query
        key, value = query_str.split(":", 1)
        
        if key == "tag":
            return self.metadata_manager.query_by_tag(graph, value)
        elif key == "status":
            return self._query_by_status(graph, value)
        elif key == "owner":
            return self._query_by_owner(graph, value)
        elif key == "file":
            return [n for n in graph.nodes if value in n.id]
        elif key == "folder":
            return [n for n in graph.nodes if f"folder:{value}" in n.id]
        else:
            return []
    
    def execute(self, graph: Graph, start_node_id: str, 
                *args, **kwargs) -> any:
        """
        Execute function chain starting from start_node_id.
        Uses ExecutionEngine from v0.1.
        """
        engine = ExecutionEngine()
        return engine.execute(graph, start_node_id, *args, **kwargs)
    
    def _load_and_attach_metadata(self, path: str, graph: Graph) -> None:
        """Load all METADATA files and attach to graph."""
        # Find all .metadata.json files
        for metadata_file in find_metadata_files(path):
            metadata = self.metadata_manager.load_metadata(metadata_file)
            # Determine which node this metadata belongs to
            node_id = metadata_file_to_node_id(metadata_file)
            node = graph.find_node_by_id(node_id)
            if node:
                node.metadata = metadata
    
    def _summarize(self, graph: Graph, path: str) -> dict:
        """Create summary of analysis."""
        folder_count = sum(1 for n in graph.nodes if "folder:" in n.id)
        file_count = sum(1 for n in graph.nodes if "file:" in n.id)
        function_count = sum(1 for n in graph.nodes if "function:" in n.id)
        
        return {
            "path": path,
            "folders": folder_count,
            "files": file_count,
            "functions": function_count,
            "total_nodes": len(graph.nodes),
            "total_edges": len(graph.edges)
        }
    
    def _query_by_status(self, graph: Graph, status: str) -> list:
        """Find all nodes with specific status."""
        results = []
        for node in graph.nodes:
            if hasattr(node, 'metadata') and 'status' in node.metadata:
                if node.metadata['status'] == status:
                    results.append(node)
        return results
    
    def _query_by_owner(self, graph: Graph, owner: str) -> list:
        """Find all nodes owned by person."""
        results = []
        for node in graph.nodes:
            if hasattr(node, 'metadata') and 'author' in node.metadata:
                if node.metadata['author'] == owner:
                    results.append(node)
        return results
```

### Step 3: Update CLI

Add commands to `jarvis/cli.py`:

```python
def do_analyze(self, args):
    """analyze <path>
    
    Complete analysis: observe folders, functions, and metadata.
    """
    path = args.strip()
    workflow = JarvisWorkflow()
    
    print(f"Analyzing {path}...")
    summary = workflow.analyze(path, self.graph)
    
    print("\n=== Analysis Summary ===")
    for key, value in summary.items():
        print(f"{key}: {value}")

def do_query(self, args):
    """query <key:value>
    
    Query graph by tag, status, owner, file, folder.
    Examples:
      query tag:core
      query status:stable
      query owner:Owen
      query file:jarvis/graph.py
    """
    workflow = JarvisWorkflow()
    results = workflow.query(self.graph, args.strip())
    
    print(f"Found {len(results)} matching nodes:")
    for node in results:
        print(f"  - {node.id}")

def do_execute(self, args):
    """execute <start_node_id> [arg1] [arg2] ...
    
    Execute function chain from graph.
    """
    parts = args.split()
    if not parts:
        print("Usage: execute <start_node_id> [args...]")
        return
    
    start_node_id = parts[0]
    func_args = parts[1:] if len(parts) > 1 else []
    
    workflow = JarvisWorkflow()
    try:
        result = workflow.execute(self.graph, start_node_id, *func_args)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Execution error: {e}")
```

### Step 4: Test Integration

Test the complete workflow:

```bash
python -m jarvis.cli
> analyze tests/
> query tag:core
> query status:stable
> query owner:Owen
> display_graph
> exit
```

Should show:
- Analysis summary (folders, files, functions)
- Query results
- Full graph with all data

---

## Integration Points

### Dependencies

✅ **Uses all v0.1 & v0.2 modules**:
- `Graph`, `Node`, `Edge` (Step 2)
- `CLI` (Step 1)
- `FolderToGraphConverter` (Step 5)
- `FunctionToGraphConverter` (Step 6)
- `MetadataManager` (Step 7)
- `ExecutionEngine` (Step 4)
- `PythonObserver` (Step 3)

### What Uses This

Step 9 (Interop tests) will test JarvisWorkflow extensively.

### Complete Architecture

```
User runs: analyze <path>
    ↓
JarvisWorkflow.analyze()
    ├─→ FolderToGraphConverter.convert()
    ├─→ FunctionToGraphConverter.convert()
    ├─→ MetadataManager.load_and_attach()
    └─→ Returns summary
        ↓
     Graph (central database)
        ↓
User runs: query tag:core
    ↓
JarvisWorkflow.query()
    └─→ Find matching nodes
        ↓
     Display results
```

---

## Deliverables Checklist

- [ ] `jarvis/integration.py` created (< 400 lines)
- [ ] JarvisWorkflow class with analyze, query, execute
- [ ] All 18+ tests in `tests/test_step_8.py` pass
- [ ] CLI `analyze` command works
- [ ] CLI `query` command works (tag, status, owner, file, folder)
- [ ] CLI `execute` command works
- [ ] Full workflow tested (observe → query → execute)
- [ ] Large projects (200+ files) handled
- [ ] Metadata properly enriches graph
- [ ] `Agent_Workspace/Progress.md` documented

---

## Agent_Workspace

Document your work in `Step_8/Agent_Workspace/`:

**Required files**:
- `Progress.md` — What you built, workflow tested
- `Decisions.md` — Integration design decisions
- `Integration_Notes.md` — How all pieces work together
- `Challenges.md` — Problems and solutions

**Example Progress.md**:
```markdown
# Step 8 Progress

## Completed
- [x] JarvisWorkflow class
- [x] analyze() method integrates all components
- [x] query() method with 5 query types
- [x] execute() method chains functions from graph
- [x] 18+ tests written and passing
- [x] CLI analyze, query, execute commands

## How It Works
analyze <path> runs:
1. FolderToGraphConverter - folder structure → nodes
2. PythonObserver - extract functions
3. FunctionToGraphConverter - functions → nodes
4. MetadataManager - load metadata files
5. Attach metadata to graph nodes

Result: Complete map of codebase in Graph

## Integration
- All modules work through central Graph
- No data isolation
- Queries work on enriched graph
- Execution uses graph for function lookup

## Next Step
Step 9 will test all interoperability comprehensively
```

---

## Key Concepts

### One Graph, Everything

Before (Steps 1-4):
- CLI in isolation
- Graph in isolation
- Observation in isolation
- Execution in isolation

After (Step 8):
- Graph is central
- All components feed into Graph
- All queries go through Graph
- All execution uses Graph

### Query Language

Simple but powerful:
```
query tag:<value>           → Find by tag
query status:<value>        → Find by status
query owner:<value>         → Find by author
query file:<path>           → Find in file
query folder:<path>         → Find in folder
```

Can be extended later for more complex queries.

### Graceful Integration

Each component handles its own errors:
```python
def analyze(self, path, graph):
    try:
        self.folder_converter.convert_folder_to_graph(path, graph)
    except PermissionError:
        logger.warning(f"Permission denied: {path}")
        # Continue with rest
    
    try:
        # Observe functions
        ...
    except SyntaxError as e:
        logger.warning(f"Syntax error: {e}")
        # Continue with other files
    
    # Continue with metadata
    ...
```

---

## Testing Strategy

### Test Fixtures

Use realistic test projects:

```python
@pytest.fixture
def test_project(tmp_path):
    """Create a realistic test project structure."""
    project = tmp_path / "test_project"
    project.mkdir()
    
    # Create folder structure
    (project / "src").mkdir()
    (project / "tests").mkdir()
    
    # Create files with functions
    (project / "src" / "utils.py").write_text("""
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
""")
    
    # Create metadata
    metadata = {
        "description": "Test project",
        "status": "active"
    }
    # Write metadata files...
    
    return project
```

### Test Pattern

```python
def test_workflow_full_cycle(test_project):
    # Arrange
    workflow = JarvisWorkflow()
    graph = Graph()
    
    # Act
    summary = workflow.analyze(str(test_project), graph)
    
    # Assert
    assert summary["folders"] >= 2
    assert summary["functions"] >= 2
    assert len(graph.nodes) > 0
    
    # Query test
    results = workflow.query(graph, "status:active")
    assert len(results) > 0
```

---

## Confirmation Checklist

Before telling Owen "Step 8 complete":

- [ ] All 18+ tests pass (`pytest tests/test_step_8.py -v`)
- [ ] No linting errors
- [ ] CLI `analyze` command works
- [ ] CLI `query` command works (all 5 query types)
- [ ] CLI `execute` command works
- [ ] Full workflow tested end-to-end
- [ ] Large projects (200+ files) handled
- [ ] Metadata properly enriches graph
- [ ] `integration.py` < 400 lines
- [ ] `Agent_Workspace/` fully documented

Run before confirming:
```bash
pytest tests/test_step_8.py -v
python -m jarvis.cli
> analyze tests/
> query tag:test
> query status:active
> display_graph
> exit
```

All should work smoothly.

---

## Questions?

If stuck:
1. Check `DEVELOPMENT_RULES.md` for general rules
2. Check previous steps (5, 6, 7) for component APIs
3. Review workflow diagram above
4. Document questions in `Agent_Workspace/Questions.md`

---

## Next Steps (Step 9)

After Step 8 is approved:
- Step 9 tests everything comprehensively
- Interoperability across all modules
- Large projects, edge cases
- Performance testing

But first: **make Step 8 solid, test full workflow, document integration points**.
