# Agent Workspace Rules & Organization

**Rules for how to use and organize the Agent_Workspace folder during development.**

---

## What is Agent_Workspace?

A **temporary working area** for you (the agent) during a step:
- Document your progress
- Track decisions
- Note questions/blockers
- Share learnings

**CRITICAL**: This entire folder is **DELETED when the step completes**.

---

## Structure

```
Agent_Workspace/
├── README.md            ← Required: Your notes and progress
├── TODO.md             ← Optional: What you're working on
├── DECISIONS.md        ← Optional: Why you made choices
└── ⚠️ NOTHING ELSE
```

### Files You MUST Create

**README.md** - Your progress log
- What you did
- What you learned
- Current status
- What's next

---

## File Purposes

### README.md (REQUIRED)

Your main progress document. Format:

```markdown
# Step X Development Progress

## Status
- Phase: [Planning/Implementation/Testing]
- Completion: [X%]
- Last Updated: [Date/Time]

## What I Did Today
1. Started implementing CLI
2. Created test cases
3. Fixed bug in graph.py
4. Questions about...

## What Worked Well
- TDD approach caught bugs early
- Test cases were clear
- Specification was detailed

## Blockers/Questions
1. Not sure about error handling in...
2. Need clarification on...
3. Should I...?

## What's Next
1. Complete implementation of...
2. Run full test suite
3. Review code quality

## Files Created/Modified
- jarvis/cli.py (new)
- tests/test_step_1.py (new)
- jarvis/__init__.py (modified)

## Code Quality Notes
- 95% test coverage
- All edge cases handled
- Following REQUIREMENTS.md

## Lessons Learned
- TDD really does prevent bugs
- Clear test cases save time
- Don't skip edge cases

## Links to Design Repo
- [DESIGN_PLAN.md](../../DESIGN_PLAN.md) - Architecture
- [JARVIS_FILE_TREE.md](../../JARVIS_FILE_TREE.md) - File structure
- [REQUIREMENTS.md](../../REQUIREMENTS.md) - Coding standards
```

### TODO.md (OPTIONAL)

Track what you're currently working on:

```markdown
# Current Work - Step X

## In Progress
- [ ] Implement CLI.process() method
- [ ] Write tests for error handling
- [ ] Review code quality

## Upcoming
- [ ] Run full test suite
- [ ] Check code coverage
- [ ] Document decisions

## Completed
- [x] Set up test file structure
- [x] Write test cases
- [x] Understand requirements
```

### DECISIONS.md (OPTIONAL)

Document architectural decisions:

```markdown
# Design Decisions - Step X

## Decision 1: Use ABC for Abstract Classes
**Context**: Need abstract base for observers

**Options**:
1. Use abc.ABC
2. Use inheritance
3. Use protocols

**Decision**: Use abc.ABC

**Rationale**: 
- Clear interface definition
- Follows Python conventions
- Better IDE support

**Alternatives Considered**: 
- Inheritance was too loose
- Protocols require Python 3.8+

---

## Decision 2: Graph Cycle Detection Algorithm
**Context**: Need to detect cycles in dependency graph

**Options**:
1. DFS approach
2. Topological sort
3. Simple visited set

**Decision**: DFS approach

**Rationale**:
- Simple to understand
- O(n) time complexity
- Catches all cycle types
```

---

## Rules for Agent_Workspace

### ✅ ALLOWED

- 📝 Markdown files (.md) - Your notes
- 📊 Progress tracking - What you did
- 💭 Decision documents - Why you chose something
- 🎯 TODO lists - What comes next
- 🔗 Links - To design docs, specs, etc.
- 📚 Learning notes - What you learned
- ❓ Questions - Things you're unsure about

### ❌ NOT ALLOWED

- 💻 Code files (.py, .js, .ts, .java, etc.)
  - Code goes in main directory
  - Tests go in tests/ directory
  
- 📁 Subdirectories
  - Keep it flat
  - All files in root of Agent_Workspace
  
- 🗑️ Temporary files
  - No `.tmp`, `.bak`, `.old` files
  - No debug prints or scratch code
  - No `test_scratch.py` or similar
  
- ⚙️ Configuration files
  - No `.env`, `.env.local`, etc.
  - No config.json, settings.yaml
  - No database files
  
- 📦 Dependencies
  - No node_modules, __pycache__
  - No venv or virtual environments
  - Use .gitignore for these

---

## What Happens to Your Notes

### During Development (You're Working)
```
Agent_Workspace/
├── README.md        ← You write progress here
├── TODO.md          ← You track work here
└── DECISIONS.md     ← You document choices here
```

### When Step Completes
```
Step is done → Owen archives your notes:

Agent_Workspace/*    → Copied to Development_Logs/Step_X/
Agent_Workspace/     → Folder DELETED

Development_Logs/Step_X/
├── README.md        ← Your progress notes preserved
├── TODO.md
├── DECISIONS.md
└── [other files]    ← For knowledge transfer
```

