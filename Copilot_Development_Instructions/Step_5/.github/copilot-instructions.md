---
applyTo: "jarvis/**,tests/**"
---

# Step 5: Folder Tree → Graph Conversion

## Task Overview

Integrate FolderObserver output INTO the Graph. The Graph becomes the single source of truth for folder structure.

Create a `FolderToGraphConverter` class that transforms a folder hierarchy into graph nodes and edges, then extends the CLI with an `observe folder` command.

**Key Point**: Everything goes into the Graph. No isolated data structures.

---

## What You'll Create

### Files to Add/Modify

- `jarvis/converters.py` — NEW (FolderToGraphConverter class, < 300 lines)
- `tests/test_step_5.py` — NEW (20+ test cases)
- `jarvis/cli.py` — MODIFY (add `observe folder` command)

### Classes/Functions

**jarvis/converters.py**:
```python
class FolderToGraphConverter:
    """Convert folder structure to graph nodes and edges."""
    
    def convert_folder_to_graph(self, folder_path: str, graph: Graph) -> None:
        """Recursively convert folder structure to graph."""
        pass
    
    def create_folder_node(self, folder_path: str) -> Node:
        """Create node for folder."""
        pass
    
    def create_file_node(self, file_path: str) -> Node:
        """Create node for file."""
        pass
```

---

## Test Specifications

Write tests FIRST before implementing. All tests must pass.

### Test Cases (20+ total)

- [ ] `test_converter_single_folder` — One folder → graph nodes
- [ ] `test_converter_subfolder_hierarchy` — Nested folders → parent/child edges
- [ ] `test_converter_files_in_folder` — Files → nodes
- [ ] `test_converter_folder_to_file_edges` — Edges folder→file
- [ ] `test_converter_complete_tree` — Full tree structure preserved
- [ ] `test_converter_metadata_nodes` — METADATA files → nodes too
- [ ] `test_graph_folder_ids` — Node IDs use folder paths
- [ ] `test_graph_serialization_consistency` — Save/load preserves structure
- [ ] `test_cli_observe_folder` — `observe <path>` creates graph
- [ ] `test_observe_update_graph` — Updating existing graph works
- [ ] `test_large_folder_tree` — 100+ files/folders handled
- [ ] `test_folder_with_symlinks` — Symlinks handled (skip them)
- [ ] `test_permission_errors_graceful` — Missing permissions handled

Write ALL tests in `tests/test_step_5.py`.

---

## Development Rules

**IMPORTANT**: Read `DEVELOPMENT_RULES.md` in the repo root. All rules apply here.

### Folder Structure

```
jarvis/                    ← Code only
├── converters.py          ← NEW (this step)
└── (existing files)

tests/                     ← Tests only
├── test_step_5.py         ← NEW (all 20+ tests)
└── (existing tests)
```

### File Creation Rules

✅ **CAN DO** (no permission needed):
- Create `jarvis/converters.py`
- Create subfolders in `/jarvis` (e.g., `jarvis/converters/`)
- Create subfolders in `/tests` (e.g., `tests/converters/`)

❌ **CANNOT DO** (will break workflow):
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
- **Naming**: `test_<what_it_tests>` (e.g., `test_converter_single_folder`)
- **Assertions**: Clear, specific assertions
- **No skipping**: No `@pytest.mark.skip`

---

## Implementation Workflow

### Step 1: Write All Tests

Create `tests/test_step_5.py`:

```python
import pytest
from jarvis.graph import Graph, Node
from jarvis.converters import FolderToGraphConverter

def test_converter_single_folder():
    """Convert single folder to node."""
    # Arrange
    converter = FolderToGraphConverter()
    graph = Graph()
    test_folder = "tests/fixtures/sample_folder"
    
    # Act
    converter.convert_folder_to_graph(test_folder, graph)
    
    # Assert
    assert len(graph.nodes) > 0
    # ... more assertions
```

Write all 20+ tests before implementing converters.py.

### Step 2: Implement FolderToGraphConverter

Create `jarvis/converters.py` with FolderToGraphConverter class.

**Key methods**:
- `convert_folder_to_graph(folder_path, graph)` — Entry point
- `_create_folder_node(folder_path)` — Create folder node
- `_create_file_node(file_path)` — Create file node
- `_add_edges(parent_node, child_nodes)` — Connect nodes

**Node naming**:
- Folder: `"folder:/path/to/folder"`
- File: `"file:/path/to/file.py"`

### Step 3: Integrate with Graph

Ensure FolderToGraphConverter:
- Adds nodes to provided Graph object
- Creates proper edges (parent→child, folder→file)
- Handles metadata files (`.metadata.json`)
- Returns/updates Graph (no isolated data)

### Step 4: Update CLI

Add command to `jarvis/cli.py`:

```python
def do_observe_folder(self, args):
    """observe_folder <path>
    
    Observe a folder and add its structure to the graph.
    """
    path = args.strip()
    converter = FolderToGraphConverter()
    converter.convert_folder_to_graph(path, self.graph)
    print(f"Observed {path} - {len(self.graph.nodes)} nodes")
```

### Step 5: Test the CLI

Verify:
```bash
python -m jarvis.cli
> observe_folder tests/fixtures/sample
> display_graph
```

Should show folder structure as nodes and edges.

---

## Integration Points

### Dependencies

