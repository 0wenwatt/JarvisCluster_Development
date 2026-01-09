---
applyTo: "jarvis/**,tests/**"
---

# Step 6: Function Scraper → Graph Conversion

## Task Overview

Integrate PythonObserver output INTO the Graph. Functions become queryable nodes in the same graph as folders.

Create a `FunctionToGraphConverter` class that transforms observed functions into graph nodes and edges. Functions now exist in the central Graph alongside folder structure.

**Key Point**: Graph is the database. Functions, folders, metadata — all in one place.

---

## What You'll Create

### Files to Add/Modify

- `jarvis/converters.py` — MODIFY (add FunctionToGraphConverter class)
- `tests/test_step_6.py` — NEW (25+ test cases)
- `jarvis/cli.py` — MODIFY (add `observe functions` command)

### Classes/Functions

**jarvis/converters.py** (expanded):
```python
class FunctionToGraphConverter:
    """Convert observed functions to graph nodes and edges."""
    
    def convert_functions_to_graph(self, file_path: str, graph: Graph) -> None:
        """Convert all functions in file to graph nodes."""
        pass
    
    def create_function_node(self, func_info: dict) -> Node:
        """Create node for function."""
        pass
    
    def create_dependency_edge(self, from_func: Node, to_func: Node) -> None:
        """Create edge for function call."""
        pass
```

---

## Test Specifications

Write tests FIRST before implementing. All tests must pass.

### Test Cases (25+ total)

- [ ] `test_converter_single_function` — Function → graph node
- [ ] `test_converter_function_metadata` — Function details stored
- [ ] `test_converter_line_numbers` — Line numbers captured
- [ ] `test_converter_file_to_function_edges` — Edges file→function
- [ ] `test_converter_multiple_functions` — Multiple functions → multiple nodes
- [ ] `test_converter_function_signatures` — Parameters + return types stored
- [ ] `test_converter_function_dependencies` — Function calls → edges
- [ ] `test_graph_function_lookup` — Find all functions in file
- [ ] `test_graph_function_query` — Query function by name across repo
- [ ] `test_cli_observe_functions` — `observe functions <path>` works
- [ ] `test_observe_update_existing_functions` — Re-observing updates nodes
- [ ] `test_large_codebase_100_functions` — 100+ functions handled
- [ ] `test_complex_function_signatures` — Type hints, *args, **kwargs handled
- [ ] `test_syntax_error_file_recovery` — One bad file doesn't break rest
- [ ] `test_graph_interop_folders_and_functions` — Both in same graph

Write ALL tests in `tests/test_step_6.py`.

---

## Development Rules

**IMPORTANT**: Read `DEVELOPMENT_RULES.md` in the repo root. All rules apply here.

### Folder Structure

```
jarvis/
├── converters.py          ← MODIFY (add FunctionToGraphConverter)
└── (existing files)

tests/
├── test_step_6.py         ← NEW (all 25+ tests)
└── (existing tests)
```

### File Creation Rules

✅ **CAN DO** (no permission needed):
- Modify `jarvis/converters.py` (add class)
- Create subfolders in `/jarvis` if needed
- Create test fixtures in `/tests`

❌ **CANNOT DO**:
- Create files in repository root
- Create folders in root without permission
- Create `.md` files in code directories

### Code Rules

- **Type hints**: All functions must have type hints
- **Docstrings**: All functions must have docstrings
- **Line length**: Max 100 characters
- **File size**: Keep converters.py < 500 lines
- **Dependencies**: stdlib only (no pip packages)
- **Python**: 3.7+ compatible

### Test Rules

- **TDD**: Write tests FIRST, then implement
- **Coverage**: Each test one specific behavior
- **Naming**: `test_<what_it_tests>`
- **Assertions**: Clear, specific
- **No skipping**: No `@pytest.mark.skip`

---

## Implementation Workflow

### Step 1: Write All Tests

Create `tests/test_step_6.py`:

```python
import pytest
from jarvis.graph import Graph, Node
from jarvis.converters import FunctionToGraphConverter
from jarvis.observers import PythonObserver

def test_converter_single_function():
    """Convert single function to node."""
    # Arrange
    converter = FunctionToGraphConverter()
    graph = Graph()
    observer = PythonObserver()
    
    # Observe a simple file
    test_file = "tests/fixtures/simple.py"
    functions = observer.observe_file(test_file)
    
    # Act
    converter.convert_functions_to_graph(test_file, graph, functions)
    
    # Assert
    assert len(graph.nodes) > 0
    assert any(n.id.startswith("function:") for n in graph.nodes)
```

Write all 25+ tests before implementing.

### Step 2: Implement FunctionToGraphConverter

Extend `jarvis/converters.py` with FunctionToGraphConverter class.

