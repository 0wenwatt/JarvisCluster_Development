# Step 3 & 3.2: Code Observation (Folders & Functions)

This step combines **Step 3** (Folder Observation) and **Step 3.2** (Function Observation) since they work together in the same `observers.py` module.

---

## Part 1: Step 3 - Basic Observation (Folder Tree)

**Status**: Ready to implement  
**Estimated Time**: 2-3 hours  
**Complexity**: Medium  
**Prerequisite**: Steps 1 & 2 complete ✅  

### Overview

Step 3 teaches Jarvis to **observe its own folder structure** and represent it as a Graph. This is the first step where Jarvis begins to become "aware" of its environment.

By the end of this step:
- Jarvis can scan a folder and create nodes for folders and files
- Jarvis understands the folder hierarchy (parent→child relationships)
- Jarvis creates METADATA files alongside observed folders/files
- Jarvis can save the observation as a graph

---

### Exact Requirements - Step 3

#### 3.1 FolderObserver Class

**Location**: `jarvis/observers.py` (NEW file)

Create a `FolderObserver` class:

```python
class FolderObserver:
    
    Methods:
    - __init__()
    
    - observe(root_path: str) -> Graph:
      • Scans folder at root_path
      • Creates nodes for:
        - The root folder itself
        - All immediate subfolders (1 level deep)
        - All immediate files (1 level deep)
      • Creates edges:
        - root folder → each subfolder
        - root folder → each file
      • Creates METADATA files (see section 3.2)
      • Returns Graph with all nodes/edges
      
      Constraints:
      - Only 1 level deep (no recursion into subdirectories)
      - Handles missing folders gracefully
      - No crash on permission errors (skip silently)
      - All node IDs are unique
      - File nodes have path as part of ID
      
      Example:
        If observing /home/user/jarvis/:
        - Node: id="root_folder", label="/home/user/jarvis"
        - Subfolder "src" → Node: id="src_folder", label="src"
        - File "config.yaml" → Node: id="config.yaml_file", label="config.yaml"
        - Edge: root_folder → src_folder
        - Edge: root_folder → config.yaml_file
```

#### 3.2 METADATA File Creation

**Important**: METADATA files are created alongside each observed folder/file.

**Location**: Same directory as the observed file/folder

**Naming Convention**:
- For folder: `{folder_name}.metadata.json`
- For file: `{filename}.metadata.json`

**File Format** (exactly):

```json
{
  "type": "folder",
  "copilot_notes": ""
}
```

or for files (updated in Step 3.2 with functions list):

```json
{
  "type": "file",
  "copilot_notes": "",
  "functions": []
}
```

