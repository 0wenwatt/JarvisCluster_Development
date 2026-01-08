# Contributing to Jarvis Cluster Development

Thank you for your interest in contributing to the Jarvis Cluster Management System! This guide will help you get started with contributing to this planning and tracking repository.

## Table of Contents

- [About This Repository](#about-this-repository)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Pull Request Process](#pull-request-process)
- [Code Review Guidelines](#code-review-guidelines)
- [Community](#community)

## About This Repository

This repository is the **planning and tracking hub** for Jarvis. It contains:
- Design plans and architecture documents
- Development roadmaps and requirements
- Tracking scripts and utilities
- Example implementations and templates
- Best practices and guidelines

**Note**: This is NOT the main implementation repository. The actual Jarvis cluster management system is implemented in a separate repository.

## Getting Started

### Prerequisites

- **Git**: Version control
- **Python 3.9+**: For scripts and examples
- **Text Editor**: VS Code, PyCharm, or your preferred editor
- **GitHub Account**: For contributing

### First-Time Setup

1. **Fork the repository**

   ```bash
   # Click the "Fork" button on GitHub
   ```

2. **Clone your fork**

   ```bash
   git clone https://github.com/YOUR_USERNAME/JarvisCluster_Development.git
   cd JarvisCluster_Development
   ```

3. **Add upstream remote**

   ```bash
   git remote add upstream https://github.com/0wenwatt/JarvisCluster_Development.git
   ```

4. **Install development dependencies**

   ```bash
   # Install Python dependencies for scripts
   pip install -r requirements-dev.txt

   # Install pre-commit hooks
   pip install pre-commit
   pre-commit install
   ```

## Development Setup

### Editor Configuration

We provide `.editorconfig` for consistent formatting. Install the EditorConfig plugin for your editor.

### Pre-commit Hooks

Pre-commit hooks automatically check your changes before commit:

```bash
# Install hooks
pre-commit install

# Run manually on all files
pre-commit run --all-files
```

The hooks will:
- Check YAML, JSON, and Markdown syntax
- Format Python code with Black
- Sort imports with isort
- Lint with flake8
- Check for trailing whitespace
- Detect secrets

### Recommended Tools

- **yamllint**: YAML linting
- **markdownlint**: Markdown linting
- **black**: Python code formatting
- **isort**: Import sorting
- **flake8**: Python linting

## Making Changes

### Branching Strategy

We use feature branches for all changes:

```bash
# Create a feature branch
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b bugfix/issue-description
```

### Types of Contributions

#### 1. Documentation Updates

Update planning documents, guides, or examples:

```bash
# Edit documentation
vim DESIGN_PLAN.md

# Commit with conventional commit message
git commit -m "docs: update scheduler architecture section"
```

#### 2. Script Improvements

Improve tracking or utility scripts:

```bash
# Edit scripts
vim scripts/compare_tree.py

# Test the script
python3 scripts/compare_tree.py --help

# Commit
git commit -m "feat(scripts): add verbose output to compare_tree"
```

#### 3. Examples and Templates

Add new examples or improve existing ones:

```bash
# Add example
vim src/examples/agents/new_example.py

# Test the example
python3 src/examples/agents/new_example.py

# Commit
git commit -m "feat(examples): add event-driven agent example"
```

#### 4. Configuration

Add or update configuration templates:

```bash
# Edit config
vim config/agents/development.yaml

# Validate
yamllint config/agents/development.yaml

# Commit
git commit -m "config: add performance tuner agent configuration"
```

### Commit Message Format

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `config`: Configuration changes

**Examples:**

```bash
feat(agents): add base class for optimization agents
fix(logging): correct correlation ID filter
docs: update agent development guidelines
config: add production logging configuration
test: add unit tests for agent manager
```

## Coding Standards

### Python Code

Follow [PEP 8](https://peps.python.org/pep-0008/) and our standards in [REQUIREMENTS.md](REQUIREMENTS.md):

```python
# Good: Clear, documented, type hints
def schedule_task(task_id: str, priority: int = 0) -> bool:
    """
    Schedule a task with the given priority.

    Args:
        task_id: Unique task identifier
        priority: Task priority (higher = more important)

    Returns:
        True if task was scheduled, False otherwise
    """
    logger.info("Scheduling task", extra={"task_id": task_id, "priority": priority})
    # Implementation...
    return True

# Bad: Unclear, no docs, no types
def sched(t, p=0):
    print(f"Scheduling {t}")
    # Implementation...
    return True
```

### Python Style

- **Line length**: 100 characters
- **Imports**: Grouped and sorted with isort
- **Formatting**: Automated with Black
- **Type hints**: Required for function signatures
- **Docstrings**: Required for all public functions

### YAML Files

```yaml
# Good: Clear structure, comments
agents:
  health_monitor:
    enabled: true
    type: monitoring
    config:
      check_interval: 5  # Seconds between checks
      timeout: 30        # Heartbeat timeout

# Bad: No comments, inconsistent indentation
agents:
  health_monitor:
   enabled: true
   type: monitoring
   config:
    check_interval: 5
    timeout: 30
```

### Markdown Documentation

- **Line length**: 120 characters
- **Headers**: Use ATX style (`#` instead of underlines)
- **Lists**: Consistent formatting
- **Code blocks**: Always specify language

## Testing

### Running Examples

Test your examples before committing:

```bash
# Test logging example
python3 src/examples/logging/structured_logging_example.py

# Test agent example
python3 src/examples/agents/health_monitor_example.py
```

### Validating Configuration

Validate YAML configurations:

```bash
# Validate all YAML files
yamllint config/

# Validate specific file
yamllint config/agents/development.yaml
```

### Testing Scripts

Test utility scripts:

```bash
# Test comparison script
python3 scripts/compare_tree.py --help

# Test with actual data
python3 scripts/compare_tree.py \
  --desired JARVIS_FILE_TREE.md \
  --actual /path/to/implementation \
  --output tracking/reports
```

## Documentation

### Documentation Standards

1. **Keep it up-to-date**: Update docs when making changes
2. **Be clear and concise**: Use simple language
3. **Provide examples**: Show, don't just tell
4. **Link related docs**: Help readers find more information

### Types of Documentation

#### Planning Documents

Update when system design changes:
- `DESIGN_PLAN.md`: Architecture and design
- `REQUIREMENTS.md`: Technical requirements
- `ROADMAP.md`: Development phases

#### How-To Guides

Add guides for common tasks:
- `docs/guides/`: Step-by-step instructions
- `config/*/README.md`: Configuration guides
- `src/*/README.md`: Component guides

#### ADRs (Architecture Decision Records)

Document important decisions:

```bash
# Create new ADR
cp docs/adr/000-template.md docs/adr/003-agent-communication.md

# Edit and commit
vim docs/adr/003-agent-communication.md
git commit -m "docs(adr): add decision record for agent communication"
```

## Pull Request Process

### Before Submitting

1. **Update documentation** if needed
2. **Run pre-commit hooks**: `pre-commit run --all-files`
3. **Test your changes** thoroughly
4. **Update CHANGELOG.md** if applicable
5. **Ensure commit messages** follow conventions

### Creating a Pull Request

1. **Push your branch**

   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create PR on GitHub**
   - Use a clear, descriptive title
   - Reference any related issues
   - Provide context in the description
   - Add screenshots if applicable

3. **PR Template**

   ```markdown
   ## Description
   Brief description of changes

   ## Type of Change
   - [ ] Documentation update
   - [ ] Script improvement
   - [ ] Configuration change
   - [ ] Example/template addition
   - [ ] Bug fix

   ## Checklist
   - [ ] Documentation updated
   - [ ] Pre-commit hooks pass
   - [ ] Examples tested
   - [ ] CHANGELOG.md updated (if applicable)

   ## Related Issues
   Closes #123
   ```

### Review Process

1. **Automated checks** run on your PR
2. **Reviewers** provide feedback
3. **Address feedback** and push updates
4. **Approval** from maintainers
5. **Merge** into main branch

## Code Review Guidelines

### For Authors

- **Keep PRs focused**: One feature/fix per PR
- **Write clear descriptions**: Explain what and why
- **Respond to feedback**: Be open to suggestions
- **Update as needed**: Address review comments

### For Reviewers

Check for:
- [ ] Clear, understandable code/documentation
- [ ] Follows coding standards
- [ ] Documentation is updated
- [ ] Examples work correctly
- [ ] No sensitive data committed
- [ ] Commit messages follow conventions

Provide:
- **Constructive feedback**: Be specific and helpful
- **Positive comments**: Acknowledge good work
- **Actionable suggestions**: Explain how to improve

## Community

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: Questions and discussions
- **Pull Requests**: Code review and collaboration

### Getting Help

- **Documentation**: Start with [USAGE_GUIDE.md](USAGE_GUIDE.md)
- **Issues**: Search existing issues first
- **Discussions**: Ask questions in GitHub Discussions

### Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please:
- Be respectful and professional
- Be patient with others
- Accept constructive criticism gracefully
- Focus on what is best for the project

## Additional Resources

### Related Documentation

- [README.md](README.md) - Project overview
- [USAGE_GUIDE.md](USAGE_GUIDE.md) - Complete usage guide
- [DESIGN_PLAN.md](DESIGN_PLAN.md) - Architecture overview
- [REQUIREMENTS.md](REQUIREMENTS.md) - Coding standards
- [ROADMAP.md](ROADMAP.md) - Development phases

### External Resources

- [Conventional Commits](https://www.conventionalcommits.org/)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
- [Markdown Guide](https://www.markdownguide.org/)
- [YAML Specification](https://yaml.org/spec/)

---

Thank you for contributing to Jarvis! Your contributions help make this project better for everyone.
