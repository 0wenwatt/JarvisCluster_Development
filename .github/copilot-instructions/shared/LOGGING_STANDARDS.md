# Logging Standards

**Shared across all roles. Updated in one place. All jobs reference automatically.**

---

## What to Log

Log all **decisions, findings, and results**.

Things to log:
- ✅ Decisions you made and why
- ✅ Issues you found
- ✅ Test results
- ✅ Code quality findings
- ✅ Conformance issues
- ✅ Errors and blockers
- ✅ Recommendations

---

## Log File Format

Use `FINDINGS.md` or job-specific file.

```markdown
# [Job Name] - Findings

**Date**: [YYYY-MM-DD]  
**Job**: [job name]  
**Status**: [In Progress / Complete]

## Summary
[Brief overview of findings]

## Findings by Category

### Category 1: [e.g., "Code Style Issues"]

**Issue #1**: [Brief description]
- Location: [file path, line number]
- Severity: [Critical / High / Medium / Low]
- Details: [Why this is an issue]
- Evidence: [What you found]
- Recommendation: [How to fix]

**Issue #2**: [Next issue]
- Location: ...
- Severity: ...
- Details: ...
- Evidence: ...
- Recommendation: ...

### Category 2: [e.g., "Missing Tests"]

**Issue #3**: ...
```

---

## Logging Structure

Organize findings by category, not by file.

**Good**:
```
## Code Style Issues
- Issue 1 (style)
- Issue 2 (style)
- Issue 3 (style)

## Missing Tests
- Issue 4 (tests)
- Issue 5 (tests)

## Documentation
- Issue 6 (docs)
```

**Avoid**:
```
## File A
- Issue 1
- Issue 2

## File B
- Issue 3
```

---

## Issue Entry Format

For each issue, include:

| Field | Required | Example |
|-------|----------|---------|
| **Brief Description** | ✅ | "Function not documented" |
| **Location** | ✅ | `src/utils.py` line 42 |
| **Severity** | ✅ | Critical / High / Medium / Low |
| **Details** | ✅ | "Why this matters" |
| **Evidence** | ✅ | "What you found" |
| **Recommendation** | ✅ | "How to fix it" |

---

## Severity Levels

### 🔴 Critical
- Breaks functionality
- Fails tests
- Security issue
- Blocks release
- **Action**: Must fix immediately

### 🟠 High
- Significantly impacts quality
- Creates maintenance burden
- Missing required feature
- Poor performance
- **Action**: Should fix before approval

### 🟡 Medium
- Improves code quality
- Minor missing docs
- Minor style inconsistency
- **Action**: Should fix in future

### 🟢 Low
- Nice-to-have improvement
- Minor style preference
- Future enhancement
- **Action**: Can address later

---

## Special Situations

### No Issues Found

If everything is good:

```markdown
# [Job Name] - Findings

**Status**: Complete  
**Result**: ✅ No issues found

## Summary
All checks passed. Code meets requirements.

## Verification Performed
- [x] Code style check
- [x] Test coverage check
- [x] Documentation check
- [x] File organization check
- [x] Spec compliance check
```

### Mixed Results

If some things are good, some aren't:

```markdown
# [Job Name] - Findings

**Status**: Issues Found  
**Result**: ⚠️ 3 critical, 5 medium issues

## Summary
Code structure is good, but testing is incomplete.

## Passing Checks
- [x] File organization
- [x] Code style

## Issues Found (See below)
- [ ] Test coverage (3 critical)
- [ ] Documentation (5 medium)

## Issues

### Testing (3 Critical)
[Details...]

### Documentation (5 Medium)
[Details...]
```

---

## After Logging

### For Designers & Coders
Your findings stay in your workspace as reference.

### For Maintainers
Your findings are reported to the user:

```markdown
# Report: [Job Name]

**Date**: [date]  
**Reviewer**: Maintainer  
**Decision**: [Approve / Request Changes]

## Summary
[Brief summary of findings]

## Issues Found
[List of issues by severity]

## Approval Status
- ✅ Approve - Ready to merge
- ⚠️ Request Changes - Issues to fix
- ❌ Reject - Blocking issues

## Next Steps
[What happens next]
```

---

## Logging Checklist

Before marking job complete:

- [ ] All findings logged
- [ ] Issues categorized
- [ ] Severity assigned
- [ ] Evidence documented
- [ ] Recommendations provided
- [ ] Summary written
- [ ] Decision/approval stated
- [ ] User will understand findings

---

**Shared Standard**: All agents, all jobs  
**Updated**: In one place, all jobs use automatically  
**Used by**: Designer, Coder, Maintainer, and all jobs