**Constraints**:
- Create METADATA for EVERY folder and file observed
- METADATA is always valid JSON
- `type` is either "file" or "folder"
- `copilot_notes` starts empty (for future expansion)
- METADATA survives across observations (don't overwrite if already exists)

#### 3.3 CLI Command

**Location**: Update `jarvis/cli.py`

Add this command:

| Command | Syntax | Behavior |
|---------|--------|----------|
| `observe` | `observe <folder_path>` | Scan folder and create graph |

**Behavior**:
- Scan folder at `<folder_path>`
- Use `FolderObserver` to create graph
- Display result (use graph's `display()` method)
- Save result as `observation.json` in current directory
- Print confirmation message

**Example**:
```
jarvis> observe tests/test_folder
Graph: 5 nodes, 4 edges
Nodes:
  - test_folder: tests/test_folder
  - subfolder_a: subfolder_a
  - subfolder_b: subfolder_b
  - file_1.txt: file_1.txt
  - file_2.py: file_2.py
Edges:
  - test_folder → subfolder_a
  - test_folder → subfolder_b
  - test_folder → file_1.txt
  - test_folder → file_2.py

Observation saved to observation.json
```

---

## Part 2: Step 3.2 - Extend Observation to Functions

**Status**: Ready to implement  
**Estimated Time**: 2-3 hours  
**Complexity**: Medium  
**Prerequisite**: Step 3 complete ✅  

### Overview

Step 3.2 extends the observer to understand **Python code structure**. Jarvis can now parse `.py` files and extract function definitions.

By the end of this step:
- Jarvis can scan Python files and find all function definitions
- Function nodes are created and linked to their parent file
- METADATA files for files include a list of contained functions
- Integration with the existing `observe` command

---

### Exact Requirements - Step 3.2

#### 3.2.1 PythonObserver Class

**Location**: `jarvis/observers.py` (same file as FolderObserver)

Create a `PythonObserver` class:

```python
class PythonObserver:
    
    Methods:
    - __init__()
    
    - observe_functions(file_path: str) -> list:
      • Parse Python file at file_path using ast module
      • Extract all top-level function definitions
      • For each function, capture:
        - Function name
        - Line number where defined
      • Return list of dicts:
        [
          {"name": "function_name", "line_number": 42},
          {"name": "another_func", "line_number": 85},
        ]
      
      Constraints:
      - Only top-level functions (not class methods, not nested)
      - Use Python ast module (standard library)
      - Gracefully handle syntax errors (skip file, return empty list)
      - Return list even if empty
```

#### 3.2.2 Integration with FolderObserver

Update the `FolderObserver.observe()` method to:

1. When observing a folder, **also observe Python files**
2. For each `.py` file found:
   - Call `PythonObserver.observe_functions()` to get function list
   - Create a node for each function
   - Create edge from file node → each function node
   - Update file METADATA to include function list

#### 3.2.3 Function Node Structure

When a function is found, create a node with:

```
Node:
  id: "{filename}:{function_name}"  # Unique within the graph
  label: function_name               # Just the name
  metadata: {
    "type": "function",
    "line_number": N,
    "copilot_notes": ""
  }
```

**Example**:
```
File: jarvis/graph.py
Functions:
  - add_node() on line 25
  - remove_node() on line 45

Nodes created:
  id="graph.py:add_node", label="add_node", metadata={type: "function", line_number: 25}
  id="graph.py:remove_node", label="remove_node", metadata={type: "function", line_number: 45}

Edges created:
  graph.py → graph.py:add_node
  graph.py → graph.py:remove_node
```

#### 3.2.4 Updated File METADATA

When a Python file is observed, update its METADATA:

```json
{
  "type": "file",
  "copilot_notes": "",
  "functions": [
    "graph.py:add_node",
    "graph.py:remove_node"
  ]
}
```

**Constraints**:
- `functions` array contains function node IDs
- List is empty for non-Python files
- Only top-level functions included

#### 3.2.5 Enhanced CLI Command

The existing `observe` command now also:
- Automatically detects `.py` files
- Calls `PythonObserver` for each `.py` file
- Creates function nodes and edges
- Updates METADATA files

---

## Code Organization

```
jarvis/
├── __init__.py
├── cli.py                   (updated from Step 1-2)
├── graph.py                 (from Step 2)
└── observers.py             (NEW: FolderObserver + PythonObserver)
```

**Constraints**:
- `observers.py` must be < 500 lines total
- Imports: `os`, `pathlib`, `json`, `ast`
- Two classes: `FolderObserver` and `PythonObserver`

---

## Test Data

- `tests/test_folder/` — Example folder with subfolders and files
- `tests/test_functions.py` — Python file with 5 functions (add, multiply, concat, uppercase, length)

Both already exist. Do not modify them.

---

## Tests to Write FIRST

**CRITICAL**: Write these tests **before** implementing observers.

### Test File: `tests/test_step_3.py` (Part 1)

Cover basic folder observation:

```python
def test_observe_test_folder():
    # Observe tests/test_folder
    # Verify: Graph has 5 nodes (root + 2 folders + 2 files)
    # Verify: Graph has 4 edges (root to each subfolder/file)

def test_folder_nodes_created():
    # Observe tests/test_folder
    # Verify: root folder node exists
    # Verify: subfolder nodes exist
    # Verify: each folder node has correct label

def test_file_nodes_created():
    # Observe tests/test_folder
    # Verify: file nodes created for .txt and .py files
    # Verify: each file node has correct label

def test_folder_to_subfolder_edges():
    # Observe tests/test_folder
    # Verify: edge exists from root to each subfolder

def test_folder_to_file_edges():
    # Observe tests/test_folder
    # Verify: edge exists from root to each file

def test_metadata_files_created():
    # Observe tests/test_folder
    # Verify: METADATA files created for all folders and files

def test_metadata_file_format():
    # Observe tests/test_folder
    # Read any METADATA file
    # Verify: file is valid JSON
    # Verify: has "type" key (either "file" or "folder")
    # Verify: has "copilot_notes" key (string)

def test_metadata_file_content():
    # Observe tests/test_folder
    # Verify types are correct (folder vs file)

def test_observation_save():
    # Observe tests/test_folder
    # Verify: observation.json file is created
    # Verify: file is valid JSON

def test_observation_load():
    # Observe tests/test_folder (saves to observation.json)
    # Load observation.json
    # Verify: loaded graph matches original

def test_cli_observe_command():
    # Simulate CLI: "observe tests/test_folder"
    # Verify: graph is displayed
    # Verify: observation.json is created
    # Verify: METADATA files created in test_folder

def test_observe_empty_folder():
    # Create a temporary empty folder
    # Observe it
    # Verify: only 1 node (the root folder itself)
    # Verify: 0 edges

def test_observe_folder_with_only_files():
    # Create temp folder with 3 files, no subfolders
    # Observe it
    # Verify: 4 nodes (root + 3 files)
    # Verify: 3 edges (root to each file)

def test_observe_folder_with_only_subfolders():
    # Create temp folder with 3 subfolders, no files
    # Observe it
    # Verify: 4 nodes (root + 3 folders)
    # Verify: 3 edges (root to each folder)

def test_metadata_persistence():
    # Observe test_folder once
    # Verify METADATA files exist
    # Observe test_folder again
    # Verify: METADATA files are not corrupted
    # (Bonus) if METADATA already exists, don't overwrite

def test_node_ids_unique():
    # Observe test_folder
    # Verify: all node IDs are unique
    # Verify: no duplicate IDs in graph
```

### Test File: `tests/test_step_3_2.py` (Part 2)

Cover Python function observation:

```python
def test_observe_functions_simple():
    # Observe tests/test_functions.py
    # Verify: 5 functions found (add, multiply, concat, uppercase, length)

def test_function_extraction_names():
    # Observe tests/test_functions.py
    # Get list of functions
    # Verify: all 5 expected functions present

def test_function_extraction_line_numbers():
    # Observe tests/test_functions.py
    # Verify: each function has "line_number" key
    # Verify: line numbers are integers and reasonable

def test_python_observer_empty_file():
    # Create temp Python file with no functions
    # Observe it
    # Verify: returns empty list

def test_python_observer_syntax_error():
    # Create temp Python file with syntax error
    # Observe it
    # Verify: doesn't crash
    # Verify: returns empty list

def test_observe_with_python_files():
    # Observe tests/ folder (contains test_functions.py)
    # Verify: file node created for test_functions.py
    # Verify: function nodes created
    # Verify: edges from file to each function

def test_function_node_creation():
    # Observe tests/test_functions.py
    # Create graph
    # Verify: nodes exist with id="test_functions.py:add", etc.
    # Verify: labels are just function names

def test_function_metadata_format():
    # Observe tests/test_functions.py
    # Get a function node
    # Verify: metadata has "type": "function"
    # Verify: metadata has "line_number" (integer)

def test_file_metadata_updated():
    # Observe tests/test_functions.py
    # Read test_functions.py.metadata.json
    # Verify: has "functions" array
    # Verify: array contains function IDs

def test_file_metadata_functions_list():
    # Observe tests/test_functions.py
    # Verify functions list contains all 5 functions

def test_observe_multiple_python_files():
    # Create temp folder with 2 Python files
    # File 1: 3 functions
    # File 2: 2 functions
    # Observe folder
    # Verify: correct number of nodes and edges

def test_file_node_edges_to_functions():
    # Observe tests/test_functions.py
    # Verify: edge exists from file node to each function node

def test_cli_observe_with_python_files():
    # Simulate CLI: "observe tests/"
    # Verify: output shows function nodes

def test_observation_save_with_functions():
    # Observe tests/test_functions.py
    # Save as observation.json
    # Verify: JSON includes function nodes and edges

def test_observation_load_with_functions():
    # Observe tests/test_functions.py
    # Load observation.json
    # Verify: loaded graph has same function nodes

def test_function_node_ids_unique():
    # Observe tests/ with multiple Python files
    # Verify: all function node IDs are unique

def test_non_python_files():
    # Observe test_folder (contains .txt and .py files)
    # Verify: only .py files get function parsing
    # Verify: .txt file node has no functions array in metadata
```

---

## Implementation Checklist

### Phase 1: Write All Tests
- [ ] Create `tests/test_step_3.py` (folder observation tests)
- [ ] Create `tests/test_step_3_2.py` (function observation tests)
- [ ] Write all test cases (listed above, 40+ total)
- [ ] Run tests — they will fail (expected)
- [ ] Verify no syntax errors

### Phase 2: Implement FolderObserver
- [ ] Create `jarvis/observers.py`
- [ ] Implement `FolderObserver` class
- [ ] Implement `observe()` method
- [ ] Scan folders (1 level only)
- [ ] Create nodes and edges
- [ ] Create METADATA files

### Phase 3: Implement PythonObserver
- [ ] Add `PythonObserver` class to same file
- [ ] Implement `observe_functions()` method
- [ ] Use `ast` module to parse `.py` files
- [ ] Extract function names and line numbers
- [ ] Handle syntax errors gracefully

### Phase 4: Integrate Both
- [ ] Update `FolderObserver.observe()` to call `PythonObserver`
- [ ] Create function nodes and edges
- [ ] Update file METADATA with function list

### Phase 5: Update CLI
- [ ] Update `jarvis/cli.py`
- [ ] Add `observe` command (if not from Step 3)
- [ ] Call `FolderObserver.observe()`
- [ ] Display result
- [ ] Save to `observation.json`

### Phase 6: Run All Tests
- [ ] Run: `pytest tests/test_step_3.py -v`
- [ ] Run: `pytest tests/test_step_3_2.py -v`
- [ ] All tests pass ✅

### Phase 7: Manual Testing
- [ ] Run CLI: `observe tests/test_folder`
- [ ] Verify folder structure observed
- [ ] Verify METADATA files created
- [ ] Run CLI: `observe tests/test_functions.py`
- [ ] Verify functions extracted
- [ ] Load observation.json and verify

---

## How to Confirm This Step Works

### Automated Testing
```bash
pytest tests/test_step_3.py tests/test_step_3_2.py -v
```

**Expected**: All tests pass ✅

### Manual Testing - Folder Observation

```
jarvis> observe tests/test_folder
```

**Expected output** (shows 5 nodes and folder structure)

### Manual Testing - Function Observation

```
jarvis> observe tests/test_functions.py
```

**Expected output** (shows file + 5 function nodes)

### Check METADATA Files

After observing, verify files exist:
```
tests/test_folder.metadata.json
tests/test_folder/folder_a.metadata.json
tests/test_folder/file_1.txt.metadata.json
tests/test_functions.py.metadata.json
```

With correct format and function lists.

### Load and Verify

```
jarvis> load observation.json
jarvis> display
```

**Expected**: Same graph as before

### What Owen Will Check
- ✅ All pytest tests pass (both test_step_3 and test_step_3_2)
- ✅ CLI observe command works for folders and Python files
- ✅ METADATA files created and formatted correctly
- ✅ Function nodes extracted correctly with line numbers
- ✅ observation.json is valid and reloadable
- ✅ Code is < 500 lines
- ✅ Only 1 level folder depth, only top-level functions

---

## Critical Notes

### DO
- ✅ Write ALL tests first (both test_step_3 and test_step_3_2)
- ✅ Only scan 1 level deep for folders
- ✅ Extract only top-level functions
- ✅ Create METADATA for everything
- ✅ Use only stdlib (os, pathlib, json, ast)
- ✅ Handle missing/empty folders and syntax errors gracefully

### DO NOT
- ❌ Recursively scan all subdirectories
- ❌ Parse file contents (except for functions in .py)
- ❌ Extract class methods or nested functions
- ❌ Validate METADATA schema
- ❌ Add compression or caching
- ❌ Implement features for Step 4+

---

## Next Step

Once this step is complete and Owen confirms:
1. All tests pass ✅ (both test_step_3 and test_step_3_2)
2. Manual CLI testing works ✅
3. METADATA files correct ✅
4. Function nodes extracted accurately ✅
5. Code meets all requirements ✅

**Move to Step 4: Execution Engine**

---

## Questions or Stuck?

1. Re-read "Exact Requirements"
2. Check test examples
3. Verify folder structure and function extraction
4. Ask Owen before proceeding to Step 4

**Do not move forward until both you and Owen confirm this step is 100% complete.**
