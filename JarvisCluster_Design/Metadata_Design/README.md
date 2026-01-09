# Metadata Design for Jarvis

**Purpose**: This document describes the structure and purpose of `.metadata.json` files used throughout Jarvis.

---

## Overview

Every module in Jarvis has a corresponding `.metadata.json` file that tracks:
- General information about the module
- Implementation and test file status
- List of functions/classes in the module
- Notes for Copilot (development instructions, known issues, etc.)

**Goal**: Make the codebase self-documenting and enable Copilot to understand module relationships and status.

---

## Metadata File Naming

**Convention**:
- Implementation file: `module_name.py`
- Metadata file: `module_name.metadata.json`

**Example**:
- File: `graph.py` → Metadata: `graph.metadata.json`
- File: `cli.py` → Metadata: `cli.metadata.json`
- File: `test_functions.py` → Metadata: `test_functions.metadata.json`

---

## Metadata Structure

Each `.metadata.json` file is divided into sections:

```json
{
  "general": {
    "name": "module_name",
    "description": "Brief description of what this module does",
    "version": "0.1",
    "status": "in-development"
  },
  "implementation": {
    "file": "module_name.py",
    "status": "not-started | in-progress | complete",
    "last_updated": "2026-01-09",
    "completion_percentage": 0
  },
  "testing": {
    "file": "module_name_Test.py",
    "status": "not-started | tests-ahead | passing | failing",
    "test_count": 0,
    "passing_tests": 0,
    "failing_tests": 0
  },
  "functions": [
    {
      "name": "function_name",
      "line_number": 42,
      "docstring": "What this function does",
      "parameters": ["param1", "param2"],
      "return_type": "str"
    }
  ],
  "classes": [],
  "dependencies": ["other_module"],
  "copilot_notes": "Any notes for Copilot developers (design decisions, gotchas, etc.)"
}
```

---

## Section Details

### `general`

Basic information about the module.

| Field | Purpose | Example |
|-------|---------|---------|
| `name` | Module name | "graph" |
| `description` | What it does | "Core graph data structure (nodes, edges)" |
| `version` | Current version | "0.1" |
| `status` | Overall status | "in-development" |

### `implementation`

Tracks the implementation file status.

| Field | Purpose | Value |
|-------|---------|-------|
| `file` | Implementation filename | "graph.py" |
| `status` | Development status | "not-started", "in-progress", "complete" |
| `last_updated` | When it was last modified | "2026-01-09" |
| `completion_percentage` | How far along (0-100) | 0-100 |

### `testing`

Tracks test file status and results.

| Field | Purpose | Value |
|-------|---------|-------|
| `file` | Test filename | "graph_Test.py" |
| `status` | Test status | "not-started", "tests-ahead", "passing", "failing" |
| `test_count` | Total number of tests | Integer |
| `passing_tests` | Number passing | Integer |
| `failing_tests` | Number failing | Integer |

**Important**: `status: "tests-ahead"` means tests exist but implementation hasn't started yet (TDD approach).

### `functions`

Array of functions in the module (auto-populated by Step 3.2 observation).

| Field | Purpose |
|-------|---------|
| `name` | Function name |
| `line_number` | Where it's defined in the file |
| `docstring` | Function's docstring |
| `parameters` | List of parameter names |
| `return_type` | Return type (if annotated) |

### `classes`

Array of classes (similar to functions, for future use).

### `dependencies`

List of other modules this module depends on.

### `copilot_notes`

Free-form text for Copilot developers. Examples:
- "Implement Node class before Edge class (Edge depends on Node)"
- "Use ast module for function extraction"
- "Test file already exists; keep tests ahead of implementation"
- "Known issue: file observation doesn't handle symlinks yet"

---

## Example: Fully Populated Metadata

After Steps 1-2 are complete, `graph.metadata.json` might look like:

```json
{
  "general": {
    "name": "graph",
    "description": "Core graph data structure with nodes, edges, and persistence",
    "version": "0.1",
    "status": "complete"
  },
  "implementation": {
    "file": "graph.py",
    "status": "complete",
    "last_updated": "2026-01-10",
    "completion_percentage": 100
  },
  "testing": {
    "file": "graph_Test.py",
    "status": "passing",
    "test_count": 15,
    "passing_tests": 15,
    "failing_tests": 0
  },
  "functions": [
    {
      "name": "save_graph",
      "line_number": 42,
      "docstring": "Save graph to JSON file",
      "parameters": ["graph", "filepath"],
      "return_type": "None"
    },
    {
      "name": "load_graph",
      "line_number": 50,
      "docstring": "Load graph from JSON file",
      "parameters": ["filepath"],
      "return_type": "Graph"
    }
  ],
  "classes": [
    {
      "name": "Node",
      "line_number": 10,
      "docstring": "Represents a node in the graph",
      "methods": ["__init__", "to_dict", "from_dict"]
    },
    {
      "name": "Edge",
      "line_number": 20,
      "docstring": "Represents an edge between two nodes",
      "methods": ["__init__", "to_dict", "from_dict"]
    },
    {
      "name": "Graph",
      "line_number": 30,
      "docstring": "Main graph data structure",
      "methods": ["__init__", "add_node", "remove_node", "add_edge", "remove_edge", "to_dict", "from_dict"]
    }
  ],
  "dependencies": [],
  "copilot_notes": "All requirements met. Ready for Step 3."
}
```

---

## Metadata for Observation Files

When Jarvis **observes** a folder/file (Step 3), it creates METADATA files for each observed item:

**For Folders**:
```json
{
  "type": "folder",
  "copilot_notes": ""
}
```

**For Files**:
```json
{
  "type": "file",
  "copilot_notes": "",
  "functions": [
    "test_functions.py:add",
    "test_functions.py:multiply"
  ]
}
```

These are **simpler** than module metadata because they describe observed filesystem items, not modules.

---

## Goals of Metadata Design

1. **Traceability** — Know what's been implemented, tested, observed
2. **Copilot Context** — Give Copilot enough info to understand the module
3. **Automation** — Enable scripts to parse status, run tests, report health
4. **Documentation** — Self-documenting code without separate docs
5. **Dependency Tracking** — Understand module relationships

---

## Future Expansions

Metadata can grow to include:
- Performance benchmarks
- Code quality metrics (complexity, test coverage)
- Architecture diagrams (as references)
- Integration test results
- Deployment status

But for v0.1, we keep it minimal: **general + implementation + testing + functions + copilot_notes**.

---

## Summary

| Section | Purpose | Auto-Populated? |
|---------|---------|-----------------|
| `general` | Module info | No (manual) |
| `implementation` | Code status | No (manual, updated as work progresses) |
| `testing` | Test status | No (manual, updated after running tests) |
| `functions` | Function list | Yes (by Step 3.2 observer) |
| `classes` | Class list | Yes (future: by observer) |
| `dependencies` | Other modules | No (manual) |
| `copilot_notes` | Development notes | No (manual) |

