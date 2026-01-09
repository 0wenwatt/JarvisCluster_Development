# Copilot Instruction Sections

**Reusable instruction sections for creating copilot instructions across the JarvisCluster development.**

---

## What This Folder Contains

Modular, reusable instruction sections that can be referenced from any `.github/copilot-instructions.md` file:

- **No duplication** - Rules live in ONE place
- **Easy updates** - Change a rule once, applies everywhere
- **Consistent** - All agents follow same rules
- **Organized** - Rules grouped by topic

---

## Files

### Core Sections

1. **[FILESYSTEM_RULES.md](FILESYSTEM_RULES.md)** - File and folder organization
   - What's allowed where
   - Folder structure rules
   - Naming conventions
   - Cleanup procedures
   - Both design and production repos

2. **[TDD_REQUIREMENTS.md](TDD_REQUIREMENTS.md)** - Test-driven development
   - Write tests first workflow
   - Test structure and naming
   - Code coverage expectations
   - Success criteria
   - Common test patterns

3. **[AGENT_WORKSPACE.md](AGENT_WORKSPACE.md)** - Workspace usage
   - What Agent_Workspace is
   - What files are allowed
   - Progress tracking
   - Best practices
   - What happens to notes

4. **[STEP_TEMPLATE.md](STEP_TEMPLATE.md)** - How to create step instructions
   - Template for new steps
   - INCLUDE pattern for reusing sections
   - Key principles
   - Maintenance guidelines
   - Example usage

### Navigation

5. **[INDEX.md](INDEX.md)** - Navigation and overview
   - All available sections
   - How to use sections
   - Benefits of modular approach
   - Maintenance guidelines

6. **[IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)** - How to implement this system
   - Problem being solved
   - Solution overview
   - Phased implementation plan
   - Checklist for updates
   - Verification steps

---

## How to Use

### For Creating New Step Instructions

1. Read [STEP_TEMPLATE.md](STEP_TEMPLATE.md)
2. Follow the pattern in the template
3. Reference shared sections instead of duplicating
4. Keep step-specific content separate

Example:
```markdown
---
applyTo: "jarvis/**,tests/**"
---

# Step X: Title - Copilot Instructions

[Step-specific content here]

See [.github/copilot-instructions/FILESYSTEM_RULES.md](../../copilot-instructions/FILESYSTEM_RULES.md)
See [.github/copilot-instructions/TDD_REQUIREMENTS.md](../../copilot-instructions/TDD_REQUIREMENTS.md)
See [.github/copilot-instructions/AGENT_WORKSPACE.md](../../copilot-instructions/AGENT_WORKSPACE.md)
```

### For Updating Rules

1. Find relevant section file
2. Update the content
3. All steps that reference it automatically get the update
4. No need to update every step file

Example: Update filesystem rules once in `FILESYSTEM_RULES.md`, all steps follow updated rules.

### For Agents

1. Read main instruction file for step
2. When you need detailed rules, follow the links
3. Find the section that covers what you need
4. Reference [INDEX.md](INDEX.md) to find sections by topic

---

## Quick Reference

### I need to know about...

| Topic | File |
|-------|------|
| Where files should go | [FILESYSTEM_RULES.md](FILESYSTEM_RULES.md) |
| How to write tests | [TDD_REQUIREMENTS.md](TDD_REQUIREMENTS.md) |
| Workspace usage | [AGENT_WORKSPACE.md](AGENT_WORKSPACE.md) |
| Creating new step | [STEP_TEMPLATE.md](STEP_TEMPLATE.md) |
| Finding sections | [INDEX.md](INDEX.md) |
| Implementing system | [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md) |

---

## The Problem This Solves

### Before (Messy)
```
Step_1/.github/copilot-instructions.md    (130 lines with all rules)
Step_2/.github/copilot-instructions.md    (130 lines, same rules) ❌ DUP
Step_3/.github/copilot-instructions.md    (130 lines, same rules) ❌ DUP
Step_4/.github/copilot-instructions.md    (130 lines, same rules) ❌ DUP
...etc × 9 steps

Issues:
- Rules duplicated 9 times
- Hard to update consistently
- Wastes space
- Increases maintenance burden
```

