# Step 2: Basic Graph, Nodes, Edges

**Status**: Ready to implement  
**Estimated Time**: 2-4 hours  
**Complexity**: Medium  
**Prerequisite**: Step 1 complete ✅  

---

## Overview

Step 2 establishes the **core data structure** for Jarvis: **Graphs, Nodes, and Edges**. This is the fundamental abstraction that everything else in Jarvis is built on.

By the end of this step, you will have:
- A `Node` class representing entities
- An `Edge` class representing relationships between nodes
- A `Graph` class that manages collections of nodes and edges
- The ability to save/load graphs as JSON
- CLI commands to manipulate graphs interactively

---

## Exact Requirements

### 2.1 Node Class

**Location**: `jarvis/graph.py`

Create a `Node` class with these **exact** properties:

```python
class Node:
    id: str                    # Unique identifier (required, non-empty)
    label: str                 # Human-readable name (required)
    metadata: dict             # Arbitrary metadata (starts empty {})
    
    Methods:
    - __init__(id, label, metadata=None)
    - to_dict() -> dict        # Serialize to dict
    - from_dict(dict) -> Node  # Static method, deserialize from dict
    - __eq__(other) -> bool    # Two nodes equal if same id
    - __repr__() -> str        # Readable string representation
```

**Constraints**:
- `id` must be unique (enforced by Graph class, not Node)
- `label` is a string
- `metadata` is a dict (can be empty)
- Node does NOT validate anything—Graph class does

### 2.2 Edge Class

**Location**: `jarvis/graph.py`

Create an `Edge` class with these **exact** properties:

```python
class Edge:
    source_id: str             # ID of source node (required)
    target_id: str             # ID of target node (required)
    metadata: dict             # Arbitrary metadata (starts empty {})
    
    Methods:
    - __init__(source_id, target_id, metadata=None)
    - to_dict() -> dict        # Serialize to dict
    - from_dict(dict) -> Edge  # Static method, deserialize from dict
    - __eq__(other) -> bool    # Two edges equal if same source & target
    - __repr__() -> str        # Readable string representation
```

**Constraints**:
- `source_id` and `target_id` are strings (IDs of nodes)
- `metadata` is a dict (can be empty)
- Edge does NOT validate that nodes exist (Graph class does)

### 2.3 Graph Class

**Location**: `jarvis/graph.py`

Create a `Graph` class with these **exact** methods:

```python
class Graph:
    nodes: dict                 # {id: Node} - internal storage
    edges: list                 # [Edge] - internal storage
    
    Methods:
    - __init__()
    
    - add_node(node: Node) -> None
      • Adds node to graph
      • If node.id already exists, replace it (no error)
      • Return None
    
    - remove_node(node_id: str) -> None
      • Removes node and ALL edges connected to it
      • If node doesn't exist, no error (silent)
      • Return None
    
    - add_edge(edge: Edge) -> None
      • Adds edge to graph
      • Does NOT validate that source/target nodes exist (for now)
      • Return None
    
    - remove_edge(source_id: str, target_id: str) -> None
      • Removes edge from source to target
      • If edge doesn't exist, no error (silent)
      • Return None
    
    - get_node(node_id: str) -> Node or None
      • Returns node with given ID, or None if not found
      • Return Node or None
    
    - to_dict() -> dict
      • Serialize entire graph to a dict
      • Format:
        {
          "nodes": [node.to_dict() for each node],
          "edges": [edge.to_dict() for each edge]
        }
      • Return dict
    
    - from_dict(dict) -> Graph
      • Static method
      • Deserialize graph from dict
      • Return Graph
    
    - __repr__() -> str
      • Readable string showing node/edge counts
      • Example: "Graph(nodes=5, edges=4)"
```

**Constraints**:
- Graph does NOT prevent cycles
- Graph does NOT prevent duplicate edges
- Graph does NOT validate node/edge relationships
- All errors (like removing non-existent node) are silent

### 2.4 JSON Serialization

**Exact JSON format** for a graph:

```json
{
  "nodes": [
    {"id": "node_1", "label": "Start", "metadata": {}},
    {"id": "node_2", "label": "End", "metadata": {}}
  ],
  "edges": [
    {"source_id": "node_1", "target_id": "node_2", "metadata": {}}
  ]
}
```

**Constraints**:
- Arrays, not objects
- Each node/edge serialized as a dict
- `metadata` must always be present (can be empty `{}`)

### 2.5 File I/O Functions

**Location**: `jarvis/graph.py` (module-level functions)

```python
def save_graph(graph: Graph, filepath: str) -> None:
    • Write graph to JSON file
    • Use json module
    • Pretty-print with indent=2
    • Return None

def load_graph(filepath: str) -> Graph:
    • Read graph from JSON file
    • Use json module
    • Return Graph instance
```

