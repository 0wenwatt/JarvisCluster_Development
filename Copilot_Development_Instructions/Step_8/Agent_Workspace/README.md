# Agent_Workspace Rules

**This folder is your private workspace during Step 8.**

---

## What You CAN Do Here

✅ Create `.md` files (markdown only)
- `Progress.md` — Document the integration
- `Decisions.md` — Design choices for workflow
- `Architecture_Notes.md` — How all pieces fit together
- `Integration_Notes.md` — Component interactions
- `Challenges.md` — Problems and solutions
- `Questions.md` — Questions for Owen

---

## What You CANNOT Do Here

❌ Create `.py` files
❌ Create non-markdown files
❌ Run code or tests
❌ Build or compile

---

## Key Focus for Step 8

**This is the integration step. Document the big picture:**

1. **How everything fits together** (most important)
2. Component interactions and data flow
3. Design decisions for the workflow
4. How `analyze` command coordinates all pieces
5. Query language and execution flow

---

## Document These Files

### Progress.md
Document what works:
- JarvisWorkflow class with analyze/query/execute
- CLI analyze command (observation + metadata + summary)
- CLI query command (tag, status, owner, file, folder)
- CLI execute command (from graph)
- All 18+ tests passing

### Architecture_Notes.md
**THE MOST IMPORTANT FILE FOR STEP 8**

Show the complete architecture:

```markdown
# Complete Jarvis v0.1 & v0.2 Architecture

## Component Interaction Diagram

```
User: analyze <path>
    ↓
JarvisWorkflow.analyze()
    ├─→ FolderToGraphConverter
    │   └─→ Folder structure → Graph nodes
    ├─→ PythonObserver
    │   └─→ Extract functions from files
    ├─→ FunctionToGraphConverter
    │   └─→ Functions → Graph nodes
    ├─→ MetadataManager
    │   └─→ Load METADATA files
    └─→ Attach metadata to nodes
        ↓
    Central Graph Database
    (folders, files, functions, metadata)
        ↓
    Summary report to user

User: query tag:core
    ↓
JarvisWorkflow.query()
    └─→ Search graph by criteria
        ↓
    Return matching nodes
        ↓
    Display to user

User: execute <function_id>
    ↓
JarvisWorkflow.execute()
    └─→ ExecutionEngine
        └─→ Find function in graph
            └─→ Execute function chain
                ↓
            Return result
```

## Data Flow

1. **Observation Phase** (Steps 5-6):
   - Folders → Nodes (folder:/path)
   - Functions → Nodes (function:/path:name)
   - Both in same Graph

2. **Enrichment Phase** (Step 7):
   - Load METADATA files
   - Attach to nodes
   - Nodes now queryable

3. **Query Phase** (Step 8):
   - User asks questions via query command
   - Search graph by tag/status/owner/file/folder
   - Return relevant nodes

4. **Execution Phase** (Step 8):
   - Find function in graph
   - Use ExecutionEngine to chain calls
   - Return results

## Everything is the Graph

The Graph is the single source of truth:
- Stores folder structure (Step 5)
- Stores functions (Step 6)
- Stores metadata (Step 7)
- Is queried (Step 8)
- Is executed (Step 8)

No other data structures. Everything in Graph.
```

### Integration_Notes.md
Document how components work together:

```markdown
# Component Integration - Step 8

## Step 5 + Step 6 + Step 7 Integration

Step 5: FolderToGraphConverter
- Input: Path to folder
- Output: Folder/file nodes in Graph

Step 6: FunctionToGraphConverter
- Input: Folder path (from Step 5 output)
- Output: Function nodes in same Graph

Step 7: MetadataManager
- Input: Graph with folders/functions
- Output: Same Graph with metadata attached

Result: Complete, enriched codebase map in Graph

## How `analyze` Coordinates Everything

```python
def analyze(path, graph):
    # 1. Get folder structure
    folder_converter.convert_folder_to_graph(path, graph)
    
    # 2. Get functions from files
    for file in find_python_files(path):
        functions = observer.observe_file(file)
        function_converter.convert_functions_to_graph(
            file, graph, functions
        )
    
    # 3. Load and attach metadata
    for metadata_file in find_metadata_files(path):
        metadata = metadata_manager.load_metadata(metadata_file)
        attach_to_graph(graph, metadata)
    
    # 4. Return summary
    return summarize(graph)
