# Agent Instructions Index

**Parent**: [Main Index](../INDEX.md)  
**Level**: 2 (Category)

---

## 📋 Summary

This section provides guidelines and instructions for AI agents (like GitHub Copilot) and developers working on this project. It defines standards, best practices, and behavioral expectations to ensure consistent, high-quality work.

---

## 🎯 Core Principles for Agents

### Understanding Your Role

**You are working in a PLANNING repository, not an implementation repository.**

This means:
- ✅ You SHOULD: Update documentation, tracking, and planning files
- ✅ You SHOULD: Help analyze progress and suggest improvements
- ✅ You SHOULD: Maintain consistency across planning documents
- ❌ You SHOULD NOT: Write Jarvis implementation code here
- ❌ You SHOULD NOT: Create Python modules for the Jarvis system
- ❌ You SHOULD NOT: Implement API endpoints or scheduling algorithms

### Key Behaviors

1. **Read Before Acting**: Always check existing documentation first
2. **Maintain Structure**: Preserve the pyramid navigation hierarchy
3. **Update Completely**: When changing something, update all related docs
4. **Document Decisions**: Major changes need rationale/ADRs
5. **Follow Standards**: Adhere to the coding and documentation standards
6. **Verify Consistency**: Ensure changes don't conflict with other docs

---

## 🗂️ Third Level Navigation

### Coding Standards
**Summary**: Code quality standards for the Jarvis implementation

**Contents**:
- Python style guide (PEP 8, type hints)
- File and function naming conventions
- Import organization
- Error handling patterns
- Testing requirements

**Applies to**: Implementation repository (when building Jarvis)

📖 **Navigate to**: [coding-standards.md](coding-standards.md)

---

### Documentation Standards
**Summary**: How to write and maintain documentation

**Contents**:
- Markdown formatting guidelines
- Documentation structure requirements
- Comment and docstring standards
- README templates
- ADR format and process

**Applies to**: This repository and implementation repository

📖 **Navigate to**: [documentation-standards.md](documentation-standards.md)

---

### Git Workflow
**Summary**: Version control standards and practices

**Contents**:
- Commit message format
- Branch naming conventions
- PR requirements and templates
- Code review guidelines
- Merge strategies

📖 **Navigate to**: [git-workflow.md](git-workflow.md)

---

### Agent Behavior Rules
**Summary**: Specific instructions for AI agents working on this project

**Contents**:
- What agents should and shouldn't do
- Navigation patterns to follow
- How to handle ambiguity
- Escalation procedures
- Quality checks before committing

📖 **Navigate to**: [agent-rules.md](agent-rules.md)

---

## 📖 Quick Reference Standards

### For Python Code (Implementation Repo)
```python
# ✅ Good: Type hints, docstrings, clear names
def schedule_task(task: Task, nodes: List[Node]) -> Optional[Node]:
    """
    Schedule a task to an available node.
    
    Args:
        task: The task to schedule
        nodes: Available worker nodes
        
    Returns:
        Selected node or None if no suitable node found
    """
    pass

# ❌ Bad: No types, unclear name, no docs
def sched(t, n):
    pass
```

### For Documentation (This Repo)
```markdown
# ✅ Good: Clear hierarchy, summaries, navigation

## Section Name

**Summary**: Brief one-line description

### Content Details
- Clear bullet points
- Organized information
- Proper linking

📖 **Navigate to**: [related-doc.md](link)

# ❌ Bad: No structure, walls of text, no navigation
```

### For Commits
```bash
# ✅ Good: Clear, scoped, imperative
git commit -m "Add scheduler core components to file tree"
git commit -m "Update DEV_STATE.md with Phase 1 progress"
git commit -m "Fix typo in API documentation"

# ❌ Bad: Vague, past tense, too broad
git commit -m "Updated stuff"
git commit -m "Made changes to docs"
git commit -m "Fixed things"
```

---

## 🚦 Decision Making Guidelines