✅ **Uses from v0.1**:
- `Graph` class (Step 2)
- `Node` class (Step 2)
- `CLI` class (Step 1)

❌ **Does NOT use**:
- ExecutionEngine
- PythonObserver (yet)

### What Uses This

Future steps will use FolderToGraphConverter:
- Step 6: FunctionToGraphConverter (similar pattern)
- Step 8: Integration layer (combines converters)

### Graph Remains Central

```
User Input → FolderToGraphConverter → Graph ← (Single source of truth)
                                         ↓
                               CLI queries/displays
```

---

## Edge Cases to Handle

### Graceful Error Handling

- **Missing folder**: Log warning, continue
- **Permission denied**: Skip folder, continue
- **Symlinks**: Skip them (don't follow cycles)
- **Large trees**: Support 100+ files/folders
- **Special files**: Handle `.metadata.json`, `.gitignore`, etc.

**Example**:
```python
try:
    for item in os.listdir(folder_path):
        process_item(item)
except PermissionError:
    logger.warning(f"Permission denied: {folder_path}")
    # Continue processing other folders
```

---

## Deliverables Checklist

- [ ] `jarvis/converters.py` created (< 300 lines)
- [ ] `FolderToGraphConverter` class implemented
- [ ] All 20+ tests in `tests/test_step_5.py` pass
- [ ] CLI `observe folder` command works
- [ ] Large folder trees (100+ items) handled
- [ ] Symlinks skipped gracefully
- [ ] Permissions errors handled gracefully
- [ ] Node IDs follow `folder:/path` pattern
- [ ] Edges properly connect parent→child
- [ ] `Agent_Workspace/Progress.md` documented

---

## Agent_Workspace

Document your work in `Step_5/Agent_Workspace/`:

**Required files**:
- `Progress.md` — What you built, what works
- `Decisions.md` — Key design choices (node naming, edge structure, etc.)
- `Integration_Notes.md` — How FolderToGraphConverter integrates with Graph
- `Challenges.md` — Any problems encountered and solutions

**Example Progress.md**:
```markdown
# Step 5 Progress

## Completed
- [x] FolderToGraphConverter class
- [x] 20+ tests written
- [x] CLI observe_folder command
- [x] Large tree testing (tested with 200 items)

## Challenges
- Symlinks caused infinite loops → Fixed by skipping them
- Performance with deep trees → Added depth limit

## Integration
- FolderToGraphConverter outputs only to Graph
- No isolated data structures
- Ready for Step 6 (functions)
```

---

## Key Concepts

### Everything Into the Graph

Wrong (isolated data):
```python
folder_structure = {
    "name": "folder",
    "children": [...]
}
return folder_structure
```

Right (graph-centric):
```python
graph.add_node(folder_node)
graph.add_edge(parent, folder_node)
return graph  # or modify in-place
```

### Node Naming Convention

- Folders: `"folder:/path/to/folder"`
- Files: `"file:/path/to/file.py"`
- This makes queries easy: `find_all_nodes("folder:*")`

### Edges Represent Structure

- `parent_folder` → `child_folder` (edge label: "contains")
- `folder` → `file` (edge label: "contains")
- Metadata files → regular nodes with metadata

---

## Testing Strategy

### Test Fixtures

Use `tests/fixtures/` for test folders:

```
tests/fixtures/
├── sample_folder/
│   ├── subfolder/
│   │   └── file.py
│   ├── file.py
│   └── .metadata.json
```

Create simple fixtures in the test file itself:
```python
@pytest.fixture
def sample_folder(tmp_path):
    """Create a sample folder structure for testing."""
    folder = tmp_path / "sample"
    folder.mkdir()
    (folder / "file1.py").write_text("# code")
    (folder / "subfolder").mkdir()
    return folder
```

### Test Pattern

```python
def test_converter_single_folder(sample_folder):
    # Arrange
    converter = FolderToGraphConverter()
    graph = Graph()
    
    # Act
    converter.convert_folder_to_graph(str(sample_folder), graph)
    
    # Assert
    assert len(graph.nodes) == 2  # folder + file
    assert any(n.id.startswith("folder:") for n in graph.nodes)
    assert any(n.id.startswith("file:") for n in graph.nodes)
```

---

## Confirmation Checklist

Before telling Owen "Step 5 complete":

- [ ] All 20+ tests pass (run `pytest tests/test_step_5.py -v`)
- [ ] No linting errors (code follows style rules)
- [ ] CLI `observe_folder` command works
- [ ] Large trees (100+ items) handled without crash
- [ ] Error cases handled gracefully
- [ ] `Agent_Workspace/` fully documented
- [ ] No files in repository root
- [ ] Code follows all rules in `DEVELOPMENT_RULES.md`

Run this before confirming:
```bash
pytest tests/test_step_5.py -v
python -m jarvis.cli
> observe_folder tests/fixtures/sample
> display_graph
> exit
```

All should work with no errors.

---

## Questions?

If stuck:
1. Check `DEVELOPMENT_RULES.md` for general rules
2. Check Step 2 (graph.py) for Graph/Node API
3. Document question in `Agent_Workspace/Questions.md`
4. Ask Owen for clarification

---

## Next Steps (Step 6)

After Step 5 is approved:
- Step 6 will do the same thing with Functions (PythonObserver → Graph)
- FolderToGraphConverter becomes a template
- Both converters work together in Step 8

But first: **make Step 5 perfect and document it well**.
