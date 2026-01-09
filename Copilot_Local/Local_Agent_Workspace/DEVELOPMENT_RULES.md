# Jarvis Development Rules

**This document defines all rules and guidelines for developing in the Jarvis production repository.**

Version: 1.0  
Last Updated: January 9, 2026

---

## Folder Structure Rules

### Root Directory `/jarvis` and `/tests`

These are the ONLY folders allowed in the repository root.

```
jarvis/                    ← Production code (NO FILES HERE)
├── cli.py
├── graph.py
├── observers.py
├── test_functions.py
└── execution.py

tests/                     ← Test files (NO PRODUCTION CODE HERE)
├── test_step_1.py
├── test_step_2.py
└── fixtures/
```

### Creating New Folders in Root

**RULE**: You CANNOT create new folders in root without explicit permission.

If you need a new folder at root level:
1. Ask Owen: "I need a new root folder: `folder_name/`. Reason: [explain]"
2. Wait for approval
3. Create folder only after approval

### Creating Files in Root

**RULE**: NO FILES in repository root (except `.gitignore`, `README.md`, `setup.py`, etc.)

All code MUST go in `/jarvis` or `/tests`.

### Creating Folders in `/jarvis` and `/tests`

**RULE**: You CAN create subfolders in `/jarvis` and `/tests` WITHOUT permission.

Example (allowed without asking):
```
jarvis/
├── converters/       ← NEW (no permission needed)
│   ├── __init__.py
│   ├── folder_converter.py
│   └── function_converter.py
├── metadata/         ← NEW (no permission needed)
│   ├── __init__.py
│   ├── manager.py
│   └── formatter.py
└── integration/      ← NEW (no permission needed)
```

---

## File Creation Rules

### Code Files (`.py`)

**Location**: Must be in `/jarvis` or `/tests`

**Allowed in `/jarvis`**:
- Module files (e.g., `cli.py`, `graph.py`)
- Submodule files (e.g., `converters/folder_converter.py`)
- Test utilities (e.g., `test_fixtures.py`)

**Allowed in `/tests`**:
- Test files (e.g., `test_step_1.py`, `test_step_5.py`)
- Test fixtures (e.g., `fixtures/sample_project/`)
- Conftest files (e.g., `conftest.py`)

### Markdown Files (`.md`)

**Allowed**:
- In `Agent_Workspace/` folder (ONLY)
- Anywhere in this design repo

**Not allowed**:
- In `/jarvis` root
- In `/tests` root
- In production repo root

---

## Metadata Files (`.metadata.json`)

### Location Rules

**METADATA files must match folder/file structure**:

```
jarvis/
├── .metadata.json              ← Module-level metadata
├── graph.py
├── graph.py.metadata.json      ← File-level metadata
├── converters/
│   ├── .metadata.json          ← Folder-level metadata
│   └── folder_converter.py
│   └── folder_converter.py.metadata.json

tests/
├── .metadata.json              ← Test module metadata
└── test_step_5.py
    └── test_step_5.py.metadata.json
```

### Creating Metadata Files

**When**:
- Created by hand during Step 7
- Created programmatically by MetadataManager

**Format** (JSON):
```json
{
  "description": "Brief description",
  "version": "0.1.0",
  "author": "Owen",
  "tags": ["graph", "core"],
  "status": "active",
  "notes": "Optional notes"
}
```

---

## Test Rules

### Test File Naming

**Format**: `test_step_X.py` or `test_step_X_Y.py`

**Examples**:
- `test_step_1.py` — Step 1 tests
- `test_step_3.py` — Step 3.1 tests
- `test_step_3_2.py` — Step 3.2 tests
- `test_step_5.py` — Step 5 tests

### Test Organization

Each test file corresponds to ONE step:
```
tests/
├── test_step_1.py       ← 4 tests (CLI)
├── test_step_2.py       ← 20+ tests (Graph)
├── test_step_3.py       ← 20 tests (Folder observation)
├── test_step_3_2.py     ← 20 tests (Function observation)
├── test_step_4_1.py     ← 18 tests (Functions)
├── test_step_4_2.py     ← 20+ tests (Execution)
├── test_step_5.py       ← 13+ tests (Folder→Graph)
├── test_step_6.py       ← 15+ tests (Functions→Graph)
├── test_step_7.py       ← 18+ tests (Metadata)
├── test_step_8.py       ← 18+ tests (Integration)
└── test_step_9_interop.py   ← 50+ tests (Interop)
```

### Test Requirements

**RULE**: TDD (Test-Driven Development) ALWAYS

1. Write tests FIRST
2. Implement code
3. All tests must pass
4. No test skipping (`@pytest.mark.skip`)

---

## Code Style Rules

### Python Version

**Requirement**: Python 3.7+ compatible

### Imports

**Allowed**:
- Standard library only (no external packages)
- Built-in modules (`os`, `sys`, `json`, `ast`, etc.)

**Not allowed**:
- `pip` packages
- External dependencies
- Third-party libraries

### Type Hints

**Requirement**: All functions must have type hints

**Example**:
```python
def add_node(self, node_id: str, label: str) -> Node:
    """Add a node to the graph."""
    pass
```

### Docstrings

