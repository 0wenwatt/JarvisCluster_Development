# Codebase Analysis Job - Task Definition

**Detailed task description.**

---

## The Task

Perform a complete analysis of the Jarvis production codebase and compare it to the desired state as specified in [SPECIFICATION.md](SPECIFICATION.md).

Your job is to:
1. **Analyze** the existing codebase
2. **Compare** against desired state
3. **Identify** all discrepancies
4. **Document** findings with evidence
5. **Report** results to Owen

---

## What "Discrepancies" Means

Things that don't match desired state:

- **File/folder organization** - Files not in right places
- **Code quality** - Style, documentation, clarity
- **Test coverage** - Missing tests, low coverage
- **Documentation** - Missing or incomplete
- **Dependencies** - Conflicting or outdated packages
- **Configuration** - Missing or incorrect settings
- **Architecture** - Code doesn't match design
- **Standards** - Doesn't follow project standards
- **Features** - Implemented incorrectly or incompletely

---

## Scope

### ✅ ANALYZE

- `src/jarvis/` - All code
- `tests/` - All test files
- `docs/` - All documentation
- Root config files (`.py`, `.yaml`, `.json`, etc.)
- `requirements.txt` or `pyproject.toml` - Dependencies
- `README.md` - Project documentation
- Any files specified in [SPECIFICATION.md](SPECIFICATION.md)

### ❌ DON'T ANALYZE

- `venv/` or `.venv/` - Virtual environments
- `__pycache__/` - Cache files
- `.git/` - Git internals
- Build artifacts
- IDE folders (`.vscode/`, `.idea/`)
- Anything outside project root

---

## Deliverables

When you finish, deliver:

### 1. Agent_Workspace Files
```
Agent_Workspace/
├── README.md           (progress notes - showing what you did)
├── FINDINGS.md         (all issues found - organized by category)
└── notes.md            (any other notes)
```

### 2. Development_Logs Archive
```
Development_Logs/maintainer-codebase-analysis/
├── README.md           (archived progress)
├── FINDINGS.md         (your findings - preserved)
├── REPORT.md           (what you submit to Owen)
└── notes.md            (archived notes)
```

### 3. REPORT.md Content

The report Owen receives:

```
# Codebase Analysis Report

**Date**: [today]
**Status**: Complete

## Summary
[Brief overview of findings]

## Issues by Severity
- Critical: [N]
- High: [N]
- Medium: [N]
- Low: [N]

## Issues by Category
[Organized findings]

## Passing Areas
[What's good]

## Recommendations
[What to do next]
```

---

## Working Process

### Phase 1: Setup
- [ ] Create Agent_Workspace/
- [ ] Create README.md with task checklist
- [ ] Read specification

### Phase 2: Analysis
- [ ] Check file organization
- [ ] Review code quality
- [ ] Verify tests
- [ ] Check documentation
- [ ] Analyze architecture
- [ ] Review dependencies

### Phase 3: Documentation
- [ ] Log all findings
- [ ] Categorize issues
- [ ] Assign severity
- [ ] Provide evidence

### Phase 4: Reporting
- [ ] Create REPORT.md
- [ ] Summarize findings
- [ ] Give recommendations

### Phase 5: Closure
- [ ] Archive Agent_Workspace
- [ ] Update Development_Logs
- [ ] Clean up
- [ ] Notify Owen

---

## Time Estimate

Rough time breakdown:

- **Setup**: 15 minutes
- **File organization**: 30 minutes
- **Code quality**: 1-2 hours
- **Tests**: 30 minutes
- **Documentation**: 30 minutes
- **Logging findings**: 1 hour
- **Creating report**: 30 minutes
- **Archiving**: 15 minutes

**Total**: 4-5 hours

---

## Key Rules

- **Be thorough** - Don't skip areas
- **Be objective** - Facts, not opinions
- **Be specific** - Location, evidence, why
- **Be professional** - Respectful tone
- **Be documented** - Everything recorded
- **Be organized** - Clear categories and structure

---

## Tools You Might Use

- `pytest` - Run tests, check coverage
- `pylint` or `flake8` - Code style checking
- File explorer - Check organization
- Text search - Find patterns
- Python interpreter - Understand code

---

## See Also

- [SPECIFICATION.md](SPECIFICATION.md) - What to check for
- [PROCEDURE.md](PROCEDURE.md) - How to do the analysis
- [../../shared/LOGGING_STANDARDS.md](../../shared/LOGGING_STANDARDS.md) - How to log findings
- [../../shared/COMMUNICATION_STANDARDS.md](../../shared/COMMUNICATION_STANDARDS.md) - How to report

---

**Task**: Complete codebase analysis and reporting  
**Owner**: You (Maintainer)  
**Goal**: Give Owen clear picture of codebase status
