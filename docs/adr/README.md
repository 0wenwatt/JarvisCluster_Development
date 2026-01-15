# Architecture Decision Records (ADR)

This directory contains Architecture Decision Records (ADRs) that document important architectural decisions made during the development of the Jarvis cluster management system.

## What is an ADR?

An Architecture Decision Record (ADR) is a document that captures an important architectural decision made along with its context and consequences.

## Why ADRs?

ADRs help:
- **Document context**: Why decisions were made
- **Track evolution**: How architecture has changed over time
- **Onboard new members**: Understand past decisions
- **Avoid revisiting**: Don't rehash old discussions
- **Facilitate review**: Make decisions visible

## ADR Format

Each ADR follows this format:

```markdown
# [Number]. [Title]

Date: YYYY-MM-DD

## Status

[Proposed | Accepted | Deprecated | Superseded by ADR-XXX]

## Context

What is the issue we're seeing that is motivating this decision or change?

## Decision

What is the change that we're proposing and/or doing?

## Consequences

What becomes easier or more difficult to do because of this change?

### Positive

- Benefit 1
- Benefit 2

### Negative

- Drawback 1
- Drawback 2

## Alternatives Considered

What other options were considered?

### Alternative 1

Description, pros, cons

### Alternative 2

Description, pros, cons

## References

- Related documents
- External resources
```

## Creating a New ADR

1. **Copy the template**

   ```bash
   cp docs/adr/000-template.md docs/adr/NNN-short-title.md
   ```

2. **Fill in the sections**
   - Use the next available number
   - Use a short, descriptive title
   - Fill in all sections

3. **Submit for review**

   ```bash
   git add docs/adr/NNN-short-title.md
   git commit -m "docs(adr): add decision record for [topic]"
   ```

## Existing ADRs

| Number | Title | Status | Date |
|--------|-------|--------|------|
| [000](000-template.md) | ADR Template | N/A | N/A |
| [001](001-agent-based-architecture.md) | Agent-Based Architecture | Accepted | 2026-01-08 |
| [002](002-structured-logging.md) | Structured Logging with Correlation IDs | Accepted | 2026-01-08 |
| [003](003-yaml-configuration.md) | YAML for Configuration Files | Accepted | 2026-01-08 |

## When to Create an ADR

Create an ADR when making decisions about:
- **Architecture**: System structure, component interactions
- **Technology**: Language, framework, database choices
- **Patterns**: Design patterns, architectural patterns
- **Processes**: Development workflows, deployment strategies
- **Standards**: Coding standards, conventions

## When NOT to Create an ADR

Don't create ADRs for:
- **Implementation details**: Small code-level decisions
- **Temporary fixes**: Short-term workarounds
- **Obvious choices**: Decisions with no real alternatives
- **Personal preferences**: Tabs vs. spaces (unless it affects the team)

## ADR Lifecycle

1. **Proposed**: Decision is being discussed
2. **Accepted**: Decision is approved and implemented
3. **Deprecated**: Decision is no longer recommended
4. **Superseded**: Replaced by a newer ADR

## Updating ADRs

ADRs should be **immutable** once accepted. To change a decision:

1. Create a new ADR that supersedes the old one
2. Update the old ADR's status to "Superseded by ADR-XXX"
3. Link between the two ADRs

## Related Resources

- [ADR GitHub Organization](https://adr.github.io/)
- [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- [Architecture Decision Records in Action](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)
