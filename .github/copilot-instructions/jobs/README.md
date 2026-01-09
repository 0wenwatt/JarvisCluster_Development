# Jobs System

**Copilot jobs - complete assignments combining roles and snippets.**

---

## What Are Jobs?

Jobs are **complete assignments** for agents to perform.

Each job:
- Has a **clear task** (what to do)
- References **shared standards** (how to work)
- Uses **role-specific snippets** (detailed guidance)
- Produces **documented output** (findings, reports)
- Archives **work and learnings** (for future reference)

---

## How Jobs Work

```
1. Create Job Folder
   ├── README.md (entry point)
   ├── TASK.md (what you're doing)
   ├── SPECIFICATION.md (desired state)
   ├── PROCEDURE.md (how to do it)
   └── (other files as needed)

2. Agent Creates Agent_Workspace/
   ├── README.md (progress notes)
   ├── FINDINGS.md (logging results)
   └── (other notes)

3. Agent Works
   (Follows procedures, logs findings, references shared standards)

4. Agent Creates Report
   (REPORT.md - for Owen)

5. Archive
   ├── Copy Agent_Workspace to Development_Logs
   ├── Delete Agent_Workspace
   └── Job complete
```

---

## Job Structure Template

Every job has this structure:

```
jobs/[job-name]/
├── README.md                     (START HERE - overview)
├── TASK.md                       (What exactly to do)
├── SPECIFICATION.md              (Desired state / requirements)
├── PROCEDURE.md                  (Step-by-step how)
├── (optional files as needed)
└── Agent_Workspace/              (Created by agent)
    ├── README.md                (progress tracking)
    ├── FINDINGS.md              (what they found)
    └── notes.md                 (other notes)
```

---

## Shared Standards in Every Job

Every job uses shared standards (updated in one place):

| Standard | Purpose | Where |
|----------|---------|-------|
| [AGENT_WORKSPACE.md](../shared/AGENT_WORKSPACE.md) | Workspace rules | All jobs |
| [LOGGING_STANDARDS.md](../shared/LOGGING_STANDARDS.md) | How to log | All jobs |
| [COMMUNICATION_STANDARDS.md](../shared/COMMUNICATION_STANDARDS.md) | How to report | All jobs |

**Key benefit**: Change standard once → all jobs use new version automatically

---

## Available Jobs

### [maintainer-codebase-analysis](maintainer-codebase-analysis/)

**Role**: Maintainer  
**Task**: Analyze codebase and compare to desired state  
**Output**: Detailed findings report  

**What it includes**:
- [README.md](maintainer-codebase-analysis/README.md) - Start here
- [TASK.md](maintainer-codebase-analysis/TASK.md) - What to do
- [SPECIFICATION.md](maintainer-codebase-analysis/SPECIFICATION.md) - Desired state
- [PROCEDURE.md](maintainer-codebase-analysis/PROCEDURE.md) - How to do it

**Time**: ~4-5 hours  
**Output**: Detailed findings of issues in codebase

---

## Creating New Jobs

To create a new job:

### 1. Create Job Folder
```bash
mkdir jobs/[job-name]
cd jobs/[job-name]
```

### 2. Create Files

**README.md** - Entry point
- Overview of job
- Links to other files
- Quick start instructions

**TASK.md** - What to do
- Detailed task description
- Scope and deliverables
- Success criteria
- Time estimate

**SPECIFICATION.md** - Desired state
- What "done" looks like
- Requirements to meet
- Standards to follow
- Comparison checklist

**PROCEDURE.md** - How to do it
- Step-by-step instructions
- Tools to use
- How to log findings
- How to report results

### 3. Reference Shared Standards

In all files, reference shared standards:
```markdown
See [../../shared/AGENT_WORKSPACE.md](../../shared/AGENT_WORKSPACE.md)
See [../../shared/LOGGING_STANDARDS.md](../../shared/LOGGING_STANDARDS.md)
See [../../shared/COMMUNICATION_STANDARDS.md](../../shared/COMMUNICATION_STANDARDS.md)
```

### 4. Example Structure

```
jobs/my-new-job/
├── README.md            (links to all files)
├── TASK.md             (what to do)
├── SPECIFICATION.md    (desired state)
└── PROCEDURE.md        (step-by-step how)
```

---

## Job Workflow

### For Agent

1. Read README.md
2. Understand TASK.md
3. Review SPECIFICATION.md
4. Create Agent_Workspace/README.md
5. Follow PROCEDURE.md step by step
6. Log findings to FINDINGS.md
7. Create REPORT.md
8. Archive Agent_Workspace
9. Notify Owen

### For Owen

1. Create job in jobs/ folder
2. Assign to Maintainer/Coder/Designer agent
3. Agent performs job
4. Agent archives work to Development_Logs/
5. Review report (REPORT.md)
6. Make decisions based on findings
7. Assign follow-up jobs if needed

---

## Key Principles

### 1. One Place to Change = All Jobs Updated

Change a shared standard once → all jobs automatically use new version.

### 2. Clear Separation

- **Shared standards** - Used by all jobs
- **Job files** - Specific to one job
- **Agent_Workspace** - Temporary working area
- **Development_Logs** - Permanent archive

### 3. Reusable Structure

Every job follows same structure:
- README → TASK → SPECIFICATION → PROCEDURE
- All reference shared standards
- All produce documented output

### 4. Progressive Disclosure

Start with README (overview) → TASK (what) → SPEC (desired) → PROCEDURE (how)

---

## Job Checklist

When creating a new job:

- [ ] Job folder created
- [ ] README.md created (entry point)
- [ ] TASK.md created (what to do)
- [ ] SPECIFICATION.md created (desired state)
- [ ] PROCEDURE.md created (how to do it)
- [ ] Shared standards referenced
- [ ] Clear, step-by-step procedures
- [ ] Success criteria defined
- [ ] Time estimate provided
- [ ] Ready for agent to start

---

## Examples

### Example: Maintainer Job

See [maintainer-codebase-analysis](maintainer-codebase-analysis/) for complete example of:
- How to structure a job
- How to reference shared standards
- How to provide step-by-step procedures
- What a complete job looks like

---

## Navigation

### By Role
- [Designer Jobs](?) (not yet created)
- [Coder Jobs](?) (not yet created)
- [Maintainer Jobs](maintainer-codebase-analysis/) (created)

### By Phase
- Analysis jobs
- Implementation jobs
- Review jobs
- Documentation jobs

---

**System**: Job-Based Assignments  
**Purpose**: Complete, repeatable work assignments  
**Key Feature**: Shared standards propagate automatically  
**Maintenance**: Add new jobs, update standards once
