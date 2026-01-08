"""
Example: Structured Logging in Jarvis

This example demonstrates best practices for logging in the Jarvis cluster
management system, including:
- Structured logging with context
- Correlation IDs for distributed tracing
- Component-specific loggers
- Performance monitoring
- Error handling

Run this example:
    python3 src/examples/logging/structured_logging_example.py
"""

import logging
import time
from typing import Dict, List, Optional

# In actual implementation, import from jarvis.logging
# from jarvis.logging import get_logger, set_correlation_id, StructuredLogger

# For this example, use simple setup
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class TaskSchedulerExample:
    """Example task scheduler with proper logging."""

    def __init__(self):
        """Initialize scheduler with logger."""
        self.logger = logging.getLogger("jarvis.scheduler")
        self.logger.info("Task scheduler initialized")

    def schedule_task(self, task_id: str, node_id: str, priority: int = 0) -> bool:
        """
        Schedule a task on a node.

        This demonstrates proper logging with structured context.
        """
        start_time = time.time()

        # Log the scheduling attempt with context
        self.logger.info(
            "Attempting to schedule task",
            extra={"task_id": task_id, "node_id": node_id, "priority": priority},
        )

        try:
            # Simulate task scheduling logic
            self._validate_task(task_id)
            self._check_node_availability(node_id)
            self._assign_task_to_node(task_id, node_id)

            duration_ms = (time.time() - start_time) * 1000

            # Log successful completion with metrics
            self.logger.info(
                "Task scheduled successfully",
                extra={
                    "task_id": task_id,
                    "node_id": node_id,
                    "priority": priority,
                    "duration_ms": round(duration_ms, 2),
                },
            )

            return True

        except ValueError as e:
            # Log validation errors at WARNING level
            self.logger.warning(
                "Task validation failed",
                extra={"task_id": task_id, "error": str(e)},
            )
            return False

        except Exception as e:
            # Log unexpected errors at ERROR level with full traceback
            self.logger.error(
                "Failed to schedule task",
                exc_info=True,
                extra={"task_id": task_id, "node_id": node_id, "error": str(e)},
            )
            return False

    def _validate_task(self, task_id: str):
        """Validate task ID."""
        self.logger.debug("Validating task", extra={"task_id": task_id})
        if not task_id or not task_id.startswith("task-"):
            raise ValueError(f"Invalid task ID: {task_id}")

    def _check_node_availability(self, node_id: str):
        """Check if node is available."""
        self.logger.debug("Checking node availability", extra={"node_id": node_id})
        # Simulate check
        if node_id == "node-unavailable":
            raise RuntimeError("Node unavailable")

    def _assign_task_to_node(self, task_id: str, node_id: str):
        """Assign task to node."""
        self.logger.debug(
            "Assigning task to node",
            extra={"task_id": task_id, "node_id": node_id},
        )
        # Simulate assignment
        time.sleep(0.1)


class WorkerNodeExample:
    """Example worker node with proper logging."""

    def __init__(self, node_id: str):
        """Initialize worker node with logger."""
        self.node_id = node_id
        self.logger = logging.getLogger(f"jarvis.worker.{node_id}")
        self.logger.info("Worker node initialized", extra={"node_id": node_id})

    def execute_task(self, task_id: str) -> Dict:
        """
        Execute a task.

        Demonstrates logging task execution lifecycle.
        """
        self.logger.info(
            "Starting task execution",
            extra={"task_id": task_id, "node_id": self.node_id},
        )

        start_time = time.time()
        result = {"status": "success", "output": None}

        try:
            # Log progress at different stages
            self.logger.debug("Pulling container image", extra={"task_id": task_id})
            time.sleep(0.05)

            self.logger.debug("Creating container", extra={"task_id": task_id})
            time.sleep(0.05)

            self.logger.debug("Starting container", extra={"task_id": task_id})
            time.sleep(0.1)

            # Simulate task completion
            result["output"] = "Task completed successfully"
            duration_ms = (time.time() - start_time) * 1000

            self.logger.info(
                "Task execution completed",
                extra={
                    "task_id": task_id,
                    "node_id": self.node_id,
                    "status": result["status"],
                    "duration_ms": round(duration_ms, 2),
                },
            )

        except Exception as e:
            result["status"] = "failed"
            result["error"] = str(e)

            self.logger.error(
                "Task execution failed",
                exc_info=True,
                extra={"task_id": task_id, "node_id": self.node_id},
            )

        return result

    def report_metrics(self):
        """Report node metrics."""
        # Example of periodic metrics logging
        metrics = {
            "cpu_usage_percent": 45.2,
            "memory_usage_mb": 1024,
            "disk_usage_percent": 60.5,
            "active_tasks": 3,
        }

        self.logger.info(
            "Node metrics",
            extra={"node_id": self.node_id, **metrics},
        )


def demonstrate_log_levels():
    """Demonstrate different log levels and when to use them."""
    logger = logging.getLogger("jarvis.examples")

    print("\n" + "=" * 60)
    print("Demonstrating Log Levels")
    print("=" * 60 + "\n")

    # DEBUG: Detailed diagnostic information
    logger.debug(
        "Processing task queue",
        extra={"queue_size": 42, "next_task": "task-123"},
    )

    # INFO: General informational messages
    logger.info(
        "Node registered successfully",
        extra={"node_id": "node-1", "capacity": {"cpu": 4, "memory": 8}},
    )

    # WARNING: Warning messages for potentially problematic situations
    logger.warning(
        "High memory usage detected",
        extra={"node_id": "node-1", "memory_usage_percent": 85},
    )

    # ERROR: Error messages when an operation fails
    logger.error(
        "Failed to connect to state store",
        extra={"store_address": "localhost:2379", "retry_count": 3},
    )

    # CRITICAL: Critical system failures
    logger.critical(
        "Cluster state inconsistent",
        extra={"expected_nodes": 5, "registered_nodes": 3},
    )


def demonstrate_structured_logging():
    """Demonstrate structured logging best practices."""
    print("\n" + "=" * 60)
    print("Demonstrating Structured Logging")
    print("=" * 60 + "\n")

    scheduler = TaskSchedulerExample()

    # Schedule valid tasks
    scheduler.schedule_task("task-001", "node-1", priority=1)
    scheduler.schedule_task("task-002", "node-2", priority=5)

    # Schedule invalid task (demonstrates warning logging)
    scheduler.schedule_task("invalid-task", "node-1")

    # Schedule task on unavailable node (demonstrates error logging)
    scheduler.schedule_task("task-003", "node-unavailable")


def demonstrate_worker_logging():
    """Demonstrate worker node logging."""
    print("\n" + "=" * 60)
    print("Demonstrating Worker Node Logging")
    print("=" * 60 + "\n")

    worker = WorkerNodeExample("node-1")

    # Execute tasks
    worker.execute_task("task-001")
    worker.execute_task("task-002")

    # Report metrics
    worker.report_metrics()


def main():
    """Run all logging examples."""
    print("\n" + "=" * 60)
    print("Jarvis Structured Logging Examples")
    print("=" * 60)

    demonstrate_log_levels()
    demonstrate_structured_logging()
    demonstrate_worker_logging()

    print("\n" + "=" * 60)
    print("Examples completed")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
