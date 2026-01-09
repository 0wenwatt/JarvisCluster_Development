# Agent Workspace Standards

**Shared across all roles. Updated in one place. All jobs reference automatically.**

---

## What Is Agent Workspace?

Your temporary working area while performing a job.

Created at: `[job-folder]/Agent_Workspace/`

Deleted when: Job completes

---

## Allowed Files

### ✅ DO Create

- `README.md` - Progress notes and status
- `TODO.md` - Task checklist
- `DECISIONS.md` - Key decisions made
- `FINDINGS.md` - Results and discoveries
- Any other `.md` files for notes

### ❌ DON'T Create

- Code files (`.py`, `.js`, etc.)
- Temporary files (`.tmp`, `.bak`, `.old`)
- Config files (`.json`, `.yaml`, `.env`)
- Database files (`.db`, `.sqlite`)
- Cache files (`.cache`, `__pycache__`)
- IDE files (`.vscode`, `.idea`)
- Any non-markdown files

---

## Workspace Structure

```
Agent_Workspace/
├── README.md           (required: progress tracking)
├── TODO.md            (optional: task checklist)
├── DECISIONS.md       (optional: key decisions)
├── FINDINGS.md        (optional: what you found)
└── notes.md           (optional: other notes)
```

---

## README.md Format

Your progress notes. Keep it updated as you work.

```markdown
# [Job Name] - Progress

**Status**: In Progress  
**Started**: [date]  
**Due**: [date]  

## Progress
- [ ] Task 1
- [x] Task 2
- [ ] Task 3

## Current Work
What you're doing right now.

## Blockers
Any issues preventing progress.

## Next Steps
What you'll do next.

## Notes
General notes and observations.
```

---

## After Job Completes

When you finish:

1. **Finalize workspace** - Complete all notes
2. **Archive workspace** - Copy to Development_Logs
3. **Delete workspace** - Remove from job folder

### Archive Location

Your notes go to:

```
Development_Logs/[job-name]/
├── README.md
├── TODO.md
├── DECISIONS.md
├── FINDINGS.md
└── (all your notes)
```

Then your Agent_Workspace folder is deleted.

---

## Key Rules

- **Markdown only** - No code, no temp files
- **Keep updated** - Progress notes reflect current state
- **Clean exit** - No clutter when done
- **Preserve learning** - Notes are archived for future reference
- **Clear communication** - Notes are readable and organized

---

## Workspace Checklist

Use this when starting and finishing:

### Starting a Job
- [ ] Agent_Workspace folder created
- [ ] README.md created with basic structure
- [ ] Status set to "In Progress"
- [ ] TODO list created if needed

### Finishing a Job
- [ ] All notes complete
- [ ] README updated with final status
- [ ] Findings documented
- [ ] Ready to archive

### Archiving (You'll be told to do this)
- [ ] Copy all files to Development_Logs/[job-name]/
- [ ] Verify files in Development_Logs
- [ ] Delete Agent_Workspace folder
- [ ] Verify deletion

---

**Shared Standard**: All agents, all jobs  
**Updated**: In one place, all jobs use automatically  
**Used by**: Designer, Coder, Maintainer, and all jobs