### 2.6 CLI Commands

**Location**: Extend `jarvis/cli.py` from Step 1

Add these commands to the existing CLI:

| Command | Syntax | Behavior |
|---------|--------|----------|
| `create_node` | `create_node <id> <label>` | Create and add a node to current graph |
| `create_edge` | `create_edge <source_id> <target_id>` | Create and add an edge to current graph |
| `remove_node` | `remove_node <id>` | Remove node from current graph |
| `remove_edge` | `remove_edge <source_id> <target_id>` | Remove edge from current graph |
| `display` | `display` | Print current graph to console (readable format) |
| `save` | `save <filename>` | Save current graph to JSON file |
| `load` | `load <filename>` | Load graph from JSON file |
| `clear` | `clear` | Clear current graph (empty it) |

**Display Format Example**:
```
Graph: 5 nodes, 4 edges
Nodes:
  - node_1: Start
  - node_2: Middle
  - node_3: End
  - node_4: Branch A
  - node_5: Branch B
Edges:
  - node_1 → node_2
  - node_2 → node_3
  - node_2 → node_4
  - node_4 → node_5
```

### 2.7 Code Organization

```
jarvis/
├── __init__.py
├── cli.py              (updated from Step 1)
├── graph.py            (NEW: Node, Edge, Graph classes)
```

**Constraints**:
- `graph.py` must be < 500 lines
- No external dependencies (use only stdlib)
- `cli.py` updated but still minimal

---

## Example Test Graphs

Three example graphs are provided in `tests/graphs/`:

1. **simple_chain.json** — 3 nodes in a line
2. **diamond.json** — 4 nodes, diamond pattern
3. **star.json** — 5 nodes, 1 center + 4 leaves

These are provided for testing. You don't create them; they already exist.

---

## Tests to Write FIRST

**CRITICAL**: Write these tests **before** implementing graph classes.

### Test File: `tests/test_step_2.py`

```python
# Tests you must write:

def test_node_creation():
    # Create node with id="n1", label="Start"
    # Verify: id, label, metadata stored correctly
    # Verify: metadata defaults to empty dict

def test_node_equality():
    # Create two nodes with same id
    # Verify: they are equal (same id)
    # Create two nodes with different ids
    # Verify: they are not equal

def test_node_to_dict():
    # Create node, convert to dict
    # Verify: dict has keys "id", "label", "metadata"
    # Verify: values are correct

def test_node_from_dict():
    # Create dict, convert to Node
    # Verify: Node has correct id, label, metadata
    # Verify: can reconstruct from dict

def test_edge_creation():
    # Create edge with source_id, target_id
    # Verify: source_id and target_id stored
    # Verify: metadata defaults to empty dict

def test_edge_equality():
    # Create two edges with same source/target
    # Verify: they are equal
    # Create two edges with different source/target
    # Verify: they are not equal

def test_graph_add_node():
    # Create empty graph
    # Add 3 nodes
    # Verify: all 3 nodes are in graph
    # Verify: node count is 3

def test_graph_add_edge():
    # Create graph with 2 nodes
    # Add edge between them
    # Verify: edge is in graph
    # Verify: edge count is 1

def test_graph_remove_node():
    # Create graph with 3 nodes, 2 edges
    # Remove 1 node
    # Verify: node removed
    # Verify: connected edges removed
    # Verify: other edges still exist

def test_graph_remove_edge():
    # Create graph with 2 edges
    # Remove 1 edge
    # Verify: 1 edge removed
    # Verify: other edge still exists
    # Verify: nodes still exist

def test_graph_to_dict():
    # Create graph with 2 nodes, 1 edge
    # Convert to dict
    # Verify: dict has "nodes" and "edges" keys
    # Verify: nodes and edges match original

def test_graph_from_dict():
    # Create dict representing a graph
    # Convert to Graph
    # Verify: all nodes and edges are present
    # Verify: can reconstruct graph from dict

def test_save_and_load_graph():
    # Create graph with 3 nodes, 2 edges
    # Save to JSON file
    # Load from JSON file
    # Verify: loaded graph is identical to original
    # Verify: node ids, labels, edges all match

def test_load_example_graphs():
    # Load tests/graphs/simple_chain.json
    # Verify: 3 nodes, 2 edges
    # Load tests/graphs/diamond.json
    # Verify: 4 nodes, 4 edges
    # Load tests/graphs/star.json
    # Verify: 5 nodes, 4 edges

def test_graph_get_node():
    # Create graph with 3 nodes
    # Get existing node by id
    # Verify: returns correct node
    # Get non-existent node
    # Verify: returns None

def test_cli_create_node():
    # Simulate CLI command: "create_node n1 Start"
    # Verify: node appears in current graph
    # Verify: can display it

def test_cli_create_edge():
    # Simulate CLI commands: create 2 nodes, then edge
    # Verify: edge is created
    # Verify: edge connects correct nodes

def test_cli_display():
    # Create graph with 2 nodes, 1 edge
    # Simulate CLI command: "display"
    # Verify: output shows nodes and edges
    # Verify: output is readable

def test_cli_save_load():
    # Create graph via CLI commands
    # Save with "save test.json"
    # Load with "load test.json"
    # Verify: reloaded graph is identical

def test_cli_remove_commands():
    # Create 3 nodes via CLI
    # Remove 1 node via CLI
    # Verify: node removed
    # Verify: remaining nodes still present
```

