# Repository Maintenance Guide

**Guidelines for keeping the JarvisCluster Design Repository clean, organized, and functional.**

---

## Maintenance Philosophy

This repository is the "control center" for the Jarvis project. It should be:

- 🧹 **Clean** — No clutter, orphaned files, or temporary content
- 📐 **Organized** — Consistent folder structure and naming
- 📝 **Documented** — Every file has clear purpose and context
- 🎯 **Purposeful** — Every file serves the project
- 🔒 **Protected** — Core files maintained carefully

---

## Regular Maintenance Schedule

### Daily (When Adding Content)
- ✅ Save files in correct locations
- ✅ Follow naming conventions
- ✅ Add headers/documentation to new files
- ✅ Delete temporary files immediately

### After Each Step Completion
1. **Archive Agent Work**
   - Move `Agent_Workspace/` to `Development_Logs/Step_X/`
   - Create `STEP_X_SUMMARY.md` summarizing what was done
   - Update `Development_Logs/INDEX.md`

2. **Verify Cleanliness**
   - Check for stray files in working folders
   - Remove any temporary notes
   - Ensure all step files are finalized

3. **Update Navigation**
   - Update main `INDEX.md` files
   - Verify links are still valid
   - Ensure folder structure is clear

### Weekly
- [ ] Scan for orphaned files
- [ ] Check for confusing folder structure
- [ ] Review recent additions
- [ ] Verify main INDEX files are current

### Monthly (Or After Major Changes)
1. **Deep Folder Audit**
   - Walk through each major folder
   - Identify unused or outdated files
   - Plan cleanup or reorganization

2. **Documentation Review**
   - Check DEVELOPMENT_RULES.md for accuracy
   - Review GUIDELINES.md for completeness
   - Update RULES.md if rules changed

3. **Structure Verification**
   - Ensure folders align with design
   - Check for any new "junk" areas
   - Plan improvements

---

## Common Maintenance Tasks

### Task: Clean Up Temporary Files

When you find temporary files (notes, drafts, etc.):

```
1. Identify: What is this file for?
2. Decide: Is it important?
   - Important? → Move to correct folder
   - Temporary? → Delete
3. Verify: Did cleanup improve things?
4. Document: Update INDEX if moved
```

### Task: Remove Orphaned Folders

When you find folders with unclear purpose:

```
1. Investigate: What was this for?
   - Read any README.md in the folder
   - Check git history if available
2. Decide: Is it needed?
   - Needed? → Move to proper location
   - Obsolete? → Archive or delete
3. Update: Remove from navigation
4. Document: Note why it was removed
```

### Task: Fix Broken Links

When you find broken links in documentation:

```
1. Identify: Which link is broken?
2. Trace: Where should it point?
3. Update: Fix the link
4. Verify: Test the link works
5. Find more: Search for similar broken links
```

### Task: Reorganize a Folder

When a folder's structure needs improving:

```
1. Plan: What's the better structure?
2. Discuss: Ask Owen if major change
3. Migrate: Move files carefully
4. Update: Update all navigation/links
5. Verify: Ensure everything still works
6. Document: Explain why change was made
```

---

## Maintenance Checklist

### Folder: `Copilot_Development_Instructions/`

- [ ] Each Step_X folder has `.github/copilot-instructions.md`
- [ ] Each Step_X folder has `Agent_Workspace/README.md`
- [ ] DESIGN_REFERENCE is current and linked
- [ ] No stray files outside step folders
- [ ] All steps properly numbered
- [ ] Links to previous steps work
- [ ] Step instructions are clear and actionable

### Folder: `JarvisCluster_Design/`

- [ ] Design documents are organized logically
- [ ] README.md exists explaining the structure
- [ ] All design decisions are documented
- [ ] Links between documents are accurate
- [ ] Obsolete design files are archived/removed
- [ ] Architecture is clearly explained
- [ ] Design rationale is documented

### Folder: `Development_Logs/`

- [ ] Each completed step has a summary
- [ ] Step folders are organized consistently
- [ ] INDEX.md is current
- [ ] Archives are clearly labeled
- [ ] Progress tracking is visible
- [ ] Completed work is preserved

### Folder: `Copilot_Local/`

- [ ] README.md is current
- [ ] GUIDELINES.md is comprehensive
- [ ] RULES.md is accurate
- [ ] No confusion between files
- [ ] Links to other docs work

### Root Directory

- [ ] No unnecessary files
- [ ] Only `.md` documentation files
- [ ] No `.py` files or code
- [ ] DEVELOPMENT_RULES.md is current
- [ ] `.gitignore` exists
- [ ] `.github/` folder exists with instructions

---

## File Review Template

When reviewing any file in the repository:

```
File: [filename]
Location: [path]
Purpose: [What is this file for?]
Status: [Current/Outdated/Needs Review]
Owner: [Who maintains this?]

Checklist:
- [ ] File has clear purpose
- [ ] File is in correct location
- [ ] File follows naming conventions
- [ ] File is well-documented (headers, comments)
- [ ] File links are accurate
- [ ] File content is current
- [ ] File is needed/used

Action: [Keep/Update/Move/Delete]
Notes: [Any additional info]
```

---

## Archive Strategy

### What to Archive
- Completed step work
- Superseded design documents
- Old versions of key files
- Historical decisions

