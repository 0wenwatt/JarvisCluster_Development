# Coder Snippets Index

**Reusable instruction pieces for Coder role.**

---

## Available Snippets

### SCOPE.md
**What a Coder does and doesn't do**
- Detailed boundaries and responsibilities
- What's in your job, what's not
- When to ask Designer for clarification
- When Maintainer checks your work

### ENVIRONMENT_SETUP.md
**How to set up Python environment**
- Conda/venv setup
- Installing dependencies
- Activating environment
- Verifying installation
- Troubleshooting

### TDD_WORKFLOW.md
**Test-first development process**
- Why test-first matters
- How to read test cases from spec
- How to write tests
- How to implement for tests
- How to verify tests pass

### CODE_STYLE.md
**Code style and standards**
- Naming conventions
- Code formatting
- Module organization
- Function/class structure
- Comment conventions
- Docstring standards

### FILE_ORGANIZATION.md
**How production repo is organized**
- Where code goes
- Where tests go
- Where docs go
- Folder structure
- File naming conventions
- Cleanup procedures

### TESTING_REQUIREMENTS.md
**Test standards and expectations**
- Test naming conventions
- Test structure
- Test coverage requirements
- Running tests
- Debugging failed tests
- Common testing patterns

### DOCUMENTATION_REQUIREMENTS.md
**Documentation standards**
- Docstring format
- Code comments
- README updates
- Module-level documentation
- Function/class documentation
- Test documentation

---

## Using Coder Snippets

When creating a complete Coder job instruction:

```
Base:
+ Designer's specification document
+ coder/SCOPE.md (what Coder does)
+ coder/ENVIRONMENT_SETUP.md (how to set up)
+ coder/TDD_WORKFLOW.md (process)
+ coder/CODE_STYLE.md (code standards)
+ coder/FILE_ORGANIZATION.md (where files go)
+ coder/TESTING_REQUIREMENTS.md (test standards)
+ coder/DOCUMENTATION_REQUIREMENTS.md (doc standards)

= Complete Coder job instruction
```

---

## Template: Coder Job Instruction

```markdown
# Coder Job: Implement Step X

## Your Task
[Task description]

## Specification
See: [Designer's step specification]

## Setup
See [.github/copilot-instructions/roles/coder/ENVIRONMENT_SETUP.md](...)

## Process
See [.github/copilot-instructions/roles/coder/TDD_WORKFLOW.md](...)

## Standards
See [.github/copilot-instructions/roles/coder/CODE_STYLE.md](...)
See [.github/copilot-instructions/roles/coder/FILE_ORGANIZATION.md](...)
See [.github/copilot-instructions/roles/coder/TESTING_REQUIREMENTS.md](...)

## Documentation
See [.github/copilot-instructions/roles/coder/DOCUMENTATION_REQUIREMENTS.md](...)

## Success Criteria
- [ ] All tests from spec implemented
- [ ] All tests passing
- [ ] Code coverage 80%+
- [ ] Code follows style guide
- [ ] Code is documented
- [ ] Workspace clean
- [ ] Ready for Maintainer verification
```

---

**System**: Role-Based Coder Snippets  
**Purpose**: Reusable instruction pieces for Coder role
