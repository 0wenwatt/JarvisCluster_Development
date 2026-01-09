# Agent_Workspace Rules

**This folder is your private workspace during Step 7.**

---

## What You CAN Do Here

✅ Create `.md` files (markdown only)
- `Progress.md` — Document what you built
- `Decisions.md` — Record design choices
- `Metadata_Format_Notes.md` — JSON format decisions
- `Integration_Notes.md` — How metadata enriches the graph
- `Challenges.md` — Problems and solutions
- `Questions.md` — Questions for Owen

✅ Write notes about:
- Metadata file format and structure
- How metadata attaches to graph nodes
- Example metadata files created
- Query patterns (by tag, status, owner, etc.)

---

## What You CANNOT Do Here

❌ Create `.py` files
❌ Create non-markdown files
❌ Run code or tests
❌ Build or compile

---

## Key Focus for Step 7

**Most important to document**:
1. Why you created example METADATA files by hand
2. The metadata JSON schema/format
3. How metadata enriches graph nodes (nodes stay central)
4. Query patterns and capabilities
5. How this integrates Steps 5 & 6 (makes them queryable)

---

## Document These Files

### Progress.md
- MetadataManager class created ✅
- 25+ tests written and passing ✅
- 3 example METADATA files created:
  - jarvis/.metadata.json
  - jarvis/graph.py.metadata.json
  - tests/.metadata.json
- CLI metadata_show and metadata_edit working ✅

### Decisions.md
Key decisions to document:
- **Metadata file location**: `.metadata.json` alongside targets
- **Format**: JSON with description, status, tags, author, etc.
- **Attachment**: Metadata enhances Node objects (doesn't replace them)
- **Inheritance**: Do child nodes inherit parent metadata? (your choice)
- **Validation**: What makes valid metadata?
- **Queries**: tag, status, owner patterns

### Metadata_Format_Notes.md
Document the format you chose:

```markdown
# Metadata JSON Format

## Module-level (.metadata.json)
```json
{
  "description": "What this module does",
  "version": "0.2.0",
  "author": "Owen",
  "tags": ["tag1", "tag2"],
  "status": "active|deprecated|planned",
  "notes": "Optional additional notes"
}
```

## File-level (file.py.metadata.json)
```json
{
  "description": "What this file does",
  "status": "active",
  "author": "Owen",
  "tags": ["core", "important"],
  "key_functions": ["func1", "func2"],
  "dependencies": [],
  "notes": "..."
}
```

## Why this format?
- Simple, extensible JSON
- Matches node structure (easy to attach)
- Queryable by all fields
- Human-readable
```

### Integration_Notes.md
Most important section! Document:

```markdown
# Integration - Step 7

## How Metadata Enriches Graph

Before Step 7:
```
Node(id="function:jarvis/graph.py:add_node", label="add_node")
```

After Step 7:
```
Node(id="function:jarvis/graph.py:add_node", label="add_node")
  .metadata = {
    "description": "Add node to graph",
    "status": "stable",
    "tags": ["core", "graph"],
    "author": "Owen"
  }
```

## Queries Become Powerful

Find all deprecated functions:
```python
query(graph, "status:deprecated")
```

Find all functions by Owen:
```python
query(graph, "owner:Owen")
```

Find all core functions:
```python
query(graph, "tag:core")
```

## Bridges Steps 5, 6, and 7

- Step 5: Creates folder structure in Graph
- Step 6: Creates functions in Graph
- Step 7: Enriches both with metadata
- Step 8: Queries the enriched graph
- Result: Complete, queryable codebase map
```

### Challenges.md
Document any issues:
- METADATA file discovery (where to look)
- Metadata validation (what's required vs optional)
- Conflicting metadata (same node, multiple files)
- Inheritance (do nested folders inherit parent metadata)
- Performance (loading many METADATA files)

---

## Example Progress Entry

```markdown
# Step 7 Progress

## Completed
- [x] MetadataManager class with load/save/query
- [x] 25+ tests written and passing
- [x] 3 example METADATA files created by hand
- [x] CLI metadata_show command
- [x] CLI metadata_edit command
- [x] Metadata attachment to graph nodes

## Example METADATA Files Created
1. `jarvis/.metadata.json` (module description)
2. `jarvis/graph.py.metadata.json` (file description, key functions)
3. `tests/.metadata.json` (test module description)

## How It Works
1. MetadataManager loads .metadata.json files
2. Files matched to nodes by path/filename
3. Metadata dict attached to node.metadata
4. Queries can now search by tag/status/owner

## Integration Points
- Works with Graph from Step 2 ✅
- Works with folder nodes from Step 5 ✅
- Works with function nodes from Step 6 ✅
- Queried by integration layer in Step 8 ✅

## Performance
- Load 100 metadata files: ~0.5 seconds ✅
- Attach to 1000 nodes: ~0.2 seconds ✅
- Query 1000 nodes: ~0.05 seconds ✅
```

---

## The Bridge Step

Step 7 is the "bridge" that connects everything:
- **Input**: Folders and functions from Steps 5 & 6
- **Action**: Enrich with metadata
- **Output**: Rich, queryable graph

Your documentation should make this clear.

---

## Remember

You create example METADATA files **by hand**. This shows:
1. What a METADATA file looks like
2. What information should be captured
3. How to document a codebase
4. A template others can copy

Document this process! Make it clear why you created what you did.

---

## Lifecycle

```
Step 6 approved
    ↓
Step 7 starts (you are here)
    ↓
You create MetadataManager class
    ↓
You create 3 example METADATA files BY HAND
    ↓
You test metadata attachment to graph
    ↓
You document in Agent_Workspace/
    ↓
All 25+ tests pass
    ↓
Owen reviews and approves
    ↓
Notes copied to design repo
    ↓
Step 8 begins (integration layer)
```

---

**Key insight: Metadata is the glue that makes the graph truly useful. Document this bridge role clearly.**
