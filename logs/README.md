# Development Logs

This directory stores development logs, session records, and progress notes for the JarvisCluster project.

## Purpose

Track development activities including:
- Development session logs
- Decision-making processes
- Problem-solving notes
- Meeting minutes
- Research findings
- Experimentation results
- Debugging sessions

## Organization

Suggested structure:

```
logs/
├── sessions/           # Daily or session-based logs
│   ├── 2026-01-08-initial-setup.md
│   └── 2026-01-15-scheduler-implementation.md
├── decisions/          # Decision logs (also see docs/decisions/)
├── experiments/        # Results from experiments and prototypes
└── meetings/           # Meeting notes and minutes
```

## Log Format

### Session Logs

Use a consistent format for session logs:

```markdown
# Session: [Title]
Date: YYYY-MM-DD
Duration: X hours
Phase: Phase N - [Phase Name]

## Goals
- [ ] Goal 1
- [ ] Goal 2

## Progress
[What was accomplished]

## Decisions Made
[Key decisions and rationale]

## Issues Encountered
[Problems and how they were resolved]

## Next Steps
[What to do next]
```

### Quick Notes

For quick capture, use simple formats:

```markdown
# YYYY-MM-DD - Quick Notes
- Implemented feature X
- Fixed bug Y
- Need to follow up on Z
```

## Best Practices

1. **Date-prefix files**: `2026-01-08-description.md`
2. **Be concise but informative**: Capture key points, not every detail
3. **Link to code**: Reference commits, PRs, and files
4. **Document decisions**: Explain why, not just what
5. **Regular updates**: Log after significant work sessions

## Version Control

Note: Individual `.log` files are excluded by `.gitignore`, but markdown files are tracked.

- **DO commit**: Markdown session logs, important notes
- **DO NOT commit**: Machine-generated `.log` files (use tracking/ directory)
- **CONSIDER**: Using this for human-written logs vs. tracking/ for automated data

## Relationship to Other Directories

| Directory | Purpose |
|-----------|---------|
| `logs/` | Human-written development logs and notes |
| `tracking/` | Automated tracking data and metrics |
| `docs/decisions/` | Formal Architectural Decision Records (ADRs) |

## Templates

See [tracking/templates/](../tracking/templates/) for report templates that may be useful for structuring logs.

## Privacy Note

Avoid committing:
- Sensitive information
- API keys or credentials
- Personal notes not relevant to the project
- Private meeting contents