**Key methods**:
- `convert_functions_to_graph(file_path, graph, functions)` — Entry point
- `_create_function_node(func_info)` — Create function node
- `_extract_dependencies(func_ast)` — Find function calls
- `_add_file_to_function_edge(file_node, func_node)` — Connect to file

**Node naming**:
- Function: `"function:<file_path>:<function_name>"`
- Example: `"function:jarvis/graph.py:add_node"`

**Node metadata** (stored on node):
- `name`: Function name
- `file`: File path
- `line_start`: Start line
- `line_end`: End line
- `parameters`: List of parameter names
- `return_type`: Return type annotation
- `calls`: List of functions it calls

### Step 3: Integrate with Graph

FunctionToGraphConverter must:
- Add function nodes to provided Graph
- Create file→function edges
- Create function→function edges (for dependencies)
- Work alongside FolderToGraphConverter (Step 5)
- Not replace existing nodes, update them

**Key integration**: If a file was already added by FolderToGraphConverter:
```python
# File node already exists: file:/path/to/file.py
# Add function nodes
function_node = Node("function:/path/to/file.py:my_func", ...)
# Connect
graph.add_edge(file_node, function_node, "contains")
```

### Step 4: Update CLI

Add command to `jarvis/cli.py`:

```python
def do_observe_functions(self, args):
    """observe_functions <path>
    
    Observe Python functions in a file or folder and add to graph.
    """
    path = args.strip()
    observer = PythonObserver()
    converter = FunctionToGraphConverter()
    
    if os.path.isfile(path):
        functions = observer.observe_file(path)
        converter.convert_functions_to_graph(path, self.graph, functions)
    else:
        for file_path in find_python_files(path):
            functions = observer.observe_file(file_path)
            converter.convert_functions_to_graph(file_path, self.graph, functions)
    
    print(f"Observed {path} - {len(self.graph.nodes)} total nodes")
```

### Step 5: Test Interoperability

Verify both work together:

```bash
python -m jarvis.cli
> observe_folder tests/
> observe_functions tests/
> display_graph
```

Should show:
- Folder nodes: `folder:tests`
- File nodes: `file:tests/test_step_6.py`
- Function nodes: `function:tests/test_step_6.py:test_converter_single_function`
- All connected by edges

---

## Integration Points

### Dependencies

✅ **Uses from v0.1**:
- `Graph` class (Step 2)
- `Node` class (Step 2)
- `CLI` class (Step 1)
- `PythonObserver` (Step 3)

✅ **Uses from v0.2**:
- `FolderToGraphConverter` (Step 5) — coordinate node IDs

### What Uses This

Future steps will use FunctionToGraphConverter:
- Step 7: MetadataManager (queries functions by metadata)
- Step 8: Integration layer (combines with FolderToGraphConverter)

### Graph Remains Central

```
Python Code → PythonObserver → FunctionToGraphConverter → Graph
                                                           ↓
                                                   (same graph as folders)
```

---

## Handling Function Dependencies

### Simple Dependency Detection

Use AST to find function calls:

```python
def extract_calls(func_ast):
    """Extract function calls from a function AST node."""
    calls = []
    for node in ast.walk(func_ast):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                calls.append(node.func.id)
    return calls
```

### Creating Dependency Edges

```python
# Find called functions in graph
for called_func_name in extracted_calls:
    # Find node: function:<file>:<called_func_name>
    called_node = graph.find_node_by_name(called_func_name)
    if called_node:
        graph.add_edge(func_node, called_node, "calls")
```

### Graceful Handling

If called function not in graph yet:
- Skip creating edge (it will be added later)
- Log it for Agent_Workspace notes
- Don't crash

---

## Edge Cases to Handle

### Graceful Error Handling

- **Syntax errors in file**: Log, skip file, continue
- **Missing imports**: Ignore external calls, continue
- **Large files (1000+ functions)**: Support it
- **Recursive functions**: Handle cycles in call graph
- **Nested functions**: Support them (create nodes)
- **Lambda functions**: Include or skip (document choice)

**Example**:
```python
try:
    tree = ast.parse(source_code)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # Process function
            create_function_node(node)
except SyntaxError as e:
    logger.warning(f"Syntax error in {file_path}: {e}")
    # Continue processing other files
```

---

## Deliverables Checklist

- [ ] `FunctionToGraphConverter` class added to `converters.py`
- [ ] All 25+ tests in `tests/test_step_6.py` pass
- [ ] CLI `observe functions` command works
- [ ] Function nodes created with proper IDs: `function:<file>:<name>`
- [ ] Function metadata captured (signature, line numbers)
- [ ] Dependencies detected and linked
- [ ] Works alongside FolderToGraphConverter (interop test)
- [ ] Large codebases (100+ functions) handled
- [ ] Syntax errors handled gracefully
- [ ] `converters.py` stays < 500 lines
- [ ] `Agent_Workspace/Progress.md` documented