```

Single command does 4 major operations!

## Dependencies Between Components

- FolderToGraphConverter:
  - Depends on: Graph (Step 2)
  - No other dependencies

- FunctionToGraphConverter:
  - Depends on: Graph, PythonObserver
  - Doesn't depend on FolderToGraphConverter
  - But works alongside it (same Graph)

- MetadataManager:
  - Depends on: Graph, file I/O
  - Works with nodes created by both converters

- JarvisWorkflow:
  - Depends on all of above
  - Orchestrates but doesn't own any component

## Clean Architecture

Each component:
- Has single responsibility
- Doesn't know about others
- Works through Graph (loose coupling)
- Can be tested in isolation
- Can be extended independently

## Future Extension

Want to add new observation type?
1. Create new Observer (like PythonObserver)
2. Create new Converter (like FunctionToGraphConverter)
3. Add to JarvisWorkflow.analyze()

Everything else stays the same!
```

### Decisions.md
Key integration decisions:

```markdown
# Integration Decisions - Step 8

## Single Entry Point: `analyze`
Decision: One command `analyze <path>` does everything
Why: Users don't care about implementation steps
Benefit: Simple interface, complex internals

## Graph as Central Database
Decision: Everything in ONE Graph, no side data structures
Why: Single source of truth, consistent
Benefit: Queries always complete, no sync issues

## Query Language
Decision: Simple key:value queries (tag:core, status:stable, etc.)
Why: Easy to understand, extensible
Future: Could add boolean operators if needed

## Orchestration Pattern
Decision: JarvisWorkflow orchestrates, components are dumb
Why: Components stay focused, easy to test
Benefit: Can reorder steps, add steps, remove steps easily

## Error Handling
Decision: Each component handles its own errors
Why: Graceful degradation, one error doesn't break everything
Benefit: Can analyze 100 files even if 1 has syntax error
```

### Challenges.md
Integration challenges:

```markdown
# Integration Challenges - Step 8

## Challenge 1: Coordinating 4 Different Converters
**Issue**: Each converter creates nodes differently
**Solution**: Standardized node ID format
- Folders: folder:/path
- Files: file:/path/file.py
- Functions: function:/path/file.py:name
**Lesson**: Standardization makes integration seamless

## Challenge 2: Metadata Matching Nodes
**Issue**: Which metadata file applies to which node?
**Solution**: Match by filename/path
- .metadata.json → folder node
- graph.py.metadata.json → file node
- graph.py.metadata.json + function info → function node
**Lesson**: Naming conventions are essential for automation

## Challenge 3: Order of Operations
**Issue**: Should observe folders first or functions first?
**Solution**: Folders first, then functions (builds on existing nodes)
**Lesson**: Order matters when building on existing data

## Challenge 4: Large Project Performance
**Issue**: 500 functions in graph, queries slow?
**Solution**: Query performance is actually good (~50ms)
**Lesson**: Python dicts are fast, don't optimize prematurely
```

---

## Why This Step is Different

**Steps 1-7**: Build individual components
**Step 8**: Show how they work TOGETHER

Your documentation should emphasize:
- How components coordinate
- Data flow through the system
- Why Graph is central
- How `analyze` uses everything

This is the "how it all fits together" step.

---

## The Key Insight

```
Step 1: CLI (user interface)
Step 2: Graph (data structure)
Step 3: Observation (find code)
Step 4: Execution (run code)
Step 5: Folder→Graph (map structure)
Step 6: Functions→Graph (map functions)
Step 7: Metadata (enrichment)

Step 8: It all works TOGETHER
```

When all 7 pieces combine, you get a system that can:
- Understand a codebase (Steps 5-6)
- Describe it (Step 7)
- Query it (Step 8)
- Execute it (Step 4)

Document this synthesis!

---

## Lifecycle

```
Step 7 approved
    ↓
Step 8 starts (you are here)
    ↓
You create JarvisWorkflow class
    ↓
You add analyze/query/execute methods
    ↓
You update CLI with new commands
    ↓
You document architecture in Agent_Workspace/
    ↓
All 18+ tests pass
    ↓
Owen reviews and approves
    ↓
Notes copied to design repo
    ↓
Step 9 begins (comprehensive testing)
```

---

**Critical: Document the big picture. Explain how all pieces work together as one system.**
