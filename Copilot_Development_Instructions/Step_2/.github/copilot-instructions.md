---
applyTo: "jarvis/**,tests/**"
---

# Step 2: Graph, Nodes, Edges - Copilot Instructions

You are implementing **Step 2 of Jarvis v0.1**.

---

## Your Task

Build the **core data structure** for Jarvis:
- `Node` class — represents entities
- `Edge` class — represents relationships
- `Graph` class — manages nodes/edges
- JSON save/load functionality

---

## Test-Driven Development (MANDATORY)

1. **Write tests FIRST** (before any implementation)
2. All test cases are in [../step_2_graph_nodes_edges.md](../step_2_graph_nodes_edges.md)
3. Run: `pytest tests/test_step_2.py -v`
4. **All tests must pass** before proceeding

---

## What You'll Create

```
jarvis/
├── cli.py          ← (from Step 1, no changes needed)
└── graph.py        ← NEW: Node, Edge, Graph classes

tests/
├── test_step_1.py  ← (from Step 1)
└── test_step_2.py  ← NEW: 20+ test cases
```

---

## Files in This Folder

- **[../step_2_graph_nodes_edges.md](../step_2_graph_nodes_edges.md)** — Complete requirements + test specs
- **[../README.md](../README.md)** — Workflow guidance
- **[../DESIGN_REFERENCE/](../DESIGN_REFERENCE/)** — Architecture documentation
- **[Agent_Workspace/](Agent_Workspace/)** — YOUR notes go here

---

## Agent Workspace Rules

⚠️ **Important**: All your working notes go in [Agent_Workspace/](Agent_Workspace/)

- ✅ Create markdown files here (.md files only)
- ✅ Document your progress, design decisions, questions
- ❌ Do NOT create code files here
- 🗑️ **This folder will be deleted when step is done**
- 📦 **Your notes will be copied to the design repo** for knowledge transfer

---

## Workflow

1. **Read** [../step_2_graph_nodes_edges.md](../step_2_graph_nodes_edges.md) completely
2. **Understand** Node, Edge, Graph requirements
3. **Write** `tests/test_step_2.py` (20+ tests from spec)
4. **Implement** `jarvis/graph.py`
5. **Update** `jarvis/cli.py` with new commands (create_node, create_edge, etc.)
6. **Verify** all tests pass
7. **Document** in `Agent_Workspace/`
8. **Tell Owen** — step is complete

---

## Critical Rules

✅ **DO**:
- Write tests FIRST (TDD)
- Keep each file < 500 lines
- Use only Python stdlib
- Implement JSON save/load
- Test with example graphs

❌ **DON'T**:
- Skip tests
- Add validation
- Import external libraries
- Implement Step 3 features
- Look ahead at future steps

---

## Test First Approach

Step 2 requires:
- **20+ test cases** (from spec file)
- Tests for Node, Edge, Graph classes
- Tests for JSON save/load
- Tests for CLI commands

Write all tests first.

---

## Confirmation Checklist

When done, verify:
- ✅ `pytest tests/test_step_2.py -v` — all pass
- ✅ Manual CLI commands work (create_node, display, save, load)
- ✅ JSON save/load preserves graph structure
- ✅ Code < 500 lines per file
- ✅ Notes in `Agent_Workspace/`

Then tell Owen: **"Step 2 complete"**

---

## Next

Once Owen confirms Step 2 is 100% complete:
- ✅ Your code persists (`graph.py`, `test_step_2.py`)
- 🗑️ This folder will be cleared
- 📂 You'll get Step 3 folder

Keep notes in `Agent_Workspace/` for knowledge transfer!