### When to Proceed
✅ Proceed when you:
- Understand the full context
- Have clear requirements
- Know where files should go
- Can maintain consistency
- Have verified no conflicts

### When to Ask
❓ Ask for clarification when:
- Requirements are ambiguous
- Multiple valid approaches exist
- Changes affect many documents
- Decision has architectural impact
- You're unsure about priority/scope

### When to Stop
🛑 Stop and escalate when:
- Major architectural decision needed
- Conflicts with existing design
- Beyond your defined scope
- Breaking changes required
- Security/compliance concerns

---

## 📋 Pre-Commit Checklist

Before committing any changes:

### For Documentation Changes
- [ ] All affected documents updated
- [ ] Cross-references still valid
- [ ] Markdown properly formatted
- [ ] Navigation links work
- [ ] Consistent terminology used
- [ ] Summaries reflect details

### For Planning Changes
- [ ] JARVIS_FILE_TREE.md updated if structure changed
- [ ] DEV_STATE.md updated if progress made
- [ ] ADR created if architectural decision made
- [ ] Related docs updated
- [ ] Tracking data reflects changes

### For All Changes
- [ ] Change aligns with project goals
- [ ] No introduction of inconsistencies
- [ ] Proper grammar and spelling
- [ ] Clear commit message prepared
- [ ] No sensitive data included

---

## 🎓 Learning Resources

### Essential Reading
1. **REQUIREMENTS.md**: Technical and coding standards
2. **CONTRIBUTING.md**: Contribution guidelines
3. **docs/adr/000-template.md**: ADR format
4. **This document**: Agent behavior guidelines

### Reference Documentation
- Python PEP 8: https://pep8.org
- Google Python Style Guide
- Markdown Guide: https://www.markdownguide.org
- Conventional Commits: https://www.conventionalcommits.org

---

## 🔧 Quality Standards

### Documentation Quality
- **Clarity**: Easy to understand for new readers
- **Completeness**: All necessary information present
- **Accuracy**: Information is correct and up-to-date
- **Consistency**: Same terminology and style throughout
- **Navigation**: Easy to find related information

### Code Quality (For Implementation)
- **Readability**: Code is self-documenting
- **Testability**: Easy to write tests for
- **Maintainability**: Easy to modify and extend
- **Performance**: Efficient algorithms and data structures
- **Security**: No vulnerabilities, input validation

---

## ⚠️ Common Mistakes to Avoid

### Documentation Mistakes
- ❌ Updating one document but not related ones
- ❌ Breaking navigation links
- ❌ Using inconsistent terminology
- ❌ Writing without clear structure
- ❌ Forgetting to update summaries

### Planning Mistakes
- ❌ Mixing planning and implementation
- ❌ Skipping priority order (P0 before P1)
- ❌ Ignoring dependencies
- ❌ Not documenting decisions
- ❌ Forgetting to update tracking

### Agent Mistakes
- ❌ Writing implementation code in this repo
- ❌ Making assumptions without verification
- ❌ Ignoring existing patterns
- ❌ Creating inconsistencies
- ❌ Not reading navigation structure

---

## 🔗 Related Resources

- **Coding Standards**: REQUIREMENTS.md
- **Contribution Guide**: CONTRIBUTING.md
- **ADR Process**: docs/adr/README.md
- **Git Workflow**: docs/guides/ (if exists)

---

## 📞 Support and Questions

### For Clarification
- Review related documentation first
- Check ADRs for architectural decisions
- Look for examples in existing code/docs
- Ask specific, well-researched questions

### Escalation Path
1. Check this documentation
2. Review main planning documents
3. Search existing ADRs
4. Consult with team
5. Create new ADR if needed

---

**Last Updated**: 2026-01-08  
**Maintained By**: Development Team  
**Purpose**: Ensure consistent, high-quality work across all contributors  
**Next**: Choose a third-level node above or return to [Main Index](../INDEX.md)
