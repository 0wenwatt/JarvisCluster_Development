---
applyTo: "STEP_BY_STEP_PLAN/**,JarvisCluster_Design/**,Copilot_Local/**,Copilot_Development_Instructions/**,Development_Logs/**"
---

# Copilot Instructions for JarvisCluster Design Repository

## Quick Start

You are working on the **JarvisCluster Design & Planning Repository** — the control center for the entire project.

**This is NOT production code.** You maintain:
- Development plans and step-by-step instructions
- Product design and architecture
- Development logs and progress tracking
- Instructions for production repo developers

---

## Read These FIRST

1. **[Copilot_Local/README.md](Copilot_Local/README.md)** ← Start here
2. **[Copilot_Local/GUIDELINES.md](Copilot_Local/GUIDELINES.md)** ← Comprehensive rules
3. **[Copilot_Local/RULES.md](Copilot_Local/RULES.md)** ← Quick reference
4. **[DEVELOPMENT_RULES.md](DEVELOPMENT_RULES.md)** ← Core project rules

---

## Your Primary Tasks

### 1. Create & Maintain Development Instructions
**Folder**: `Copilot_Development_Instructions/Step_X/`

- Create `.github/copilot-instructions.md` for each step
- Prepare detailed `Agent_Workspace/README.md` with implementation guidance
- Reference DEVELOPMENT_RULES.md throughout
- Write tests first, then implementation

### 2. Design the Jarvis Architecture
**Folder**: `JarvisCluster_Design/`

- Create architecture and design documents
- Record design decisions and rationale
- Organize design into logical subfolders
- Keep product design comprehensive and clear

### 3. Maintain the Development Plan
**Folder**: `Copilot_Development_Instructions/` or `STEP_BY_STEP_PLAN/`

- Keep step instructions clear and detailed
- Update as Owen refines the approach
- Link between steps consistently
- Ensure tests are specified before implementation

### 4. Track Progress & Archive Work
**Folder**: `Development_Logs/`

- Create `STEP_X_SUMMARY.md` after each step completes
- Archive `Agent_Workspace/` folders from agents
- Update `INDEX.md` for navigation
- Preserve what was learned

### 5. Keep Repository Clean
**All locations**

- Follow folder structure rules
- No files in root (except `.md`)
- No code in design repo
- Regular cleanup and maintenance
- See [Copilot_Local/REPOSITORY_MAINTENANCE.md](Copilot_Local/REPOSITORY_MAINTENANCE.md)

---

## Critical Rules

### ✅ DO

1. **Follow Folder Structure**
   - Keep each type of content in designated folder
   - Create subfolders as needed in allowed areas
   - Update navigation/INDEX files

2. **Document Everything**
   - Why decisions were made
   - How to implement steps
   - What was learned
   - Design rationale

3. **Keep It Clean**
   - No temporary files in root
   - No stray code anywhere
   - Regular cleanup
   - Clear organization

4. **Ask Owen**
   - New root folders
   - Major structure changes
   - Rule modifications
   - If unclear about anything

### ❌ DON'T

1. **Create Files in Root** (except `.md`)
   - ❌ `.py` files in root
   - ❌ Configuration files in root
   - ❌ Temporary files in root
   - ✅ `.md` documentation in root (allowed)

2. **Create New Root Folders** (without permission)
   - ❌ New root folders without asking
   - ✅ Ask Owen: "I need `folder_name/` because [reason]"
   - ✅ Wait for approval
   - ✅ Create only after approval

3. **Code/Test in Design Repo**
   - ❌ Implementation code
   - ❌ Test files
   - ❌ This is design, not production
   - ✅ Create instructions for production agents instead

4. **Ignore Rules**
   - ❌ Skip reading documentation
   - ❌ Make assumptions without asking
   - ❌ Violate folder structure
   - ✅ Read rules, ask when unsure

---

## Repository Structure

