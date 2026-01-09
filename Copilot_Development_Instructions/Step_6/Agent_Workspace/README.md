# Agent_Workspace Rules

**This folder is your private workspace during Step 6.**

---

## What You CAN Do Here

✅ Create `.md` files (markdown only)
- `Progress.md` — Document what you built
- `Decisions.md` — Record design choices
- `Integration_Notes.md` — How functions integrate with folders
- `Challenges.md` — Problems you faced and solutions
- `Questions.md` — Questions for Owen

✅ Write notes about:
- Function observation implementation
- Dependency detection approach
- How FunctionToGraphConverter relates to FolderToGraphConverter
- Integration issues and solutions

---

## What You CANNOT Do Here

❌ Create `.py` files
❌ Create non-markdown files
❌ Run code or tests
❌ Build or compile

Agent_Workspace is for notes only.

---

## Key Focus for Step 6

**Most important to document**:
1. How FunctionToGraphConverter works
2. How it integrates with FolderToGraphConverter (from Step 5)
3. Function node naming and structure
4. Dependency detection approach
5. Any challenges with complex function signatures

---

## Document These Files

### Progress.md
What you built and what works

### Decisions.md
- Function node naming: `function:<file>:<name>`
- Dependency detection: How you find function calls
- Handling of nested functions, lambdas, etc.
- Metadata structure for functions

### Integration_Notes.md
- How Step 6 works with Step 5 (same Graph, same pattern)
- FolderToGraphConverter creates folder/file nodes
- FunctionToGraphConverter creates function nodes
- Both add to same Graph
- Result: Folder structure + functions in one place

### Challenges.md
- Complex function signatures
- Nested/lambda functions
- Recursive function detection
- Missing imports (can't resolve external calls)
- AST parsing edge cases

---

## Remember

- Step 5 created folders/files in Graph
- Step 6 adds functions to same Graph
- Step 7 adds metadata
- Step 8 integrates everything
- Your notes help explain how Step 6 fits into the larger picture

Document how your work builds on Step 5 and prepares for Step 7.

---

## Lifecycle

```
Step 5 approved
    ↓
Step 6 starts (you are here)
    ↓
You develop FunctionToGraphConverter
    ↓
You document in Agent_Workspace/
    ↓
All 25+ tests pass
    ↓
Owen reviews code and notes
    ↓
Notes copied to design repo
    ↓
Agent_Workspace deleted
    ↓
Step 7 begins
```

---

**Focus on integration: How Step 6 combines with Step 5 to create a complete codebase map.**
