# Shared Standards

**Standards used by all roles and all jobs. Updated in one place. All jobs automatically use new versions.**

---

## The Concept

Instead of each role or job having its own rules about:
- How to organize workspace
- How to log findings
- How to communicate results

All roles and all jobs use **shared, centralized standards**.

**Benefit**: Change a standard once → all jobs automatically use the new version.

---

## Available Shared Standards

### [AGENT_WORKSPACE.md](AGENT_WORKSPACE.md)
**Workspace organization and file standards**

Used by: All agents, all jobs

Covers:
- What files are allowed
- How to organize notes
- How to update progress
- How to archive when done

Updated once → all jobs use automatically

---

### [LOGGING_STANDARDS.md](LOGGING_STANDARDS.md)
**How to log findings and results**

Used by: All agents, all jobs

Covers:
- What to log
- How to organize findings
- Severity levels
- How to document issues
- Format for findings

Updated once → all jobs use automatically

---

### [COMMUNICATION_STANDARDS.md](COMMUNICATION_STANDARDS.md)
**How to communicate results to user**

Used by: All agents, all jobs (especially Maintainer)

Covers:
- What information to report
- How to structure reports
- Report templates
- Communication rules
- Key principles

Updated once → all jobs use automatically

---

## How Jobs Use Shared Standards

When creating a job instruction:

```markdown
# Job: [Job Name]

## Your Workspace
See [shared/AGENT_WORKSPACE.md](../shared/AGENT_WORKSPACE.md)

## Your Findings
See [shared/LOGGING_STANDARDS.md](../shared/LOGGING_STANDARDS.md)

## Your Report
See [shared/COMMUNICATION_STANDARDS.md](../shared/COMMUNICATION_STANDARDS.md)

## Specific Task
[Task-specific instructions]
```

---

## Example: Updating a Standard

### Before (without shared standards)
To change workspace rules:
- Update Designer README
- Update Coder README
- Update Maintainer README
- Update all 20+ job descriptions
= **30+ files to change**

### After (with shared standards)
To change workspace rules:
- Update `shared/AGENT_WORKSPACE.md`
= **1 file to change**

All jobs automatically use new version!

---

## Adding New Standards

When you identify something all roles need:

1. Create new `.md` file in `shared/`
2. Document the standard clearly
3. Add to this README
4. Have all roles/jobs reference it
5. Update once → all use new version

---

## Current Standards

| Standard | Purpose | Scope |
|----------|---------|-------|
| [AGENT_WORKSPACE.md](AGENT_WORKSPACE.md) | Workspace organization | All agents, all jobs |
| [LOGGING_STANDARDS.md](LOGGING_STANDARDS.md) | Findings documentation | All agents, all jobs |
| [COMMUNICATION_STANDARDS.md](COMMUNICATION_STANDARDS.md) | User communication | All agents, all jobs |

---

## Future Standards

Common candidates for shared standards:

- **CODE_REVIEW_PRINCIPLES.md** - How to review code
- **TEST_STANDARDS.md** - Test naming, structure, coverage
- **DOCUMENTATION_STANDARDS.md** - How to document
- **QUALITY_GATES.md** - What "done" means
- **ERROR_HANDLING.md** - How to handle issues
- **ESCALATION.md** - When to ask for help

---

## Key Principle

**One place to change = all jobs updated automatically.**

Keep shared standards:
- ✅ Focused on one topic
- ✅ Used by multiple roles/jobs
- ✅ Not specific to one job
- ✅ Stable and reusable

---

**System**: Shared Standards for All Jobs  
**Purpose**: One change propagates to all jobs automatically  
**Maintenance**: Centralized, easy to keep consistent