```
JarvisCluster_Development/          ← THIS REPO
├── .github/
│   └── copilot-instructions.md      ← This file
├── DEVELOPMENT_RULES.md             ← Core project rules
├── Copilot_Local/                   ← Instructions for THIS repo
│   ├── README.md
│   ├── GUIDELINES.md
│   ├── RULES.md
│   └── REPOSITORY_MAINTENANCE.md
├── Copilot_Development_Instructions/ ← Instructions for PRODUCTION repo
│   ├── Step_1/
│   ├── Step_2/
│   └── ... Step_N/
├── JarvisCluster_Design/            ← Product design & architecture
│   ├── Architecture/
│   ├── Database_Design/
│   └── ... design topics/
└── Development_Logs/                ← Progress tracking & archives
    ├── STEP_1_SUMMARY.md
    ├── STEP_2_SUMMARY.md
    └── Step_1/, Step_2/ (archives)
```

---

## Permission Reference

### ✅ NO PERMISSION NEEDED

- Create files in `Copilot_Development_Instructions/Step_X/`
- Create design documents in `JarvisCluster_Design/`
- Create `.md` files in existing folders
- Create subfolders in designated areas
- Archive step work to `Development_Logs/`
- Update DEVELOPMENT_RULES.md with new rules
- Maintain Copilot_Local/

### ⚠️ ASK OWEN FIRST

- Create new root folder
- Add non-markdown files to root
- Major folder reorganization
- Change core architecture of repo
- Remove existing files/folders

---

## Common Tasks

| Task | Folder | Permission? | Learn More |
|------|--------|------------|------------|
| Create step instructions | `Copilot_Development_Instructions/Step_X/` | ✅ | [GUIDELINES.md](Copilot_Local/GUIDELINES.md) |
| Design the product | `JarvisCluster_Design/` | ✅ | [GUIDELINES.md](Copilot_Local/GUIDELINES.md) |
| Log completed step | `Development_Logs/` | ✅ | [GUIDELINES.md](Copilot_Local/GUIDELINES.md) |
| Update rules | `DEVELOPMENT_RULES.md` | ✅ | [RULES.md](Copilot_Local/RULES.md) |
| Create root folder | Root | ⚠️ | Ask Owen |
| Add root files | Root | ⚠️ | Ask Owen first |

---

## Workflow Example: Completing a Step

```
1. Agent completes Step 4 work in `Copilot_Development_Instructions/Step_4/Agent_Workspace/`
2. You create `Development_Logs/STEP_4_SUMMARY.md`
   - What was built
   - Key decisions
   - What was learned
3. You archive `Agent_Workspace/` to `Development_Logs/Step_4/`
4. You update `Development_Logs/INDEX.md`
5. You verify everything is clean and links work
6. You prepare instructions for Step 5
```

---

## When Confused

**Ask yourself in order**:

1. Is this in [Copilot_Local/RULES.md](Copilot_Local/RULES.md)? → Use quick ref
2. Is this explained in [Copilot_Local/GUIDELINES.md](Copilot_Local/GUIDELINES.md)? → Read guide
3. Is this a core rule in [DEVELOPMENT_RULES.md](DEVELOPMENT_RULES.md)? → Check rules
4. Still confused? → Ask Owen

---

## Key Principles

🎯 **Centralized Design** — Everything flows through this repo  
🧹 **Keep Clean** — No clutter, organized structure  
📝 **Document Thoroughly** — Future developers need context  
🔒 **Respect Boundaries** — Design repo ≠ production repo  
✅ **Follow Rules** — They protect the project  

---

## Next Steps

1. Read [Copilot_Local/README.md](Copilot_Local/README.md)
2. Review [Copilot_Local/GUIDELINES.md](Copilot_Local/GUIDELINES.md)
3. Check [DEVELOPMENT_RULES.md](DEVELOPMENT_RULES.md)
4. Start your work in appropriate folder
5. Ask Owen if anything is unclear

---

**Repository**: JarvisCluster Design & Planning  
**Purpose**: Control center for Jarvis project development  
**Last Updated**: January 9, 2026

