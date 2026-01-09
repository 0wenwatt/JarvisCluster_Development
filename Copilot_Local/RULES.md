# Copilot_Local - Quick Reference Rules

**Fast lookup for rules when working in the JarvisCluster Design Repository.**

---

## Quick Rules

### Root Directory

| Item | Allowed? | Notes |
|------|----------|-------|
| `.md` files | ✅ | Documentation only |
| `.gitignore` | ✅ | Standard Git file |
| `.github/` folder | ✅ | Copilot instructions |
| `.py` files | ❌ | Use designated folders |
| New folders | ❌ | Ask Owen first |
| Configuration files | ❌ | Use designated folders |
| Temporary files | ❌ | Must clean up |

---

### File Creation

| Action | Permission? | Example |
|--------|-------------|---------|
| Create `.md` in root | ✅ | `README.md`, `RULES.md` |
| Create step instructions | ✅ | `Copilot_Development_Instructions/Step_5/` |
| Create design documents | ✅ | `JarvisCluster_Design/Architecture/` |
| Create development logs | ✅ | `Development_Logs/STEP_4_SUMMARY.md` |
| Create `.py` file in root | ❌ | Use designated folder |
| Create new root folder | ❌ | Ask Owen: "I need `folder_name/` because..." |
| Create code files anywhere | ❌ | Code goes in production repo |
| Create test files here | ❌ | Tests go in production repo |

---

### Folder Creation

| Folder Location | Free to Create? | Examples |
|-----------------|-----------------|----------|
| `Copilot_Development_Instructions/Step_X/` | ✅ | `Step_5/`, `Step_6/` |
| `JarvisCluster_Design/[Subfolder]/` | ✅ | `Architecture/`, `Database_Design/` |
| `Development_Logs/Step_X/` | ✅ | `Step_1/`, `Step_2/` |
| `Copilot_Local/[Subfolder]` | ⚠️ | Keep simple, ask if large |
| Root directory | ❌ | **ASK PERMISSION FIRST** |

---

### File Naming

```
Documentation Files:        Step-specific Files:        Design Files:
✅ README.md               ✅ STEP_4_SUMMARY.md         ✅ Architecture.md
✅ GUIDELINES.md           ✅ STEP_4_NOTES.md           ✅ Database_Design.md
✅ RULES.md                ✅ Agent_Workspace/          ✅ API_Specification.md
✅ INDEX.md                ✅ .github/                  ✅ [TOPIC]_DESIGN.md
```

---

### Cleanup Rules

| Item | Action | When? |
|------|--------|-------|
| Temporary files | Delete | Immediately after use |
| Stray `.py` files in root | Delete | Found |
| Unfinished notes | Archive or delete | After step completion |
| Old versions | Archive or delete | Replaced by new version |
| Orphaned folders | Delete | After verification |

---

### Decision Making

**Ask Owen if**:
- Creating new root folder
- Adding file type to root
- Major folder reorganization
- Changing core DEVELOPMENT_RULES.md
- Unclear about a rule

**Don't ask if**:
- Creating step instructions
- Creating design documents
- Creating `.md` files
- Organizing within designated folders
- Updating documentation
- Adding to DEVELOPMENT_RULES.md

---

### Common Tasks

#### ✅ Create Step Instructions
```
Location: Copilot_Development_Instructions/Step_X/
Files:
  - .github/copilot-instructions.md
  - Agent_Workspace/README.md
  - Agent_Workspace/TODO.md (optional)
```

#### ✅ Log Step Completion
```
Location: Development_Logs/
Files:
  - STEP_X_SUMMARY.md (create)
  - Step_X/ (archive from agent)
  - INDEX.md (update)
```

#### ✅ Design Product
```
Location: JarvisCluster_Design/
Files:
  - Create subfolder if needed
  - Create `.md` design documents
  - Record decisions
```

#### ✅ Update Rules
```
Files:
  - DEVELOPMENT_RULES.md (add rule)
  - Reference in relevant docs
  - Document why rule exists
```

#### ❌ Don't: Create Code Here
```
Code files (.py, .js, .ts, etc.)
↓ These go in the PRODUCTION REPOSITORY
↓ Create instructions instead, production agents implement
```

---

### Permission Request Template

When you need Owen's permission:

```
I need to [ACTION].

Reason: [Explain why this is necessary]

Proposed location/details: [Provide specifics]

Impact: [How does this help the project?]
```

---

### Emergency Cleanup

If repo gets cluttered:

1. Identify all stray files
2. Move important files to correct location
3. Delete temporary files
4. Verify folder structure
5. Update INDEX.md
6. Report to Owen

---

## Related Documents

- **Full Guidelines**: [GUIDELINES.md](GUIDELINES.md)
- **Development Rules**: [DEVELOPMENT_RULES.md](../DEVELOPMENT_RULES.md)
- **Repo Instructions**: [.github/copilot-instructions.md](../.github/copilot-instructions.md)

---

## Checklist: Before You Create Something

- [ ] Is this the right folder?
- [ ] Does it follow naming conventions?
- [ ] Is it allowed in this location?
- [ ] Would Owen approve?
- [ ] Does it stay organized?
- [ ] Will I document it?
- [ ] Do I need permission?

---

**Last Updated**: January 9, 2026