### Where to Archive
- `Development_Logs/` for step archives
- `Development_Logs/Archive/` for old content
- Git history for version tracking

### Archive Naming
```
STEP_X_ARCHIVE/          — Completed step files
[TOPIC]_OLD.md           — Previous version
[TOPIC]_v1.md            — Versioned document
```

---

## Updating DEVELOPMENT_RULES.md

When you discover the need for a new rule:

1. **Document the Issue**
   - Why is this rule needed?
   - What problem does it solve?
   - What would happen without it?

2. **Add the Rule**
   - Write clearly and concisely
   - Give examples if helpful
   - Explain the rationale

3. **Communicate**
   - Add to DEVELOPMENT_RULES.md
   - Reference in relevant step instructions
   - Update GUIDELINES.md if agent-related

4. **Enforce**
   - Check new work against rule
   - Remind others of the rule
   - Document exceptions if needed

---

## Handling Special Cases

### Case: Someone Created Files in Wrong Location

```
1. Don't blame — it happens
2. Identify: What should go where?
3. Move: Put files in correct location
4. Update: Fix any affected links/references
5. Clarify: Remind about correct locations
6. Improve: Maybe the rule wasn't clear enough?
```

### Case: Folder Purpose Becomes Unclear

```
1. Investigate: Read the folder's README
2. Check: What files are in it?
3. Consult: Ask others what it's for
4. Decide: Is it still needed?
5. Fix: Either clarify purpose or remove it
6. Document: Update GUIDELINES.md to prevent confusion
```

### Case: Repository Gets Messy After Multiple Changes

```
1. Don't panic — clean up is part of maintenance
2. Assess: What needs fixing?
   - Stray files?
   - Unclear structure?
   - Broken links?
3. Plan: Create cleanup plan
4. Execute: Make changes systematically
5. Verify: Test that everything works
6. Document: Explain what was cleaned up
```

---

## Tools for Maintenance

### File Organization
- Git history (see what changed when)
- Folder structure review (walk through folders)
- Link checking (ensure all references work)

### Documentation
- README files (explain folder purpose)
- INDEX files (navigate structure)
- RULES files (communicate expectations)

### Communication
- Commit messages (explain why changes were made)
- File headers (document purpose)
- Decision logs (record why decisions were made)

---

## Red Flags (Watch For These)

🚩 **Stray files in root**
- Only `.md` files belong in root
- Code/config files should be in folders

🚩 **Orphaned folders**
- Folders with no clear purpose
- Folders with no README.md
- Folders no one understands

🚩 **Broken links**
- References to moved/deleted files
- Invalid file paths
- Typos in documentation

🚩 **Inconsistent naming**
- Files named randomly
- Folder names not matching pattern
- Versions not clearly marked

🚩 **Outdated documentation**
- README files not matching contents
- Old file names referenced
- Instructions for deleted processes

🚩 **Documentation drift**
- Rules applied inconsistently
- Folder structure doesn't match GUIDELINES
- Links between documents failing

---

## Documentation Consistency

### Every Folder Should Have
```
✅ README.md           — Explain purpose
✅ INDEX.md (if large) — Navigate contents
✅ Clear organization  — Logical structure
✅ Consistent naming   — Follow patterns
```

### Every File Should Have
```
✅ Clear purpose       — Why does it exist?
✅ Proper location     — Is it in right folder?
✅ Documentation       — Headers/comments
✅ Current info        — Is it up-to-date?
```

### Every Document Should Link
```
✅ To parent README    — Where does it fit?
✅ To related docs     — Context and references
✅ To next steps       — What comes after?
✅ Back to main nav    — How to get home?
```

---

## Maintenance Log

Keep a simple log of maintenance work:

```markdown
## Maintenance Log

### 2026-01-10
- Cleaned up temporary files in Step_4/
- Updated broken link in GUIDELINES.md
- Added new rule to DEVELOPMENT_RULES.md
- Reviewed folder structure, no issues found

### 2026-01-05
- Archived Step_3 work to Development_Logs/
- Created STEP_3_SUMMARY.md
- Fixed typo in Step_3 instructions
```

---

## When to Do Deep Maintenance

Do a **deep maintenance pass** when:

✅ You're starting a new phase  
✅ Major structural changes are planned  
✅ Repository feels "cluttered"  
✅ Many steps have been completed  
✅ New people are joining the project  
✅ Rules have changed significantly  

**Deep Maintenance Includes**:
- Full folder audit
- Broken link detection
- Consistency review
- Documentation update
- Structure optimization
- Archive organization

---

## Success Metrics

A well-maintained repository has:

✅ **Clarity** — Purpose of every file is obvious  
✅ **Organization** — Logical folder structure  
✅ **Accuracy** — All information is current  
✅ **Consistency** — Rules applied uniformly  
✅ **Linkage** — Documents reference each other correctly  
✅ **Accessibility** — Easy to find what you need  
✅ **Cleanliness** — No clutter or confusion  

---

## Summary

**Maintenance is ongoing**, not one-time:

- Clean daily
- Organize weekly
- Audit monthly
- Deep clean as needed
- Update documentation continuously

A well-maintained repository is easier to use, easier to understand, and easier to build upon.

---

**Maintenance Guide Created**: January 9, 2026  
**For**: Agents and developers maintaining the JarvisCluster Design Repository
