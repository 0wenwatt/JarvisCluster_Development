# Copilot_Local - Agent Guidelines for Design Repository

**This folder contains instructions and guidelines for Agents (like Copilot) working in the JarvisCluster Design Repository.**

---

## Overview

This repository is for **design, planning, and documentation** of the Jarvis project.

It is NOT the production repository. The actual code development happens in a separate production repo that receives instructions and guidance from this design repo.

---

## Repository Purpose

This design repository maintains:

1. **Development Plans** - Step-by-step development roadmap
2. **Design Documents** - Architecture and design decisions
3. **Development Rules** - Standards for code and development
4. **Step Instructions** - Detailed guidance for each step
5. **Development Logs** - Records of completed steps
6. **Agent Guidelines** - Rules for agents working here (this folder)

---

## Repository Structure

```
JarvisCluster_Development/
├── .github/
│   └── copilot-instructions.md       ← Instructions for agents in this repo
├── Copilot_Local/                    ← You are here
│   ├── README.md                     ← This file
│   ├── RULES.md                      ← Agent rules and guidelines
│   └── REPOSITORY_GUIDELINES.md      ← How to maintain this repo
├── Copilot_Development_Instructions/ ← Instructions for production repo agents
│   ├── Step_1/ through Step_9/       ← Step-by-step development
├── JarvisCluster_Design/             ← Product design & decisions
├── Development_Logs/                 ← Step completion records
└── DEVELOPMENT_RULES.md              ← Core development rules
```

---

## Key Rules for This Repository

### ✅ DO

1. **Keep Repository Clean**
   - Only folders in root (no files except essential `.md`, `.gitignore`, etc.)
   - Remove temporary files and folders
   - Periodically clean up (after major changes)

2. **Maintain Folder Structure**
   - Never create files in root (except .md documentation)
   - All code and work in designated folders
   - Use folder organization consistently

3. **Update Documentation**
   - Keep instructions current
   - Update DEVELOPMENT_RULES.md when rules change
   - Update folder structures when they change

4. **Track Development**
   - Log steps to Development_Logs/
   - Create summaries for each step
   - Maintain INDEX.md

5. **Respect Owen's Authority**
   - Ask permission before creating root-level folders
   - Follow all rules in DEVELOPMENT_RULES.md
   - Don't override design decisions without approval

### ❌ DON'T

1. **Create Files in Root**
   - ❌ Root files (except `.md`, `.gitignore`)
   - ❌ Root `.py` files
   - ❌ Root configuration files
   - ✅ Root `.md` documentation files (allowed)

2. **Create Root Folders Without Permission**
   - ❌ New folders in root without asking
   - ✅ Ask Owen: "I need a new root folder: `folder_name/`. Reason: [explain]"
   - ✅ Wait for approval
   - ✅ Create only after approval

3. **Create Files Outside Designated Folders**
   - ❌ Files in arbitrary locations
   - ✅ Keep files in designated folders
   - ✅ Follow folder structure rules

4. **Modify Production Code**
   - ❌ This is a design repo, not production
   - ✅ Create instructions for production repo agents
   - ✅ Reference production repo, don't change it

---

## Folder-Specific Rules

### Root Directory

**Allowed Files**:
- ✅ `.md` documentation files (STEPS_LIST.md, README.md, etc.)
- ✅ `.gitignore`
- ✅ `.github/` folder

**Not Allowed**:
- ❌ `.py` files
- ❌ Any non-documentation files
- ❌ New folders (without permission)

### Copilot_Development_Instructions/

**Purpose**: Instructions for production repo agents

**Rules**:
- ✅ Create new Step folders (Step_5, Step_6, etc.)
- ✅ Create `.github/copilot-instructions.md` files
- ✅ Create `Agent_Workspace/README.md` files
- ❌ Don't create code files (they go in production repo)
- ❌ Don't create test files (they go in production repo)

**Subfolders**:
- ✅ Step_1 through Step_N (free to create for new steps)
- ✅ DESIGN_REFERENCE/ (free to modify)

### JarvisCluster_Design/

**Purpose**: Product design and decisions

**Rules**:
- ✅ Create design documents
- ✅ Create architecture documents
- ✅ Create decision records
- ✅ Create folder structure for different design aspects
- ❌ Don't create code files
- ❌ Don't create test files

**Subfolders** (examples):
- ✅ Architecture/ (system architecture)
- ✅ Database_Design/ (data model)
- ✅ API_Design/ (API specification)
- ✅ Decision_Log/ (design decisions)
- etc.

### Development_Logs/

**Purpose**: Record of completed development steps

**Rules**:
- ✅ Create Step folders (Step_1, Step_2, etc.)
- ✅ Archive Agent_Workspace notes
- ✅ Create step summaries
- ✅ Update INDEX.md
- ❌ Don't modify Agent_Workspace files (archive as-is)
- ❌ Don't create anything else

### Copilot_Local/

**Purpose**: Guidelines for agents in this design repo (this folder)

**Rules**:
- ✅ Create `.md` documentation files
- ✅ Create guidelines and processes
- ✅ Create rules and standards
- ❌ Don't create code files
- ❌ Don't create subfolders (keep simple)

---

## Your Responsibilities as an Agent in This Repo

### Planning & Documentation
1. **Maintain Roadmap** - Keep STEPS_LIST.md updated
2. **Track Progress** - Update Development_Logs when steps complete
3. **Document Decisions** - Record why decisions were made
4. **Update Instructions** - Keep step instructions current

### Repository Maintenance
1. **Keep Clean** - Remove temporary files/folders
2. **Organize Content** - Follow folder structure
3. **Update Rules** - Add to DEVELOPMENT_RULES.md when needed
4. **Regular Cleanup** - Periodically review and clean

