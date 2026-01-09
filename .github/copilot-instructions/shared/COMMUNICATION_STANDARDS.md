# Communication Standards

**Shared across all roles. Updated in one place. All jobs reference automatically.**

---

## Who Gets What Information

### For You (Owen)

You get:
- **What was done** (summary)
- **Key findings** (issues, discoveries)
- **Recommendations** (what to do next)
- **Decision** (approve / reject / changes needed)

Format: Clear, concise report with findings logged

---

## How to Report Findings

### Executive Summary

Start with brief overview:

```
**Job**: [Job Name]
**Status**: Complete
**Result**: [Summary in 1-2 sentences]
**Decision**: Approve / Request Changes / Reject
```

---

### Findings Section

Then detail findings:

```
## Issues Found

### Critical (3)
1. Issue A (location, why, fix)
2. Issue B (location, why, fix)
3. Issue C (location, why, fix)

### High (5)
1. Issue D
2. Issue E
...

### Medium (2)
...
```

---

### Recommendation Section

End with what you recommend:

```
## Recommendation

**Option 1**: Approve as-is
- Reasoning: Why it's ready

**Option 2**: Request changes
- Issues to fix: [List above]
- Timeline: [When could be done]

**My Recommendation**: Option X
```

---

## Report Location

Where reports go:

```
Development_Logs/[job-name]/
├── REPORT.md           (what you submit)
├── FINDINGS.md         (detailed findings from workspace)
└── [other notes]
```

---

## Report Template

Use this when completing a job:

```markdown
# [Job Name] - Report

**Date**: [YYYY-MM-DD]  
**Agent Role**: [Designer / Coder / Maintainer]  
**Status**: Complete  

---

## Executive Summary

[1-2 sentence summary of what was done and result]

**Result**: ✅ / ⚠️ / ❌  
**Decision**: Approve / Request Changes / Reject

---

## What Was Done

[Describe the work performed]

- [What was done 1]
- [What was done 2]
- [What was done 3]

---

## Findings

[Detailed findings from FINDINGS.md]

### Issues Found: [Number by severity]
- 🔴 Critical: [N]
- 🟠 High: [N]
- 🟡 Medium: [N]
- 🟢 Low: [N]

### Category 1: [e.g., Code Style]
- Issue 1 (location, severity, details)
- Issue 2 (location, severity, details)

### Category 2: [e.g., Testing]
- Issue 3 (location, severity, details)

### Category 3: [e.g., Documentation]
- Issue 4 (location, severity, details)

---

## Positive Findings

[What was done well]

- [Thing 1]
- [Thing 2]
- [Thing 3]

---

## Recommendation

[Your recommendation based on findings]

**Decision**: 
- ✅ **Approve** - Ready to proceed
- ⚠️ **Request Changes** - Issues to fix first
- ❌ **Reject** - Blocking issues, needs rework

**If changes requested**:
- Issues to fix: [List critical/high items]
- Estimated effort: [Time to fix]
- Timeline: [When ready]

---

## Next Steps

[What happens next]

1. [If approved]: ...
2. [If changes requested]: ...
3. [If rejected]: ...

---

## Detailed Findings

See `FINDINGS.md` for complete details.

```

---

## Communication Rules

### ✅ DO

- Be specific and clear
- Use examples and locations
- Provide actionable feedback
- Explain why something matters
- Suggest how to fix issues
- Be professional and respectful
- Document everything

### ❌ DON'T

- Be vague ("something's wrong")
- Give subjective feedback
- Make it personal
- Assume understanding
- Skip documentation
- Make demands without explanation

---

## Key Principles

1. **Be Clear** - Anyone can understand findings
2. **Be Complete** - All relevant information included
3. **Be Actionable** - Next steps are obvious
4. **Be Respectful** - Professional tone always
5. **Be Documented** - Everything recorded for future reference

---

**Shared Standard**: All agents, all jobs  
**Updated**: In one place, all jobs use automatically  
**Used by**: Designer, Coder, Maintainer, and all jobs
