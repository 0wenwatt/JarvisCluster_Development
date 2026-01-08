# Source Code Directory

This directory is for code examples, prototypes, and reference implementations related to the JarvisCluster_Development repository.

## Important Note

⚠️ **This is NOT the main Jarvis implementation repository.**

The actual Jarvis cluster management system is implemented in a separate repository. This `src/` directory is for:
- Code examples demonstrating concepts
- Prototype implementations for testing ideas
- Reference implementations of algorithms
- Helper scripts specific to this development/planning repo
- Small utilities for documentation or tracking

## Purpose

Store supplementary code such as:
- **Examples**: Sample code illustrating design patterns
- **Prototypes**: Quick proof-of-concept implementations
- **Utilities**: Scripts for processing documentation or data
- **Templates**: Code templates for the main implementation
- **Tools**: Development and planning helper tools

## Organization

Suggested structure:

```
src/
├── examples/           # Example implementations
│   ├── scheduler_example.py
│   └── task_queue_example.py
├── prototypes/         # Proof-of-concept code
│   └── load_balancer_prototype.py
├── utilities/          # Helper scripts
│   ├── doc_generator.py
│   └── tree_parser.py
└── templates/          # Code templates
    └── component_template.py
```

## What Goes Here vs. Main Repo

| Location | Purpose | Examples |
|----------|---------|----------|
| **This repo** (`src/`) | Planning, examples, utilities | Documentation tools, algorithm prototypes, planning scripts |
| **Main Jarvis repo** | Actual implementation | Production scheduler, API server, worker nodes |

## Code Standards

Code in this directory should:
1. Follow Python best practices (PEP 8)
2. Include docstrings and comments
3. Be well-documented with README files
4. Serve a clear educational or utility purpose
5. Not duplicate production code

## Examples

### Example File Structure

```python
"""
Example: Simple Task Queue Implementation

This demonstrates the basic concept of a priority queue
for task scheduling in Jarvis.

Note: This is a simplified example. The actual implementation
is in the main Jarvis repository with additional features.
"""

import heapq
from typing import Any, List, Tuple

class SimplePriorityQueue:
    """Example priority queue for task scheduling."""
    
    def __init__(self):
        self._queue: List[Tuple[int, Any]] = []
    
    def enqueue(self, item: Any, priority: int):
        """Add item with given priority (lower = higher priority)."""
        heapq.heappush(self._queue, (priority, item))
    
    def dequeue(self) -> Any:
        """Remove and return highest priority item."""
        if self._queue:
            return heapq.heappop(self._queue)[1]
        return None
```

## Running Code

Most code here should be standalone or have minimal dependencies:

```bash
# Run an example
python3 src/examples/scheduler_example.py

# Run a utility
python3 src/utilities/doc_generator.py
```

## Dependencies

If code requires dependencies:
1. Document them in a README or docstring
2. Consider adding a `requirements.txt` for this directory
3. Keep dependencies minimal and well-justified

## Testing

Code examples should be:
- Self-contained
- Easy to understand
- Demonstrating one concept at a time
- Tested (if complex)

## Contributing

When adding code to this directory:
1. Create a README in the subdirectory
2. Document the purpose and usage
3. Include examples of running the code
4. Keep it simple and focused
5. Link to related design documents

## Related Documentation

- [DESIGN_PLAN.md](../DESIGN_PLAN.md) - Architecture that examples illustrate
- [USE_CASES.md](../USE_CASES.md) - Use cases that code demonstrates
- [REQUIREMENTS.md](../REQUIREMENTS.md) - Coding standards to follow
