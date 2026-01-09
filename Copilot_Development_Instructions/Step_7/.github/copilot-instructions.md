---
applyTo: "jarvis/**,tests/**"
---

# Step 7: Metadata Files & Manager

## Task Overview

Create metadata files by hand, build a MetadataManager to handle them, and attach metadata to graph nodes.

Graph nodes become rich with information: descriptions, tags, ownership, status, version. Everything queryable.

**Key Point**: Metadata enriches the graph. Graph nodes stay at center, metadata describes them.

---

## What You'll Create

### Files to Add/Modify

- `jarvis/metadata_manager.py` — NEW (MetadataManager class, < 400 lines)
- `tests/test_step_7.py` — NEW (25+ test cases)
- `jarvis/.metadata.json` — NEW (example, created by hand)
- `jarvis/graph.py.metadata.json` — NEW (example, created by hand)
- `tests/.metadata.json` — NEW (example, created by hand)
- `jarvis/cli.py` — MODIFY (add `metadata` commands)

### Classes/Functions

**jarvis/metadata_manager.py**:
```python
class MetadataManager:
    """Manage metadata files and attach to graph nodes."""
    
    def load_metadata(self, path: str) -> dict:
        """Load METADATA.json file."""
        pass
    
    def save_metadata(self, path: str, metadata: dict) -> None:
        """Save METADATA.json file."""
        pass
    
    def attach_to_graph(self, graph: Graph, metadata_map: dict) -> None:
        """Attach metadata to graph nodes."""
        pass
    
    def query_by_tag(self, graph: Graph, tag: str) -> list:
        """Find all nodes with a tag."""
        pass
```

---

## Test Specifications

Write tests FIRST before implementing. All tests must pass.

### Test Cases (25+ total)

- [ ] `test_metadata_file_format` — METADATA.json structure correct
- [ ] `test_metadata_file_load` — Load existing METADATA file
- [ ] `test_metadata_file_save` — Save METADATA file
- [ ] `test_metadata_node_description` — Add description to node
- [ ] `test_metadata_node_tags` — Add tags/labels to node
- [ ] `test_metadata_node_owner` — Add ownership info
- [ ] `test_metadata_node_status` — Add status (planned, done, deprecated)
- [ ] `test_metadata_inheritance` — Child nodes inherit parent metadata
- [ ] `test_metadata_file_folder_metadata` — METADATA for folders
- [ ] `test_metadata_file_function_metadata` — METADATA for functions
- [ ] `test_metadata_graph_integration` — Metadata attached to graph nodes
- [ ] `test_metadata_query` — Query nodes by tag/status/owner
- [ ] `test_metadata_bulk_update` — Update multiple nodes at once
- [ ] `test_metadata_merge_files` — Combine METADATA from multiple files
- [ ] `test_cli_metadata_show` — Show metadata for node
- [ ] `test_cli_metadata_edit` — Edit metadata via CLI
- [ ] `test_metadata_validation` — Invalid metadata rejected
- [ ] `test_metadata_conflicts` — Conflicting metadata handled

Write ALL tests in `tests/test_step_7.py`.

---

## Development Rules

**IMPORTANT**: Read `DEVELOPMENT_RULES.md` in the repo root. All rules apply here.

### Folder Structure

```
jarvis/
├── metadata_manager.py          ← NEW (this step)
├── .metadata.json               ← NEW (example, created by hand)
├── graph.py.metadata.json       ← NEW (example, created by hand)
└── (existing files)

tests/
├── test_step_7.py               ← NEW (all 25+ tests)
├── .metadata.json               ← NEW (example, created by hand)
└── (existing tests)
```

### File Creation Rules

✅ **CAN DO** (no permission needed):
- Create `jarvis/metadata_manager.py`
- Create METADATA files (`.metadata.json`)
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

## Metadata File Format

### File Location and Naming

Metadata files are `.metadata.json` alongside their targets:

```
jarvis/
├── .metadata.json                    ← Module metadata
├── graph.py                          ← File
├── graph.py.metadata.json            ← File metadata
├── converters.py
├── converters.py.metadata.json

tests/
├── .metadata.json                    ← Test module metadata
├── test_step_6.py
├── test_step_6.py.metadata.json
```