### Supporting Development
1. **Prepare Instructions** - Create detailed step guidance
2. **Design System** - Help design the product
3. **Track Metrics** - Monitor development progress
4. **Document Learnings** - Capture insights from completed steps

---

## Repository Maintenance Process

### Weekly
- Check for stray files/folders
- Update progress tracking
- Verify folder structure

### After Each Step Completion
- Create step summary (STEP_X_SUMMARY.md)
- Update INDEX.md
- Archive Agent_Workspace notes
- Review for cleanup needed

### Monthly (Or As Needed)
- Deep clean of temporary files
- Review folder structure
- Audit DEVELOPMENT_RULES.md
- Check instruction accuracy

---

## Examples of Agent Work in This Repo

### ✅ Examples of Good Work

1. **Creating Step Instructions**
   ```
   - Read previous steps
   - Create Copilot_Development_Instructions/Step_5/.github/copilot-instructions.md
   - Create Copilot_Development_Instructions/Step_5/Agent_Workspace/README.md
   - Reference DEVELOPMENT_RULES.md throughout
   ```

2. **Logging Step Progress**
   ```
   - Agent completes Step 4
   - Create Development_Logs/STEP_4_SUMMARY.md
   - Update Development_Logs/INDEX.md
   - Keep Development_Logs/Step_4/ as archive
   ```

3. **Designing Product**
   ```
   - Create JarvisCluster_Design/Architecture/
   - Create design documents
   - Record decisions
   - Update when designs change
   ```

4. **Updating Rules**
   ```
   - Discover new rule needed
   - Add to DEVELOPMENT_RULES.md
   - Reference in step instructions
   - Document why rule exists
   ```

### ❌ Examples of Bad Work

1. **Creating Root Files**
   ```
   ❌ Create config.json in root
   ❌ Create temp_notes.txt in root
   ❌ Create helper.py in root
   ```

2. **Creating Root Folders Without Permission**
   ```
   ❌ Create root/new_folder without asking
   ❌ Create root/another_folder without approval
   ```

3. **Cluttering Folders**
   ```
   ❌ Leave temporary files around
   ❌ Create orphaned folders
   ❌ Leave confusing structure
   ```

4. **Ignoring Rules**
   ```
   ❌ Create code in design repo
   ❌ Modify production repo directly
   ❌ Ignore folder structure
   ```

---

## When You Need Owen's Permission

### Request Permission For:

1. **New Root Folders**
   ```
   "I need a new root folder: `folder_name/`. 
    Reason: [explain what it's for]"
   ```

2. **New File Types in Root**
   ```
   "I need to create `file.ext` in root. 
    Reason: [explain why]"
   ```

3. **Major Structure Changes**
   ```
   "I want to reorganize JarvisCluster_Design/ to [new structure]. 
    Reason: [explain benefits]"
   ```

4. **Changing Core Rules**
   ```
   "I want to add/change rule: [describe]. 
    Reason: [explain why]"
   ```

---

## Self-Contained Agent Work

### No Permission Needed For:

✅ Creating step instructions in `Copilot_Development_Instructions/Step_X/`  
✅ Creating design docs in `JarvisCluster_Design/` subfolders  
✅ Creating/updating `.md` files in existing folders  
✅ Creating new subfolders in designated areas  
✅ Updating DEVELOPMENT_RULES.md with new rules  
✅ Logging steps in Development_Logs/  
✅ Expanding Copilot_Local with guidelines  
✅ Maintaining folder structure  

---

## File Naming Conventions

### Documentation Files
- `README.md` - Folder overview
- `SYSTEM.md` - System explanation
- `INDEX.md` - Navigation and index
- `GUIDELINES.md` - Guidelines and rules
- `RULES.md` - Specific rules
- `STEP_X_SUMMARY.md` - Step summary

### Instruction Files
- `.github/copilot-instructions.md` - GitHub custom instructions

### Design Files
- `[TOPIC].md` - Design document
- `[TOPIC]_DESIGN.md` - Detailed design
- `[TOPIC]_DECISION.md` - Design decision

---

## Questions to Ask Yourself

**Before creating a file or folder**:

1. **Is this the right place?** - Does it fit the folder structure?
2. **Does it follow rules?** - Is it allowed in this location?
3. **Will Owen approve?** - Would he want this here?
4. **Is it documented?** - Will others understand it?
5. **Does it stay clean?** - Will it create clutter?

---

## Key Documents to Review

**Before working in this repo**:

1. [DEVELOPMENT_RULES.md](../DEVELOPMENT_RULES.md) - Core rules
2. [.github/copilot-instructions.md](../.github/copilot-instructions.md) - Repo instructions
3. [Copilot_Local/RULES.md](RULES.md) - Specific agent rules (linked below)
4. [Copilot_Local/REPOSITORY_GUIDELINES.md](REPOSITORY_GUIDELINES.md) - How to maintain repo

---

## Getting Help

**If unsure about something**:

1. Check [DEVELOPMENT_RULES.md](../DEVELOPMENT_RULES.md)
2. Check [.github/copilot-instructions.md](../.github/copilot-instructions.md)
3. Review folder structure examples in this file
4. Ask Owen for clarification

---

## Summary

**As an agent in this design repository**:

✅ Keep the repo clean and organized  
✅ Follow all folder structure rules  
✅ Ask permission for root-level changes  
✅ Create detailed instructions for production agents  
✅ Log completed steps  
✅ Design the product thoughtfully  
✅ Maintain documentation  
✅ Update rules when needed  

This repository is the "control center" for the entire Jarvis project. Keep it clean, organized, and up-to-date!

---

**Guidelines Created**: January 9, 2026  
**For**: Agents working in JarvisCluster Design Repository
