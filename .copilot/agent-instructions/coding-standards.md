# Coding Standards

**Parent**: [Agent Instructions Index](index.md)  
**Level**: 3 (Topic Detail)

---

## 📋 Summary

This document defines coding standards for the Jarvis implementation. These standards ensure consistency, readability, and maintainability across the codebase.

**Important**: These standards apply to the **implementation repository** (where Jarvis code lives), not this planning repository.

---

## 🐍 Python Style Guide

### Base Standards
- **Follow PEP 8**: Python's official style guide
- **Follow PEP 257**: Docstring conventions
- **Use PEP 484**: Type hints for all functions
- **Line Length**: 100 characters (not 79, for readability)
- **Indentation**: 4 spaces (no tabs)

### Code Formatting
Use `black` for automatic formatting:
```bash
black --line-length 100 jarvis/
```

Use `isort` for import sorting:
```bash
isort jarvis/
```

---

## 📝 Naming Conventions

### Files and Modules
```python
# ✅ Good: lowercase with underscores
task_queue.py
resource_matcher.py
state_manager.py

# ❌ Bad: camelCase or mixed
taskQueue.py
ResourceMatcher.py
Task-Queue.py
```

### Classes
```python
# ✅ Good: PascalCase
class TaskQueue:
class ResourceMatcher:
class StateManager:

# ❌ Bad: other styles
class task_queue:
class taskQueue:
```

### Functions and Methods
```python
# ✅ Good: lowercase with underscores
def schedule_task():
def find_suitable_node():
def get_task_status():

# ❌ Bad: camelCase
def scheduleTask():
def findSuitableNode():
```

### Variables
```python
# ✅ Good: lowercase with underscores
task_id = "task-123"
available_nodes = []
max_retries = 3

# ❌ Bad: camelCase or single letters (except loop counters)
taskId = "task-123"
t = "task-123"
```

### Constants
```python
# ✅ Good: UPPERCASE with underscores
TASK_STATUS_PENDING = "pending"
MAX_RETRY_COUNT = 3
DEFAULT_TIMEOUT = 30

# ❌ Bad: lowercase or mixed
task_status_pending = "pending"
MaxRetryCount = 3
```

### Private Members
```python
# ✅ Good: leading underscore for private
class Scheduler:
    def __init__(self):
        self._queue = []        # Private
        self.config = {}        # Public
    
    def _internal_method(self): # Private method
        pass

# ❌ Bad: no distinction
class Scheduler:
    def __init__(self):
        self.queue = []         # Unclear if public/private
```

---

## 🎯 Type Hints

### Always Use Type Hints
```python
# ✅ Good: Full type annotations
def schedule_task(task: Task, nodes: List[Node]) -> Optional[Node]:
    """Schedule a task to an available node."""
    pass

def get_task_status(task_id: str) -> TaskStatus:
    """Get the current status of a task."""
    pass

# ❌ Bad: No type hints
def schedule_task(task, nodes):
    pass
```

### Complex Types
```python
from typing import List, Dict, Optional, Union, Tuple, Callable

# ✅ Good: Detailed types
def process_tasks(
    tasks: List[Task],
    node_map: Dict[str, Node],
    callback: Optional[Callable[[Task], None]] = None
) -> Tuple[List[Task], List[Task]]:
    """Process tasks and return (successful, failed)."""
    pass

# For Python 3.9+, use built-in types
def process_tasks(
    tasks: list[Task],
    node_map: dict[str, Node]
) -> tuple[list[Task], list[Task]]:
    pass
```

### Return Types
```python
# ✅ Good: Explicit returns
def find_node(task: Task) -> Optional[Node]:
    if suitable_node:
        return suitable_node
    return None

# ✅ Good: Multiple return types
def parse_config(path: str) -> Union[Config, ConfigError]:
    pass

# ❌ Bad: Implicit None
def find_node(task: Task) -> Node:  # Can return None but type says Node
    if suitable_node:
        return suitable_node
    return None  # Type error!
```

---

## 📚 Documentation

### Module Docstrings
```python
"""
Task queue management module.

This module provides FIFO and priority-based task queue implementations
for the Jarvis scheduler.

Example:
    queue = TaskQueue()
    queue.enqueue(task)
    next_task = queue.dequeue()
"""
```

### Function Docstrings
```python
def schedule_task(task: Task, nodes: List[Node]) -> Optional[Node]:
    """
    Schedule a task to an available node.
    
    Finds the first node with sufficient resources to run the task,
    assigns the task to that node, and updates the state.
    
    Args:
        task: The task to schedule with resource requirements
        nodes: List of available worker nodes
    
    Returns:
        The selected node if scheduling succeeded, None otherwise
    
    Raises:
        SchedulerError: If task is invalid or nodes list is empty
        StateError: If state update fails
    
    Example:
        >>> scheduler = Scheduler()
        >>> task = Task(image="ubuntu", command="echo hello")
        >>> node = scheduler.schedule_task(task, available_nodes)
        >>> print(f"Scheduled to {node.id}")
    """
    pass
```

### Class Docstrings
```python
class TaskQueue:
    """
    FIFO task queue for scheduler.
    
    Maintains a first-in-first-out queue of pending tasks. Thread-safe
    for concurrent access from multiple scheduler threads.
    
    Attributes:
        max_size: Maximum queue size (None for unlimited)
        size: Current number of tasks in queue
    
    Example:
        >>> queue = TaskQueue(max_size=1000)
        >>> queue.enqueue(task1)
        >>> queue.enqueue(task2)
        >>> next_task = queue.dequeue()
    """
    
    def __init__(self, max_size: Optional[int] = None):
        """
        Initialize task queue.
        
        Args:
            max_size: Maximum queue size, None for unlimited
        """
        pass
```

