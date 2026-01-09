# Maintainer Job: Codebase Analysis & Conformance Review

**Analyze the codebase. Compare to desired state. Report findings.**

---

## Quick Start

1. Read this README
2. Go to [TASK.md](TASK.md) - What you're doing
3. Go to [SPECIFICATION.md](SPECIFICATION.md) - Desired state
4. Go to [PROCEDURE.md](PROCEDURE.md) - How to do it
5. Create `Agent_Workspace/README.md` and start working

---

## Your Job

You are analyzing the Jarvis codebase and comparing it to the desired state of requirements.

**Your output**: A detailed report of what conforms and what doesn't, so Owen knows the current status.

---

## What You'll Deliver

```
Agent_Workspace/
├── README.md              (progress tracking)
├── FINDINGS.md            (detailed findings by category)
└── (other notes as needed)

Then:
Development_Logs/[job-name]/
├── README.md              (archived progress)
├── FINDINGS.md            (your findings - preserved)
├── REPORT.md              (report to Owen)
└── (other notes - preserved)
```

---

## Standards You'll Use

All aspects of this job follow shared standards (updated in one place):

### Workspace
See [../../shared/AGENT_WORKSPACE.md](../../shared/AGENT_WORKSPACE.md)
- Where to put notes
- What files allowed
- How to organize workspace

### Findings
See [../../shared/LOGGING_STANDARDS.md](../../shared/LOGGING_STANDARDS.md)
- How to log issues
- Severity levels
- How to format findings
- Evidence and recommendations

### Communication
See [../../shared/COMMUNICATION_STANDARDS.md](../../shared/COMMUNICATION_STANDARDS.md)
- How to report results
- Report format
- What information Owen needs
- Communication rules

---

## The Workflow

### 1. Understand the Specification
- Read [SPECIFICATION.md](SPECIFICATION.md)
- Understand desired state
- Know what to check for

### 2. Plan Your Analysis
- Read [PROCEDURE.md](PROCEDURE.md)
- Create checklist of what to review
- Organize your approach

### 3. Analyze the Codebase
- Review code organization
- Check conformance to specs
- Run tests and coverage checks
- Review documentation
- Check code quality

### 4. Log Your Findings
- Document issues found
- Categorize by type
- Assign severity
- Provide evidence
- Recommend fixes

### 5. Report Results
- Create REPORT.md
- Summarize findings
- Give final assessment
- Archive workspace
- Inform Owen

---

## Key Points

### ✅ Your Role
- Analyze codebase objectively
- Compare to specification
- Document findings clearly
- Report honestly
- Provide recommendations

### ❌ NOT Your Role
- Fix code (that's Coder's job)
- Make architectural changes
- Approve based on preference
- Skip documentation
- Make it personal

---

## Success Criteria

Job is complete when:

- [ ] Codebase fully analyzed
- [ ] All findings logged
- [ ] Findings categorized and prioritized
- [ ] Report created
- [ ] Owen has clear understanding of status
- [ ] Archive complete
- [ ] Workspace cleaned up

---

## Start Here

1. **Set up workspace**:
   ```
   Create folder: Agent_Workspace/
   Create file: Agent_Workspace/README.md
   ```

2. **In README.md write**:
   ```markdown
   # Codebase Analysis - Progress
   
   **Status**: In Progress
   **Started**: [today's date]
   
   ## Tasks
   - [ ] Review file organization
   - [ ] Check code style
   - [ ] Verify tests
   - [ ] Check documentation
   - [ ] Analyze quality
   - [ ] Document findings
   - [ ] Create report
   
   ## Current Work
   Starting with file organization review...
   ```

3. **Read the specification**:
   - Go to [SPECIFICATION.md](SPECIFICATION.md)

4. **Follow the procedure**:
   - Go to [PROCEDURE.md](PROCEDURE.md)

5. **Document as you go**:
   - Create `FINDINGS.md` as you analyze
   - Update `README.md` with progress
   - Keep notes organized

6. **When complete**:
   - Finalize findings
   - Create REPORT.md
   - Archive to Development_Logs
   - Clean up workspace

---

## Important Files

- [TASK.md](TASK.md) - What exactly you're doing
- [SPECIFICATION.md](SPECIFICATION.md) - Desired state specification
- [PROCEDURE.md](PROCEDURE.md) - Step-by-step how to analyze

---

## Questions?

Refer to shared standards:

- **How to organize workspace?** → [shared/AGENT_WORKSPACE.md](../../shared/AGENT_WORKSPACE.md)
- **How to log findings?** → [shared/LOGGING_STANDARDS.md](../../shared/LOGGING_STANDARDS.md)
- **How to report results?** → [shared/COMMUNICATION_STANDARDS.md](../../shared/COMMUNICATION_STANDARDS.md)

---

**Job**: Maintainer - Codebase Analysis  
**Role**: Analyze and report  
**Output**: Detailed findings and recommendations  
**For**: Owen to understand codebase status
