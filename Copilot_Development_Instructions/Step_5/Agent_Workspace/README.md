# Agent_Workspace Rules

**This folder is your private workspace during Step 5.**

---

## What You CAN Do Here

✅ Create `.md` files (markdown only)
- `Progress.md` — Document what you built
- `Decisions.md` — Record design choices
- `Integration_Notes.md` — How this integrates with other steps
- `Challenges.md` — Problems you faced and solutions
- `Questions.md` — Questions for Owen

✅ Write notes about:
- What you learned
- How things integrate
- Design decisions made
- Challenges encountered
- Time spent on each part

---

## What You CANNOT Do Here

❌ Create `.py` files (Python code)
- Code goes in `/jarvis` or `/tests` in production repo
- Not in Agent_Workspace

❌ Create non-markdown files
- Images, PDFs, etc. not allowed
- Text files should be `.md`

❌ Run code or tests
- All execution happens in main repo
- Not in Agent_Workspace

❌ Build or compile
- Agent_Workspace is for notes only
- Building happens in main repo

---

## Why This Folder Exists

This folder captures your knowledge:

1. **During Step 5**: You document as you develop
2. **After Step 5**: Owen reads your notes to understand what you did
3. **Next Steps**: Your notes inform Step 6, Step 7, etc.
4. **Design Repo**: Notes get copied to the design repo for permanent record

---

## Lifecycle

```
Step 5 starts
    ↓
You develop code in /jarvis and /tests
    ↓
You document in Agent_Workspace/
    ↓
Step 5 complete - all tests pass
    ↓
Owen reviews code and notes
    ↓
Owen approves
    ↓
Agent_Workspace notes copied to design repo
    ↓
Agent_Workspace folder deleted
    ↓
Step 6 begins
```

---

## What to Document

Create these files:

### Progress.md
```markdown
# Step 5 Progress

## Completed
- [x] FolderToGraphConverter class
- [x] 20+ tests written
- [x] CLI observe_folder command
- [x] Large folder trees tested

## What Works
- Single folder observation ✅
- Nested folder hierarchies ✅
- File node creation ✅
- Metadata file handling ✅

## Integration
- FolderToGraphConverter outputs only to Graph
- No isolated data structures
- Ready for Step 6 (functions)
```

### Decisions.md
```markdown
# Key Decisions - Step 5

## Node Naming
- Folders: `folder:/path/to/folder`
- Files: `file:/path/to/file.py`
- Why: Makes queries consistent with Step 6

## Edge Structure
- Parent folder → child folder: "contains"
- Folder → file: "contains"
- Why: Natural hierarchy, queryable

## Symlink Handling
- Decision: Skip symlinks
- Why: Avoid infinite loops
- Test: `test_folder_with_symlinks`
```

### Integration_Notes.md
```markdown
# Integration - Step 5

## How FolderToGraphConverter Works
1. Takes folder path and Graph object
2. Recursively walks folder tree
3. Creates folder nodes: `folder:/path`
4. Creates file nodes: `file:/path/file.py`
5. Adds edges: parent→child, folder→file
6. Returns modified Graph

## Dependencies
- Uses: Graph class (Step 2)
- Used by: Step 6 (functions), Step 8 (integration)

## Graph After Step 5
```
Graph {
  nodes: [
    Node(folder:/tests),
    Node(folder:/tests/fixtures),
    Node(file:/tests/test_step_5.py),
    ...
  ],
  edges: [
    Edge(folder:/tests → folder:/tests/fixtures, "contains"),
    Edge(folder:/tests → file:/tests/test_step_5.py, "contains"),
    ...
  ]
}
```
```

### Challenges.md
```markdown
# Challenges - Step 5

## Challenge 1: Symlinks Caused Infinite Loops
**Problem**: Symlinks created circular directory traversal
**Solution**: Skip symlinks, log them, continue
**Test**: `test_folder_with_symlinks`
**Lesson**: Always handle filesystem edge cases

## Challenge 2: Deep Folder Hierarchies
**Problem**: Very deep folders (50+ levels) slowed traversal
**Solution**: Added depth limit (20 levels)
**Test**: `test_large_folder_tree`
**Lesson**: Sometimes limits are good

## Challenge 3: Permission Errors
**Problem**: Some folders not readable (permission denied)
**Solution**: Catch PermissionError, log, continue
**Test**: `test_permission_errors_graceful`
**Lesson**: Graceful degradation is essential
```

### Questions.md
```markdown
# Questions for Owen - Step 5

1. Should we follow symlinks or skip them?
   - Current: Skip (no infinite loops)
   - Could follow with cycle detection

2. Depth limit for folder trees?
   - Current: No limit, but tested up to 50 levels
   - Should we limit? (performance?)

3. Node naming for `.metadata.json` files?
   - Current: Treat as regular files
   - Should they be special? (they are metadata)
```

---

## Don't Document

You don't need to document:
- Line-by-line code comments (that's in the code)
- How Python works
- Standard library details
- Individual test cases (tests are self-documenting)

---

## Format Guidelines

- Use Markdown (`.md` files)
- Keep sections short and clear
- Use bullet points and checklists
- Include code examples only if helpful
- Reference tests by name

---

## Timeline

You have the entire duration of Step 5 to document. Don't rush.

- Document as you go, not at the end
- Capture decisions when you make them
- Record challenges as they happen
- Write questions when they arise

---

## After Step 5

Your notes will be:
1. **Reviewed** by Owen
2. **Copied** to the design repo
3. **Used** to prepare Step 6
4. **Permanently** stored for future reference

Make them good! Future developers will read them.

---

## Questions About This Workspace?

If unclear:
1. Re-read relevant sections above
2. Look at Agent_Workspace READMEs in other steps (same pattern)
3. Keep notes anyway - Owen will clarify if needed

Remember: **This is YOUR workspace. Use it to document YOUR work.**