### In the Design Repo
Your notes become part of project history:
- Used to understand what was done
- Reference for future developers
- Record of decisions made

---

## Best Practices

### Write Clear Progress Notes

✅ **GOOD**
```
## What I Did Today
1. Implemented CLI.process() method
   - Takes user input string
   - Returns command result or error
   - Handles empty strings gracefully
2. Created comprehensive tests
   - 15 test cases for process()
   - Tests normal flow and edge cases
   - 100% code coverage for CLI class
```

❌ **BAD**
```
## What I Did Today
- did stuff
- coded
- tested things
```

### Document Decisions with Context

✅ **GOOD**
```
## Decision: Use recursive DFS for cycle detection
**Why**: 
- Simple to understand and maintain
- O(V+E) time complexity
- Handles all cycle types

**Alternatives**: 
- Topological sort (more complex)
- BFS (same complexity, less intuitive)

**Tradeoff**: Recursive approach uses stack, could hit limits on very large graphs
```

❌ **BAD**
```
## Decision: Used DFS
Used it because it works.
```

### Track What Works and What Doesn't

✅ **GOOD**
```
## What Worked Well
- TDD approach caught 3 bugs before manual testing
- Clear test case names made debugging easy
- Specification was detailed, no ambiguity

## What Was Difficult
- Understanding cycle detection algorithm took time
- Edge case with empty lists was tricky
- Initial misunderstanding of observer pattern

## Lessons Learned
- Don't skip edge cases in tests
- Clear naming is worth the extra time
- Design upfront prevents rework
```

### Keep Notes Updated

- Update after each coding session
- At minimum, update daily
- Include what you accomplished
- Include blockers/questions

### Link to Design Docs

Use relative links to reference:
```markdown
See [JARVIS_FILE_TREE.md](../../JARVIS_FILE_TREE.md) for complete structure.

Follow [REQUIREMENTS.md](../../REQUIREMENTS.md) standards.

Review [DESIGN_PLAN.md](../../DESIGN_PLAN.md) for architecture.
```

---

## Common Patterns

### Pattern 1: Daily Progress Update

```markdown
# Step X Development Progress

## Today's Work

### Morning
- [ ] Reviewed specification and existing tests
- [ ] Started implementing Graph.add_edge()
- [x] Created test cases for add_edge

### Afternoon
- [x] Implemented Graph.add_edge() method
- [x] Fixed 2 test failures
- [x] Added cycle detection
- [ ] Run full test suite

## Current Status
- 60% complete
- 8 of 12 functions implemented
- All tests passing for completed functions

## Next
- Implement remaining 4 functions
- Full test run
- Code review
```

### Pattern 2: Questions and Blockers

```markdown
## Blockers/Questions

### Q1: Error Handling Strategy
**Question**: Should Graph.add_node() raise exception for duplicate node or silently ignore?

**Options**:
1. Raise ValueError (fail early)
2. Silently ignore (defensive)
3. Return success boolean (explicit)

**Research Needed**: Check USE_CASES.md for expected behavior

**Status**: Waiting on clarification

---

### Q2: Type Hints
**Question**: Should I use Optional[T] or T | None (Python 3.10+)?

**Context**: Code needs to support Python 3.8+

**Decision**: Use Optional[T] from typing

**Status**: Resolved - implements compatibility
```

### Pattern 3: Lessons Learned

```markdown
## Lessons Learned This Step

### 1. TDD Really Works
Started writing tests first and caught bugs immediately:
- Test caught missing validation on empty string
- Test caught off-by-one error in loop
- Would have taken hours to find manually

### 2. Clear Naming Saves Time
Functions with clear names were easier to test:
- `test_add_node_to_graph()` is clear
- `test_1()` would have been confusing

### 3. Edge Cases Matter
Found 3 edge cases through testing:
- Empty graph handling
- Self-referential edges
- Duplicate node handling

### 4. Design-First Approach
Following specification saved time:
- Knew exactly what to implement
- No guessing about requirements
- Tests matched specification perfectly
```

---

## Cleanup Before Finishing

When the step is complete and you're done:

- [x] Updated README.md with final status
- [x] Documented all decisions
- [x] Noted any issues for next step
- [x] Verified all test cases pass
- [x] Code follows REQUIREMENTS.md
- [x] No temporary files in workspace
- [x] All links work
- [x] Notes are clear and useful

Your notes will be copied to the design repo as knowledge transfer. Make sure they're useful!

---

## Summary

| Item | Rule |
|------|------|
| **Purpose** | Document your progress and learnings |
| **Location** | Agent_Workspace/ (temporary) |
| **Files** | Markdown only (.md) |
| **Structure** | Flat, no subdirectories |
| **Updates** | Regular (daily minimum) |
| **Cleanup** | Automatic (folder deleted) |
| **Preservation** | Copied to Development_Logs |

---

**Use Agent_Workspace to document, track, and share your work.**  
**Your notes help future developers understand decisions made during development.**

**Last Updated**: January 9, 2026