### File Format (JSON)

**Module-level** (jarvis/.metadata.json):
```json
{
  "description": "Jarvis core module",
  "version": "0.2.0",
  "author": "Owen",
  "created": "2026-01-09",
  "tags": ["core", "graph", "observation"],
  "status": "active",
  "notes": "Central graph database and CLI interface"
}
```

**File-level** (jarvis/graph.py.metadata.json):
```json
{
  "description": "Graph data structure - nodes, edges, basic operations",
  "status": "stable",
  "author": "Owen",
  "version": "0.1.0",
  "tags": ["graph", "core", "database"],
  "key_functions": ["add_node", "add_edge", "remove_node"],
  "dependencies": [],
  "notes": "Central data structure, used by all other modules"
}
```

**Function-level** (embedded in metadata or separate):
```json
{
  "functions": {
    "add_node": {
      "description": "Add a node to the graph",
      "status": "stable",
      "parameters": ["node_id", "label"],
      "return_type": "Node"
    }
  }
}
```

---

## Implementation Workflow

### Step 1: Write All Tests

Create `tests/test_step_7.py` with all 25+ test cases.

```python
import pytest
import json
from pathlib import Path
from jarvis.metadata_manager import MetadataManager
from jarvis.graph import Graph, Node

def test_metadata_file_format():
    """Valid METADATA.json files load correctly."""
    # Arrange
    manager = MetadataManager()
    metadata_file = Path("jarvis/.metadata.json")
    
    # Act
    metadata = manager.load_metadata(str(metadata_file))
    
    # Assert
    assert isinstance(metadata, dict)
    assert "description" in metadata
    assert "status" in metadata
```

Write all tests before implementing.

### Step 2: Create Example Metadata Files

Create 3 METADATA files by hand. These are EXAMPLES that agents will see:

**jarvis/.metadata.json**:
```json
{
  "description": "Jarvis core module - graph database and CLI interface",
  "version": "0.2.0",
  "author": "Owen",
  "created": "2026-01-09",
  "tags": ["core", "graph", "observation", "execution"],
  "status": "active",
  "notes": "Central graph serves as single source of truth for all Jarvis data"
}
```

**jarvis/graph.py.metadata.json**:
```json
{
  "description": "Graph data structure with Node, Edge, and Graph classes",
  "file": "jarvis/graph.py",
  "status": "stable",
  "author": "Owen",
  "created": "2026-01-08",
  "version": "0.1.0",
  "tags": ["core", "database", "graph"],
  "key_classes": ["Node", "Edge", "Graph"],
  "dependencies": ["jarvis.observers"],
  "usage": "Central data structure for all Jarvis operations",
  "notes": "Stores folder structure, functions, metadata, and execution data"
}
```

**tests/.metadata.json**:
```json
{
  "description": "Test suite for Jarvis",
  "version": "0.2.0",
  "author": "Owen",
  "created": "2026-01-09",
  "tags": ["tests", "tdd", "integration"],
  "status": "active",
  "coverage": "100+test cases across 9 steps",
  "notes": "All development follows TDD - tests written first"
}
```

These become examples that developers can copy and modify.

### Step 3: Implement MetadataManager

Create `jarvis/metadata_manager.py`:

**Key methods**:

```python
class MetadataManager:
    """Manage metadata for graph nodes."""
    
    def load_metadata(self, path: str) -> dict:
        """
        Load METADATA.json file.
        
        Args:
            path: Path to METADATA.json file
            
        Returns:
            Dictionary of metadata
        """
        with open(path, 'r') as f:
            return json.load(f)
    
    def save_metadata(self, path: str, metadata: dict) -> None:
        """Save METADATA.json file."""
        # Validate before saving
        self._validate_metadata(metadata)
        with open(path, 'w') as f:
            json.dump(metadata, f, indent=2)
    
    def attach_to_graph(self, graph: Graph, metadata_map: dict) -> None:
        """Attach metadata dict to graph nodes."""
        for node_id, metadata in metadata_map.items():
            node = graph.find_node_by_id(node_id)
            if node:
                node.metadata = metadata
    
    def query_by_tag(self, graph: Graph, tag: str) -> list:
        """Find all nodes with a specific tag."""
        results = []
        for node in graph.nodes:
            if hasattr(node, 'metadata') and 'tags' in node.metadata:
                if tag in node.metadata['tags']:
                    results.append(node)
        return results
    
    def _validate_metadata(self, metadata: dict) -> bool:
        """Validate metadata structure."""
        if not isinstance(metadata, dict):
            raise ValueError("Metadata must be a dict")
        if 'description' not in metadata:
            raise ValueError("Metadata must have 'description'")
        return True
```

### Step 4: Update CLI

Add metadata commands to `jarvis/cli.py`:

```python
def do_metadata_show(self, args):
    """metadata_show <node_id>
    
    Show metadata for a node.
    """
    node_id = args.strip()
    node = self.graph.find_node_by_id(node_id)
    if node and hasattr(node, 'metadata'):
        import json
        print(json.dumps(node.metadata, indent=2))
    else:
        print(f"No metadata for {node_id}")

def do_metadata_edit(self, args):
    """metadata_edit <node_id> <key> <value>
    
    Edit metadata for a node.
    """
    parts = args.split(maxsplit=2)
    if len(parts) != 3:
        print("Usage: metadata_edit <node_id> <key> <value>")
        return
    
    node_id, key, value = parts
    node = self.graph.find_node_by_id(node_id)
    if node:
        if not hasattr(node, 'metadata'):
            node.metadata = {}
        node.metadata[key] = value
        print(f"Updated {node_id}.{key} = {value}")
    else:
        print(f"Node not found: {node_id}")
```

### Step 5: Test Integration

Verify everything works:

```bash
python -m jarvis.cli
> observe_folder tests/
> observe_functions tests/
> load_metadata jarvis/.metadata.json
> metadata_show file:tests
> exit
```

---

## Integration Points

### Dependencies

✅ **Uses from v0.1**:
- `Graph` class (Step 2)
- `Node` class (Step 2)
- `CLI` class (Step 1)

✅ **Uses from v0.2**:
- `FolderToGraphConverter` (Step 5)
- `FunctionToGraphConverter` (Step 6)

### What Uses This

Future steps will use MetadataManager:
- Step 8: Integration layer (queries by metadata)
- Step 9: Interop tests (all data with metadata)

### Graph Nodes Enhanced

```
Node (from Steps 5-6)
├── id: "function:jarvis/graph.py:add_node"
├── label: "add_node"
└── metadata: {                    ← NEW (Step 7)
    "description": "...",
    "status": "stable",
    "tags": ["core", "graph"],
    "author": "Owen",
    "version": "0.1.0"
  }
```

---

## Example Metadata Queries

After Step 7:

```bash
# Find all "core" functions
query_by_tag("core")
→ [node1, node2, node3]

# Find all deprecated functions
query_by_status("deprecated")
→ [node4, node5]

# Find all functions owned by Owen
query_by_owner("Owen")
→ [node1, node2, ..., node20]

# Find all test files with status "active"
query nodes where "file" in id and status == "active"
→ [test_step_1, test_step_2, ...]
```

---

## Deliverables Checklist

- [ ] `jarvis/metadata_manager.py` created (< 400 lines)
- [ ] MetadataManager class with all methods
- [ ] All 25+ tests in `tests/test_step_7.py` pass
- [ ] 3 example METADATA files created by hand:
  - [ ] `jarvis/.metadata.json`
  - [ ] `jarvis/graph.py.metadata.json`
  - [ ] `tests/.metadata.json`
- [ ] CLI `metadata_show` command works
- [ ] CLI `metadata_edit` command works
- [ ] Metadata attaches to graph nodes
- [ ] Query by tag works
- [ ] Query by status works
- [ ] Metadata files validate correctly
- [ ] `Agent_Workspace/Progress.md` documented

---

## Agent_Workspace

Document your work in `Step_7/Agent_Workspace/`:

**Required files**:
- `Progress.md` — What you built, example metadata files
- `Decisions.md` — Design choices (metadata format, validation, etc.)
- `Integration_Notes.md` — How metadata enriches graph nodes
- `Challenges.md` — Any problems encountered

**Example Progress.md**:
```markdown
# Step 7 Progress

## Completed
- [x] MetadataManager class
- [x] 25+ tests written and passing
- [x] Example METADATA files created by hand
- [x] CLI metadata_show and metadata_edit commands
- [x] Query by tag/status/owner working

## Example Metadata Files
Created:
- jarvis/.metadata.json (module description)
- jarvis/graph.py.metadata.json (file description)
- tests/.metadata.json (test module description)

## Challenges
- Validation: Ensured required fields present
- Inheritance: Decided child nodes don't inherit yet

## Next
- Step 8 will integrate everything
- Step 9 will test full interop
```

---

## Key Concepts

### Metadata is Separate

Metadata lives in `.metadata.json` files, NOT in code:

✅ Good:
```
jarvis/
├── graph.py
└── graph.py.metadata.json
```

❌ Bad:
```python
# DON'T put metadata in code
class Graph:
    metadata = {"description": "..."}
```

### Graph Nodes Get Enriched

Before (Step 6):
```python
node = Node("function:jarvis/graph.py:add_node", "add_node")
```

After (Step 7):
```python
node = Node("function:jarvis/graph.py:add_node", "add_node")
node.metadata = {
    "description": "Add a node to the graph",
    "status": "stable",
    "tags": ["core", "graph"],
    "author": "Owen"
}
```

### Querying Becomes Powerful

With metadata, queries become rich:

```python
# Find all deprecated functions
manager.query_by_tag(graph, "deprecated")

# Find all functions owned by Owen
manager.query_by_owner(graph, "Owen")

# Find all stable, core functions
manager.query_by_tags(graph, ["stable", "core"])
```

---

## Testing Strategy

### Test Fixtures

Create example metadata files in tests:

```python
@pytest.fixture
def sample_metadata():
    return {
        "description": "Test metadata",
        "status": "active",
        "tags": ["test", "example"],
        "author": "Test Agent"
    }

@pytest.fixture
def metadata_file(tmp_path, sample_metadata):
    metadata_path = tmp_path / "test.metadata.json"
    with open(metadata_path, 'w') as f:
        json.dump(sample_metadata, f)
    return metadata_path
```

### Test Pattern

```python
def test_metadata_file_load(metadata_file):
    # Arrange
    manager = MetadataManager()
    
    # Act
    loaded = manager.load_metadata(str(metadata_file))
    
    # Assert
    assert loaded["description"] == "Test metadata"
    assert "test" in loaded["tags"]
```

---

## Confirmation Checklist

Before telling Owen "Step 7 complete":

- [ ] All 25+ tests pass (`pytest tests/test_step_7.py -v`)
- [ ] No linting errors
- [ ] 3 example METADATA files created and valid
- [ ] MetadataManager loads/saves correctly
- [ ] CLI metadata commands work
- [ ] Metadata attaches to graph nodes
- [ ] Query by tag/status/owner works
- [ ] Validation rejects invalid metadata
- [ ] `metadata_manager.py` < 400 lines
- [ ] `Agent_Workspace/` fully documented

Run before confirming:
```bash
pytest tests/test_step_7.py -v
python -m jarvis.cli
> observe_folder tests/
> observe_functions tests/
> metadata_show file:tests
> metadata_edit file:tests status active
> exit
```

All should work without errors.

---

## Questions?

If stuck:
1. Check `DEVELOPMENT_RULES.md` for general rules
2. Check example metadata files created in this step
3. Review JSON format in "Metadata File Format" section
4. Document questions in `Agent_Workspace/Questions.md`

---

## Next Steps (Step 8)

After Step 7 is approved:
- Step 8 combines everything: observe + metadata + query + execute
- Single `analyze` command does it all
- Everything integrated via Graph

But first: **make Step 7 solid, create good examples, test thoroughly**.