### After (Clean)
```
.github/copilot-instructions/
├── FILESYSTEM_RULES.md       (ONE place)
├── TDD_REQUIREMENTS.md       (ONE place)
├── AGENT_WORKSPACE.md        (ONE place)
└── STEP_TEMPLATE.md          (ONE place)

Step_1/.github/copilot-instructions.md    (50 lines, references sections)
Step_2/.github/copilot-instructions.md    (50 lines, references sections)
...etc × 9 steps

Benefits:
- Rules in ONE place
- Easy to update
- Consistent enforcement
- Professional appearance
```

---

## Implementation Status

### ✅ Created
- [FILESYSTEM_RULES.md](FILESYSTEM_RULES.md) - Comprehensive filesystem organization guide
- [TDD_REQUIREMENTS.md](TDD_REQUIREMENTS.md) - Testing requirements and workflow
- [AGENT_WORKSPACE.md](AGENT_WORKSPACE.md) - Workspace usage guidelines
- [STEP_TEMPLATE.md](STEP_TEMPLATE.md) - Template for creating steps
- [INDEX.md](INDEX.md) - Navigation and reference
- [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md) - Implementation roadmap

### ⏳ Next: Update Existing Steps
- Update Step_1 through Step_9 instructions
- Clean up Agent_Workspace folders
- Verify all links work
- Complete verification

---

## Key Principles

### ✅ DO

1. **Keep sections focused** - One topic per file
2. **Reference often** - Link from step instructions
3. **Update in one place** - Change rules once
4. **Maintain clarity** - Each section stands alone
5. **Document relationships** - Show how sections connect

### ❌ DON'T

1. **Duplicate content** - Use references instead
2. **Scatter rules** - Keep in centralized sections
3. **Create random sections** - Use existing ones
4. **Ignore updates** - Update all references
5. **Leave broken links** - Verify links work

---

## Maintenance

### Adding a New Section

When you discover a rule that should be shared:

1. Create new `.md` file in this folder
2. Document the rule clearly
3. Add reference in [INDEX.md](INDEX.md)
4. Update relevant step instructions to reference it
5. Remove duplication from step files

### Updating an Existing Section

When a rule changes:

1. Edit the section file
2. Update content
3. All steps that reference it automatically updated
4. No need to update 9 step files!

### Removing a Section

When a section is no longer needed:

1. Archive the file (don't delete)
2. Update [INDEX.md](INDEX.md)
3. Check which steps referenced it
4. Update those step files to adjust

---

## Success Metrics

The system is working when:

✅ All step instructions reference shared sections  
✅ No duplication across multiple files  
✅ Updating a rule updates all steps  
✅ Workspaces are clean (notes only)  
✅ All links work  
✅ Consistent experience across steps  
✅ Professional appearance  

---

## Related Documentation

- [JARVIS_FILE_TREE.md](../../JARVIS_FILE_TREE.md) - Desired code structure
- [REQUIREMENTS.md](../../REQUIREMENTS.md) - Coding standards
- [DESIGN_PLAN.md](../../DESIGN_PLAN.md) - System architecture
- [Copilot_Local/GUIDELINES.md](../../Copilot_Local/GUIDELINES.md) - Design repo guidelines

---

## Getting Help

**I need to...**

- Understand filesystem organization → [FILESYSTEM_RULES.md](FILESYSTEM_RULES.md)
- Learn TDD workflow → [TDD_REQUIREMENTS.md](TDD_REQUIREMENTS.md)
- Use Agent_Workspace → [AGENT_WORKSPACE.md](AGENT_WORKSPACE.md)
- Create a new step → [STEP_TEMPLATE.md](STEP_TEMPLATE.md)
- Find a section → [INDEX.md](INDEX.md)
- Implement this system → [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)

---

## Summary

This folder contains **reusable instruction sections** that:
- Eliminate duplication across step files
- Provide single source of truth for rules
- Make updates easy and consistent
- Professional and well-organized
- Scalable for future steps

**Use the INCLUDE pattern to reference these sections from your instruction files.**

---

**Last Updated**: January 9, 2026  
**Status**: Ready for implementation  
**Next Step**: Update existing step instructions to use these sections