**Requirement**: All functions must have docstrings

**Example**:
```python
def add_node(self, node_id: str, label: str) -> Node:
    """
    Add a node to the graph.
    
    Args:
        node_id: Unique identifier for the node
        label: Human-readable label
        
    Returns:
        The created Node object
    """
    pass
```

### Line Length

**Requirement**: Maximum 100 characters per line

### File Size

**Requirement**: Keep files < 400-500 lines

**When a file gets too large**:
1. Split into submodules
2. Create new folder (if in `/jarvis`, no permission needed)
3. Move related code

---

## Agent_Workspace Rules

### What You CAN Do

- Create `.md` files (markdown ONLY)
- Document progress
- Write notes for Owen
- List questions
- Record decisions

### What You CANNOT Do

- Create `.py` files (code goes in `/jarvis` or `/tests`)
- Create non-markdown files
- Run tests here
- Build here

### Agent_Workspace Lifecycle

1. **Created** at start of step
2. **Used** to document learnings
3. **Reviewed** by Owen after step
4. **Copied** to design repo (permanent record)
5. **Deleted** after step approval

### What to Document

Create these files in `Agent_Workspace/`:

- `Progress.md` — What you did, what works
- `Questions.md` — Questions for Owen
- `Decisions.md` — Key design decisions made
- `Challenges.md` — Problems faced, solutions found
- `Integration_Notes.md` — How this step integrates with others

---

## Git Rules

### Commits

**Format**: Clear, descriptive commit messages

```
Step 1: Implement basic CLI
- Add CLI class
- Implement command loop
- Add 4 tests
```

### Branches

**One branch per step** (if needed):
```
main
├── step-1-cli
├── step-2-graph
└── step-5-folder-to-graph
```

### Code Review

Before merging:
- [ ] All tests pass
- [ ] No linting errors
- [ ] Agent_Workspace documented
- [ ] Owen approved

---

## Command Line Tools

### Available Commands (Step 1+)

```bash
# CLI Commands (Step 1)
python -m jarvis.cli
  > echo hello          # Echo command
  > exit               # Exit program

# Graph Commands (Step 2)
> create_node id1 "Node 1"
> create_edge id1 id2 "connected"
> display_graph
> save_graph graph.json
> load_graph graph.json

# Observation Commands (Step 3)
> observe_folder <path>
> observe_functions <path>

# Execution Commands (Step 4)
> run start_node

# Analysis Commands (Step 5+)
> analyze <path>
> query <property> <value>
> metadata show <node_id>
> metadata edit <node_id> <key> <value>
```

### Adding New Commands

To add a new command:

1. Create function in appropriate module (e.g., `cli.py`)
2. Add command to CLI dispatch in `cli.py`
3. Write tests in appropriate `test_step_X.py`
4. Document in Agent_Workspace/Decisions.md
5. Update this list if it's a user-facing command

---

## Rules for Future Expansion

### When Adding New Commands

1. Add command name to this document
2. Specify in step's `copilot-instructions.md`
3. Write tests first
4. Document in Agent_Workspace

### When Adding New Folders

1. **In root?** → Ask permission
2. **In `/jarvis`?** → Create freely
3. **In `/tests`?** → Create freely

### When Adding New File Types

Update this document BEFORE implementation.

---

## Error Handling Rules

### Graceful Degradation

All failures should be graceful:
- Catch errors
- Log them
- Continue execution
- Don't crash entire program

**Example**:
```python
try:
    observe_folder(path)
except PermissionError:
    logger.warning(f"Permission denied: {path}")
    continue  # Don't crash
```

### Edge Cases

Always handle:
- Empty input
- Missing files
- Invalid data
- Syntax errors in observed code
- Circular dependencies

---

## Performance Rules

### For v0.1 & v0.2

- No optimization needed yet
- Keep code readable
- Focus on correctness

### For v0.3+

- Queries should complete in < 100ms
- Large graphs (500+ functions) should be supported
- Memory usage reasonable for typical projects

---

## Documentation Rules

### In Production Code

Every module should have:
- Module docstring (at top)
- Class docstrings
- Function docstrings
- Inline comments for complex logic

### In Tests

Test names should be descriptive:
```python
def test_graph_add_node_creates_node_with_id():
    # Good

def test_add():
    # Bad (unclear what it tests)
```

### In Agent_Workspace

After each step, document:
- What was built
- How it integrates with existing code
- Questions encountered
- Decisions made

---

## Approval Workflow

### Before Starting a Step

1. Read step's `copilot-instructions.md`
2. Read step's `step_X_*.md` specification
3. Review this DEVELOPMENT_RULES.md
4. Ask questions in Agent_Workspace/Questions.md

### During Step

1. Write tests first
2. Implement code to pass tests
3. Follow all rules above
4. Document in Agent_Workspace

### After Step

1. All tests pass ✅
2. No linting errors ✅
3. Agent_Workspace fully documented ✅
4. Owen reviews and approves ✅

---

## Rule Updates

This document will grow as new features are added.

When Owen adds new rules:
1. They'll be added here first
2. Then referenced in step `copilot-instructions.md` files
3. Agents will be notified

Current version: **1.0**

Last updated by Owen: January 9, 2026