**Test Structure**:
- Use pytest
- Test both classes (Node, Edge, Graph) and CLI commands
- Mock or simulate CLI input for command tests
- Verify both internal state and output

---

## Implementation Checklist

**Remember**: Write tests first, then implement.

### Phase 1: Write Tests
- [ ] Create `tests/test_step_2.py`
- [ ] Write all 20+ test cases (listed above)
- [ ] Run tests — they will fail (expected)
- [ ] Verify no syntax errors in test file

### Phase 2: Implement Classes
- [ ] Create `jarvis/graph.py`
- [ ] Implement `Node` class
- [ ] Implement `Edge` class
- [ ] Implement `Graph` class with all methods
- [ ] Implement `save_graph()` and `load_graph()` functions
- [ ] Keep file < 500 lines

### Phase 3: Implement CLI
- [ ] Update `jarvis/cli.py`
- [ ] Add commands: `create_node`, `create_edge`, etc.
- [ ] Maintain graph in memory during session
- [ ] Implement `display` with readable format
- [ ] Keep code clean and simple

### Phase 4: Run Tests
- [ ] Run: `pytest tests/test_step_2.py -v`
- [ ] All tests pass ✅

### Phase 5: Manual Testing
- [ ] Start CLI
- [ ] Create 3 nodes
- [ ] Create 2 edges
- [ ] Run `display` — see readable output
- [ ] Run `save test.json` — file created
- [ ] Run `load test.json` — graph reloaded
- [ ] Verify graph is identical

---

## How to Confirm This Step Works

### Automated Testing
```bash
pytest tests/test_step_2.py -v
```

**Expected**: All tests pass ✅

### Manual Testing - Interactive

Start the CLI and run these commands in order:

```
jarvis> create_node n1 Start
jarvis> create_node n2 Middle
jarvis> create_node n3 End
jarvis> create_edge n1 n2
jarvis> create_edge n2 n3
jarvis> display
```

**Expected output**:
```
Graph: 3 nodes, 2 edges
Nodes:
  - n1: Start
  - n2: Middle
  - n3: End
Edges:
  - n1 → n2
  - n2 → n3
```

Continue:
```
jarvis> save my_graph.json
jarvis> clear
jarvis> display
```

**Expected**: Graph is empty

Continue:
```
jarvis> load my_graph.json
jarvis> display
```

**Expected**: Same output as before (3 nodes, 2 edges)

### Manual Testing - Load Examples

```
jarvis> load tests/graphs/simple_chain.json
jarvis> display
```

**Expected**: 3 nodes, 2 edges, linear chain

```
jarvis> load tests/graphs/diamond.json
jarvis> display
```

**Expected**: 4 nodes, 4 edges, diamond pattern

### What Owen Will Check
- ✅ All pytest tests pass
- ✅ CLI commands work interactively
- ✅ Save/load preserves graph structure exactly
- ✅ Example graphs load correctly
- ✅ Display output is readable
- ✅ Code is < 500 lines per file
- ✅ No extra features beyond what's listed

---

## Critical Notes

### DO
- ✅ Write tests first
- ✅ Keep Node/Edge/Graph simple (no validation)
- ✅ Use only Python stdlib (json, etc.)
- ✅ Make display output readable
- ✅ Test with example graphs
- ✅ Handle edge cases (empty graph, non-existent nodes, etc.)

### DO NOT
- ❌ Add validation of node/edge relationships
- ❌ Add cycle detection or graph algorithms
- ❌ Add weights or direction validation
- ❌ Prevent duplicate edges
- ❌ Add visualization or diagrams
- ❌ Implement features for Step 3+
- ❌ Use external libraries

---

## Next Step

Once this step is complete and Owen confirms:
1. All tests pass ✅
2. Manual CLI testing works ✅
3. Example graphs load correctly ✅
4. Code meets all requirements ✅

**Move to Step 3: Observation (Folders)**

---

## Questions or Stuck?

1. Re-read "Exact Requirements"
2. Check test examples for expected behavior
3. Verify your classes have all required methods
4. Ask Owen before proceeding to Step 3

**Do not move forward until both you and Owen confirm this step is 100% complete.**
