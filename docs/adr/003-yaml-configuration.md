# 3. YAML for Configuration Files

Date: 2026-01-08

## Status

Accepted

## Context

The Jarvis cluster management system requires extensive configuration:
- Agent settings (intervals, thresholds, limits)
- Logging configuration (levels, handlers, formatters)
- Environment-specific settings (dev, staging, production)
- Resource limits and quotas
- Network endpoints and addresses
- Feature flags

We need a configuration format that:
- Is human-readable and editable
- Supports hierarchical data structures
- Allows comments for documentation
- Has good tooling support
- Can be validated
- Is widely adopted in the industry

## Decision

We will use **YAML (YAML Ain't Markup Language)** as the primary configuration format for Jarvis.

Key decisions:
1. **File naming**: Use `.yaml` extension (not `.yml`)
2. **Indentation**: 2 spaces (enforced by yamllint)
3. **Comments**: Encouraged for non-obvious settings
4. **Validation**: Schema validation before loading
5. **Environment overrides**: Separate files per environment
6. **Secrets**: Never commit secrets, use environment variables or secret management
7. **Defaults**: Provide sensible defaults in code

Configuration structure:
```
config/
├── agents/
│   ├── development.yaml
│   ├── production.yaml
│   └── testing.yaml
├── logging/
│   ├── development.yaml
│   ├── production.yaml
│   └── logging_config.yaml
└── default.yaml
```

## Consequences

### Positive

- **Human-readable**: Easy to read and edit by humans
- **Comments**: Supports inline comments for documentation
- **Hierarchical**: Natural representation of nested config
- **Widespread adoption**: Industry standard (Kubernetes, Docker Compose, etc.)
- **Tooling**: Excellent editor support and validation tools
- **Type rich**: Supports strings, numbers, booleans, lists, maps
- **Anchors & references**: DRY with YAML anchors and aliases

### Negative

- **Syntax sensitivity**: Indentation-based syntax can cause errors
- **Security risks**: Can execute code if not loaded safely (use safe_load)
- **Ambiguity**: Some values can be interpreted in multiple ways
- **Complex nesting**: Deep nesting can be hard to read
- **Tab issues**: Tabs are not allowed (spaces only)

### Neutral

- **Learning curve**: YAML syntax is relatively simple but has quirks
- **Validation**: Requires explicit validation schemas
- **Conversion**: Can convert to/from JSON when needed

## Alternatives Considered

### Alternative 1: JSON

**Description**: JavaScript Object Notation for configuration

**Pros**:
- Simple syntax
- Ubiquitous support
- Strict parsing (less ambiguity)
- Native to JavaScript
- Easy to validate

**Cons**:
- No comments (major limitation)
- Not as human-readable
- Verbose (requires quotes)
- No trailing commas allowed
- No multi-line strings

**Why not chosen**: Lack of comments is a deal-breaker for configuration files

### Alternative 2: TOML

**Description**: Tom's Obvious, Minimal Language

**Pros**:
- Simple and unambiguous syntax
- Very human-readable
- Comments supported
- Good for flat configs
- Type-safe

**Cons**:
- Less widely adopted
- Poor support for deep nesting
- Not as flexible
- Fewer tools and libraries
- Not as familiar to team

**Why not chosen**: Less common than YAML, poor nesting support

### Alternative 3: Python Files

**Description**: Configuration as Python code

**Pros**:
- Maximum flexibility
- Can use Python logic
- Type hints and IDE support
- No parsing needed
- Can import other configs

**Cons**:
- Security risk (arbitrary code execution)
- Requires Python interpreter
- Not language-agnostic
- Can't be edited by non-programmers
- Difficult to validate

**Why not chosen**: Security concerns and not suitable for non-developers

### Alternative 4: Environment Variables

**Description**: All configuration via environment variables

**Pros**:
- Simple mechanism
- Widely supported
- Good for secrets
- Cloud-native
- No files to manage

**Cons**:
- Flat namespace (no nesting)
- Everything is a string
- Difficult to manage many variables
- No comments
- Hard to version control

**Why not chosen**: Too limiting for complex configuration; we use env vars for secrets only

## Implementation

Implementation steps:

1. **Week 1: Standards & Tools**
   - Create .yamllint.yaml configuration
   - Add yamllint to pre-commit hooks
   - Document YAML coding standards
   - Create validation schemas

2. **Week 2: Configuration Files**
   - Create agent configuration files
   - Create logging configuration files
   - Create environment-specific configs
   - Add examples and templates

3. **Week 3: Loading & Validation**
   - Implement config loading utilities
   - Add schema validation
   - Handle environment variable interpolation
   - Add error handling

4. **Week 4: Documentation & Migration**
   - Document configuration options
   - Create configuration guide
   - Add examples
   - Team training

**Dependencies**:
- PyYAML library for parsing
- yamllint for validation
- jsonschema for schema validation (optional)

## Validation

Success criteria:

- **Readability**: Team members can understand configs without explanation
- **Correctness**: yamllint catches all syntax errors
- **Maintainability**: Configs are easy to update and version
- **Security**: No secrets committed to repository
- **Documentation**: All config options documented

Metrics to track:
- Configuration-related bugs
- Time to add new config options
- Team satisfaction with configuration
- Number of validation errors caught

Review:
- After 1 month of usage
- If major issues arise
- When considering new config needs

## References

- [YAML Specification](https://yaml.org/spec/1.2/spec.html)
- [yamllint Documentation](https://yamllint.readthedocs.io/)
- [YAML Best Practices](https://www.yaml.info/learn/bestpractices.html)
- [config/agents/README.md](../../config/agents/README.md) - Agent configuration guide
- [config/logging/README.md](../../config/logging/README.md) - Logging configuration guide
- [The Twelve-Factor App: Config](https://12factor.net/config)