---

## Agent_Workspace

Document your work in `Step_6/Agent_Workspace/`:

**Required files**:
- `Progress.md` — What you built, what works
- `Decisions.md` — Design choices (dependency detection, node naming, etc.)
- `Integration_Notes.md` — How FunctionToGraphConverter works with FolderToGraphConverter
- `Challenges.md` — Problems and solutions

**Example Progress.md**:
```markdown
# Step 6 Progress

## Completed
- [x] FunctionToGraphConverter class
- [x] 25+ tests written and passing
- [x] CLI observe_functions command
- [x] Dependency edge creation
- [x] Tested with 200+ function codebase

## Challenges
- Nested functions: Created nodes for them too
- Recursive calls: Handled by allowing cycles in graph
- Missing imports: Skipped external calls gracefully

## Integration
- FunctionToGraphConverter + FolderToGraphConverter = complete repo map
- Both add to same Graph object
- Node IDs are consistent (folder:/path vs function:/path:name)
- Ready for Step 7 (metadata)
```

---

## Key Concepts

### Function Node Naming

**Format**: `"function:<file_path>:<function_name>"`

**Examples**:
- `"function:jarvis/graph.py:add_node"`
- `"function:tests/test_step_6.py:test_converter_single_function"`

This allows:
- Query all functions in a file: `find_nodes("function:jarvis/graph.py:*")`
- Find specific function: `find_node("function:jarvis/graph.py:add_node")`

### Metadata on Function Nodes

Store as node properties:
```python
func_node.metadata = {
    "name": "add_node",
    "file": "jarvis/graph.py",
    "line_start": 45,
    "line_end": 52,
    "parameters": ["self", "node_id", "label"],
    "return_type": "Node",
    "calls": ["_validate_id", "Node"]
}
```

### Graph Consistency

When converting functions:
- Reuse existing file nodes (don't create duplicates)
- Reuse existing graph nodes if they exist
- Add only new function nodes
- Update if observing same file again

```python
# File node should already exist from Step 5
file_node = graph.find_node_by_id("file:jarvis/graph.py")
if not file_node:
    # Create if missing
    file_node = graph.add_node("file:jarvis/graph.py", "File")

# Create function node
func_node = graph.add_node("function:jarvis/graph.py:add_node", "Function")

# Connect
graph.add_edge(file_node, func_node, "contains")
```

---

## Testing Strategy

### Test Fixtures

Use simple test files:

```python
# tests/fixtures/simple.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def call_other():
    result = add(1, 2)
    return result
```

```python
# tests/fixtures/complex.py
class Helper:
    def method(self):
        pass

def outer():
    def inner():
        pass
    return inner()
```

### Test Pattern

```python
def test_converter_single_function():
    # Arrange
    converter = FunctionToGraphConverter()
    observer = PythonObserver()
    graph = Graph()
    test_file = "tests/fixtures/simple.py"
    
    # Observe to get function info
    functions = observer.observe_file(test_file)
    
    # Act
    converter.convert_functions_to_graph(test_file, graph, functions)
    
    # Assert
    assert len(graph.nodes) >= 2  # file + functions
    func_nodes = [n for n in graph.nodes if "function:" in n.id]
    assert len(func_nodes) >= 2  # add, multiply
    assert any("add" in n.id for n in func_nodes)
```

---

## Confirmation Checklist

Before telling Owen "Step 6 complete":

- [ ] All 25+ tests pass (`pytest tests/test_step_6.py -v`)
- [ ] No linting errors
- [ ] CLI `observe functions` command works
- [ ] Works alongside `observe folder` (interop test)
- [ ] 100+ function codebases handled
- [ ] Syntax errors handled gracefully
- [ ] Function nodes have proper metadata
- [ ] Dependencies detected
- [ ] `converters.py` < 500 lines
- [ ] `Agent_Workspace/` fully documented

Run before confirming:
```bash
pytest tests/test_step_6.py -v
python -m jarvis.cli
> observe_folder tests/
> observe_functions tests/
> display_graph
> exit
```

Should show complete repo map (folders + functions).

---

## Questions?

If stuck:
1. Check `DEVELOPMENT_RULES.md` for general rules
2. Check Step 3 (observers.py) for PythonObserver API
3. Check Step 5 (converters.py) for FolderToGraphConverter pattern
4. Document questions in `Agent_Workspace/Questions.md`

---

## Next Steps (Step 7)

After Step 6 is approved:
- Step 7 creates MetadataManager to enrich these graph nodes
- Functions will have metadata (owner, status, description)
- Both folder and function nodes are fully described

But first: **make Step 6 perfect, test interop, document well**.