### Inline Comments
```python
# ✅ Good: Explain WHY, not WHAT
def calculate_score(node: Node) -> float:
    # Use weighted average to prefer nodes with more available resources
    # while still considering current load
    resource_weight = 0.7
    load_weight = 0.3
    return (resource_score * resource_weight) + (load_score * load_weight)

# ❌ Bad: Obvious comments
def calculate_score(node: Node) -> float:
    # Calculate the score
    score = 0
    # Return the score
    return score
```

---

## 🏗️ Code Structure

### Import Organization
```python
# ✅ Good: Organized imports (use isort)
# Standard library
import os
import sys
from typing import List, Optional

# Third-party
import docker
import yaml
from fastapi import FastAPI

# Local
from jarvis.config import Config
from jarvis.exceptions import SchedulerError
from jarvis.models import Task, Node
```

### Function Length
- **Ideal**: 10-30 lines
- **Maximum**: 50 lines
- **If longer**: Break into smaller functions

### Class Structure
```python
class Scheduler:
    """Class docstring."""
    
    # Class constants
    MAX_RETRIES = 3
    
    def __init__(self, config: Config):
        """Constructor."""
        # Public attributes
        self.config = config
        
        # Private attributes
        self._queue = TaskQueue()
        self._running = False
    
    # Public methods first
    def start(self) -> None:
        """Start scheduler."""
        pass
    
    def stop(self) -> None:
        """Stop scheduler."""
        pass
    
    # Private methods last
    def _internal_method(self) -> None:
        """Internal helper."""
        pass
```

---

## 🧪 Error Handling

### Use Specific Exceptions
```python
# ✅ Good: Specific exceptions
from jarvis.exceptions import TaskError, SchedulerError

def schedule_task(task: Task) -> Node:
    if not task.is_valid():
        raise TaskError(f"Invalid task: {task.id}")
    
    if not self._has_available_nodes():
        raise SchedulerError("No available nodes")
    
    return selected_node

# ❌ Bad: Generic exceptions
def schedule_task(task: Task) -> Node:
    if not task.is_valid():
        raise Exception("Bad task")  # Too generic
```

### Exception Docstrings
```python
class TaskError(Exception):
    """
    Raised when task validation or execution fails.
    
    Args:
        message: Error description
        task_id: ID of the task that failed
    """
    
    def __init__(self, message: str, task_id: Optional[str] = None):
        super().__init__(message)
        self.task_id = task_id
```

---

## 🔐 Security Best Practices

### Input Validation
```python
# ✅ Good: Validate all inputs
def submit_task(task_spec: dict) -> Task:
    # Validate required fields
    if "image" not in task_spec:
        raise TaskError("Missing required field: image")
    
    # Sanitize inputs
    image = task_spec["image"].strip()
    if not is_valid_image_name(image):
        raise TaskError(f"Invalid image name: {image}")
    
    # Validate resource limits
    if "cpu" in task_spec:
        cpu = float(task_spec["cpu"])
        if cpu <= 0 or cpu > 32:
            raise TaskError(f"Invalid CPU request: {cpu}")
    
    return Task(**task_spec)
```

### Avoid Injection
```python
# ✅ Good: Use parameterized queries/commands
command = ["docker", "run", "--rm", image]
subprocess.run(command, check=True)

# ❌ Bad: String interpolation
command = f"docker run --rm {image}"  # Command injection risk!
os.system(command)
```

---

## ✅ Code Quality Checklist

Before committing code:

### Functionality
- [ ] Code works as intended
- [ ] Edge cases handled
- [ ] Errors handled gracefully
- [ ] No hardcoded values (use config)

### Style
- [ ] Follows PEP 8
- [ ] Type hints on all functions
- [ ] Docstrings on all public APIs
- [ ] Meaningful variable names
- [ ] No commented-out code

### Quality
- [ ] No duplicate code
- [ ] Functions are focused (single responsibility)
- [ ] Classes have clear purpose
- [ ] Imports organized
- [ ] No circular dependencies

### Testing
- [ ] Unit tests written
- [ ] Tests pass
- [ ] Edge cases tested
- [ ] Coverage > 70%

### Security
- [ ] Input validated
- [ ] No SQL/command injection risks
- [ ] No hardcoded secrets
- [ ] Sensitive data not logged

---

## 🛠️ Development Tools

### Required Tools
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Format code
black --line-length 100 jarvis/

# Sort imports
isort jarvis/

# Type checking
mypy jarvis/

# Linting
flake8 jarvis/
pylint jarvis/

# Run tests
pytest tests/
```

### Pre-commit Hooks
Set up pre-commit hooks to enforce standards:
```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

---

## 🔗 Related Standards

- **Documentation Standards**: [documentation-standards.md](documentation-standards.md)
- **Git Workflow**: [git-workflow.md](git-workflow.md)
- **Testing Standards**: See REQUIREMENTS.md in implementation repo

---

## 📚 External References

- **PEP 8**: https://pep8.org/
- **PEP 257**: https://www.python.org/dev/peps/pep-0257/
- **PEP 484**: https://www.python.org/dev/peps/pep-0484/
- **Google Python Style Guide**: https://google.github.io/styleguide/pyguide.html
- **Black Formatter**: https://black.readthedocs.io/

---

**Applies To**: Jarvis implementation repository  
**Last Updated**: 2026-01-08  
**Enforcement**: Via pre-commit hooks and code review  
**Next**: Return to [Agent Instructions Index](index.md) or [Main Index](../INDEX.md)
