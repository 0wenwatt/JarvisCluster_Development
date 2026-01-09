# Designer Snippets Index

**Reusable instruction pieces for Designer role.**

---

## Available Snippets

### SCOPE.md
**What a Designer does and doesn't do**
- Detailed boundaries and responsibilities
- What's in your job, what's not
- When to hand off to Coders
- When to involve Maintainer

### DESIGN_PROCESS.md
**How to create a design**
- Step-by-step design process
- How to think through architecture
- Decision-making framework
- Documentation during design
- Common patterns and pitfalls

### SPECIFICATION_TEMPLATE.md
**Template for creating step specifications**
- Standard structure for specs
- All sections that must be included
- How to write clear requirements
- How to specify test cases
- Example spec

### DOCUMENTATION.md
**What you must document**
- Design decisions and why
- Architecture diagrams (text-based)
- Integration points
- Future considerations
- Known limitations
- Rationale for choices

### FILESYSTEM_RULES.md
**How the design repo is organized**
- Where design docs go
- Where step specs go
- Folder structure rules
- File naming conventions
- Cleanup after steps complete

---

## Using Designer Snippets

When creating a complete Designer job instruction:

```
Base:
+ designer/SCOPE.md (what Designer does)
+ designer/DESIGN_PROCESS.md (how to design)
+ designer/SPECIFICATION_TEMPLATE.md (format for specs)
+ designer/DOCUMENTATION.md (what to document)
+ designer/FILESYSTEM_RULES.md (where things go)

Then add:
+ Specific task (design Step_X, create architecture, etc.)
= Complete Designer job instruction
```

---

## Template: Designer Job Instruction

```markdown
# Designer Job: [Task Name]

## Your Task
[What Designer needs to create]

## Requirements
See [.github/copilot-instructions/roles/designer/SCOPE.md](...)
See [.github/copilot-instructions/roles/designer/DESIGN_PROCESS.md](...)

## Deliverables
See [.github/copilot-instructions/roles/designer/SPECIFICATION_TEMPLATE.md](...)

## Documentation
See [.github/copilot-instructions/roles/designer/DOCUMENTATION.md](...)

## File Organization
See [.github/copilot-instructions/roles/designer/FILESYSTEM_RULES.md](...)

## Success Criteria
- [ ] Specification complete and clear
- [ ] Test cases defined
- [ ] Design documented
- [ ] Ready to hand off to Coder
```

---

**System**: Role-Based Designer Snippets  
**Purpose**: Reusable instruction pieces for Designer role
