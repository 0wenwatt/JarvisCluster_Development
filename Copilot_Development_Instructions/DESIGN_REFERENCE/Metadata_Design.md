# Metadata Design for Jarvis

**Purpose**: This document describes the structure and purpose of `.metadata.json` files.

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

---

## Metadata Structure

Each `.metadata.json` file has these sections:

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
- "Known issue: file observation doesn't handle symlinks yet"

---

## Goals of Metadata Design

1. **Traceability** — Know what's been implemented, tested, observed
2. **Copilot Context** — Give Copilot enough info to understand the module
3. **Automation** — Enable scripts to parse status, run tests, report health
4. **Documentation** — Self-documenting code without separate docs
5. **Dependency Tracking** — Understand module relationships

---

## Summary

| Section | Purpose |
|---------|---------|
| `general` | Module info |
| `implementation` | Code status |
| `testing` | Test status |
| `functions` | Function list |
| `classes` | Class list |
| `dependencies` | Other modules |
| `copilot_notes` | Development notes |

