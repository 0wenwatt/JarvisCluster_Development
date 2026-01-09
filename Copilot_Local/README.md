# Copilot_Local: Instructions for Design Repository Agents

**READ THIS FIRST** if you are working in the JarvisCluster Design Repository.

---

## What is This Folder?

`Copilot_Local/` contains instructions and guidelines for Agents (like Copilot) working in the **design and planning repository**.

This is NOT the production code repository. This repository maintains:
- Development plans and roadmaps
- Product design and architecture
- Step-by-step development instructions
- Development logs and progress tracking

Code implementation happens in a **separate production repository** that receives instructions from this design repo.

---

## Three Key Documents

**Start here** — Read these three documents in order:

1. **[GUIDELINES.md](GUIDELINES.md)** — Comprehensive guide for how to work in this repo
   - Repository structure and purpose
   - Detailed rules for each folder
   - Your responsibilities as an agent
   - Repository maintenance process
   - Examples of good and bad work

2. **[RULES.md](RULES.md)** — Quick reference for common questions
   - What files/folders can I create?
   - When do I need permission?
   - File naming conventions
   - Common tasks checklist
   - Permission request template

3. **[DEVELOPMENT_RULES.md](../DEVELOPMENT_RULES.md)** — Core rules for the entire project
   - Architecture principles
   - Code structure rules
   - Development standards
   - Testing requirements

---

## Your Role

As an agent in this repository, you:

✅ **Maintain** the step-by-step development plan  
✅ **Create** detailed instructions for production repo agents  
✅ **Design** the Jarvis system architecture  
✅ **Document** design decisions and principles  
✅ **Log** completed steps and progress  
✅ **Keep clean** the repository structure  

---

## Quick Rules

### ✅ You Can Freely Create
- Step instructions in `Copilot_Development_Instructions/Step_X/`
- Design documents in `JarvisCluster_Design/`
- Development logs in `Development_Logs/`
- `.md` files in existing folders
- New subfolders in designated areas

### ❌ You Cannot Create
- Files in root directory (except `.md`)
- New root folders (without permission)
- Code files in this design repo
- Test files in this design repo

### ⚠️ You Must Ask Permission For
- Creating new root-level folders
- Adding non-markdown files to root
- Major reorganizations
- Changes to core rules

---

## Before You Start

1. **Understand the Repository Structure**
   - Read [GUIDELINES.md](GUIDELINES.md)
   - Know which folder is which
   - Understand why rules exist

2. **Know Your Boundaries**
   - This is a design repo, not production
   - Code goes in production repo
   - You prepare instructions, not code
   - Keep repo clean and organized

3. **Ask When Unsure**
   - Check [RULES.md](RULES.md) first
   - Read [GUIDELINES.md](GUIDELINES.md)
   - If still unclear, ask Owen

---

## The Three Zones of This Repository

### 1. Development Instructions Zone
**Folder**: `Copilot_Development_Instructions/`  
**You**: Create detailed instructions for production agents  
**They**: Implement code based on your instructions

### 2. Design Zone
**Folder**: `JarvisCluster_Design/`  
**You**: Document product design, architecture, decisions  
**Use**: Create design documents, architecture diagrams, decision records

### 3. Progress Tracking Zone
**Folder**: `Development_Logs/`  
**You**: Log completed steps and progress  
**Record**: Step summaries, agent workspace archives, progress updates

---

## Common Tasks

| Task | Location | Learn More |
|------|----------|------------|
| Create step instructions | `Copilot_Development_Instructions/Step_X/` | [GUIDELINES.md](GUIDELINES.md) |
| Design the product | `JarvisCluster_Design/` | [GUIDELINES.md](GUIDELINES.md) |
| Log completed steps | `Development_Logs/` | [GUIDELINES.md](GUIDELINES.md) |
| Add agent guidelines | `Copilot_Local/` | Keep this folder simple |
| Check what's allowed | `Copilot_Local/RULES.md` | This file |
| Understand why | `Copilot_Local/GUIDELINES.md` | Full explanation |

---

## Repository Structure Map

```
JarvisCluster_Development/
├── .github/                          ← GitHub configuration
│   └── copilot-instructions.md       ← Main repo instructions
├── Copilot_Local/                    ← You are here
│   ├── README.md                     ← This file
│   ├── GUIDELINES.md                 ← Comprehensive guide
│   └── RULES.md                      ← Quick reference
├── Copilot_Development_Instructions/ ← For production agents
│   ├── Step_1/
│   ├── Step_2/
│   ├── ... more steps ...
│   └── DESIGN_REFERENCE/
├── JarvisCluster_Design/             ← Product design
│   ├── Architecture/
│   ├── Database_Design/
│   ├── API_Design/
│   └── ... more design ...
├── Development_Logs/                 ← Progress tracking
│   ├── STEP_1_SUMMARY.md
│   ├── STEP_2_SUMMARY.md
│   ├── ... more summaries ...
│   └── INDEX.md
└── DEVELOPMENT_RULES.md              ← Core project rules
```

---

## Permission Examples

### ✅ NO PERMISSION NEEDED
- Create `Copilot_Development_Instructions/Step_5/`
- Create design docs in `JarvisCluster_Design/`
- Update `.md` files in existing folders
- Create new subfolders in designated areas

### ⚠️ ASK OWEN FIRST
- Create new folder in root
- Add files to root (non-markdown)
- Major folder reorganization
- Change DEVELOPMENT_RULES.md fundamentally

---

## Next Steps

1. **Read** [GUIDELINES.md](GUIDELINES.md) — Understand the full picture
2. **Scan** [RULES.md](RULES.md) — Know the quick rules
3. **Review** [DEVELOPMENT_RULES.md](../DEVELOPMENT_RULES.md) — Understand core rules
4. **Start** your work in the appropriate folder

---

## Key Principles

🎯 **Single Source of Truth**  
- One plan in `Copilot_Development_Instructions/`
- One design in `JarvisCluster_Design/`
- One log in `Development_Logs/`

🧹 **Keep It Clean**  
- No stray files
- No temporary clutter
- Organized structure
- Regular cleanup

📝 **Document Everything**  
- Why decisions were made
- How to implement steps
- What was learned
- Progress updates

🔒 **Respect Boundaries**  
- This is design, not implementation
- Code lives in production repo
- Ask when unsure
- Follow all rules

---

## Questions?

**Ask yourself in order**:
1. Is this in [RULES.md](RULES.md)? → Use quick reference
2. Is this explained in [GUIDELINES.md](GUIDELINES.md)? → Read detailed guide
3. Is this a core rule in [DEVELOPMENT_RULES.md](../DEVELOPMENT_RULES.md)? → Consult core rules
4. Still unsure? → Ask Owen

---

**This folder created**: January 9, 2026  
**For**: Agents and developers working in JarvisCluster Design Repository

