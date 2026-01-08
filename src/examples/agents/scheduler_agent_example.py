"""
Example: Task Scheduler Agent

This example demonstrates a scheduling agent that assigns tasks to nodes
based on available resources.

Run this example:
    python3 src/examples/agents/scheduler_agent_example.py
"""

import asyncio
import logging
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base_agent import Event, SchedulingAgent

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


@dataclass
class Task:
    """Task to be scheduled."""

    task_id: str
    cpu_required: float
    memory_required: float
    priority: int = 0
    assigned_node: Optional[str] = None


@dataclass
class Node:
    """Cluster node."""

    node_id: str
    cpu_available: float
    memory_available: float
    cpu_total: float
    memory_total: float
    assigned_tasks: List[str] = None

    def __post_init__(self):
        """Initialize assigned_tasks if not provided."""
        if self.assigned_tasks is None:
            self.assigned_tasks = []

    def has_capacity(self, cpu: float, memory: float) -> bool:
        """Check if node has capacity for task."""
        return self.cpu_available >= cpu and self.memory_available >= memory

    def allocate(self, task: Task):
        """Allocate resources for task."""
        self.cpu_available -= task.cpu_required
        self.memory_available -= task.memory_required
        self.assigned_tasks.append(task.task_id)

    def deallocate(self, task: Task):
        """Deallocate resources from task."""
        self.cpu_available += task.cpu_required
        self.memory_available += task.memory_required
        if task.task_id in self.assigned_tasks:
            self.assigned_tasks.remove(task.task_id)


class TaskSchedulerAgent(SchedulingAgent):
    """
    Task scheduler agent that assigns tasks to nodes.

    This agent:
    - Maintains a queue of pending tasks
    - Finds suitable nodes for tasks
    - Assigns tasks based on resource availability
    - Handles scheduling failures
    """

    def __init__(self, agent_id: str, config: Dict):
        """Initialize task scheduler agent."""
        super().__init__(agent_id, config)

        # State
        self.nodes: Dict[str, Node] = {}
        self.task_queue: List[Task] = []
        self.scheduled_tasks: Dict[str, Task] = {}

        # Configuration
        self.schedule_interval = config.get("schedule_interval", 1)

    def register_node(self, node: Node):
        """Register a node for scheduling."""
        self.nodes[node.node_id] = node
        self.logger.info(
            "Node registered",
            extra={
                "node_id": node.node_id,
                "cpu": node.cpu_total,
                "memory": node.memory_total,
            },
        )

    def submit_task(self, task: Task):
        """Submit a task for scheduling."""
        self.task_queue.append(task)
        self.logger.info(
            "Task submitted",
            extra={
                "task_id": task.task_id,
                "cpu": task.cpu_required,
                "memory": task.memory_required,
                "priority": task.priority,
            },
        )

    async def run(self):
        """Main scheduler loop."""
        while self.running:
            try:
                await self._process_queue()
                await asyncio.sleep(self.schedule_interval)
            except Exception as e:
                self.logger.error(
                    "Error in scheduler loop",
                    exc_info=True,
                    extra={"error": str(e)},
                )
                self.metrics.errors_encountered += 1

    async def _process_queue(self):
        """Process task queue and schedule tasks."""
        if not self.task_queue:
            return

        # Sort by priority (higher priority first)
        self.task_queue.sort(key=lambda t: t.priority, reverse=True)

        tasks_to_remove = []

        for task in self.task_queue:
            node_id = await self.schedule_task(task)
            if node_id:
                tasks_to_remove.append(task)
                self.scheduled_tasks[task.task_id] = task

        # Remove scheduled tasks from queue
        for task in tasks_to_remove:
            self.task_queue.remove(task)

    async def schedule_task(self, task: Dict) -> Optional[str]:
        """
        Schedule a task on a suitable node.

        Args:
            task: Task to schedule (can be dict or Task object)

        Returns:
            Node ID where task was scheduled, or None if scheduling failed
        """
        # Handle both dict and Task object
        if isinstance(task, dict):
            task = Task(**task)

        self.logger.debug(
            "Attempting to schedule task",
            extra={"task_id": task.task_id},
        )

        # Find suitable node
        node = self._find_suitable_node(task)

        if node:
            # Allocate resources and assign task
            node.allocate(task)
            task.assigned_node = node.node_id

            self.logger.info(
                "Task scheduled",
                extra={
                    "task_id": task.task_id,
                    "node_id": node.node_id,
                    "cpu_remaining": node.cpu_available,
                    "memory_remaining": node.memory_available,
                },
            )

            self.metrics.tasks_completed += 1
            return node.node_id

        else:
            self.logger.warning(
                "No suitable node found for task",
                extra={
                    "task_id": task.task_id,
                    "cpu_required": task.cpu_required,
                    "memory_required": task.memory_required,
                },
            )
            return None

    def _find_suitable_node(self, task: Task) -> Optional[Node]:
        """
        Find a suitable node for the task.

        Uses a simple best-fit strategy: choose node with least available
        resources that can still accommodate the task.

        Args:
            task: Task to schedule

        Returns:
            Suitable node or None if no node has capacity
        """
        suitable_nodes = [
            node
            for node in self.nodes.values()
            if node.has_capacity(task.cpu_required, task.memory_required)
        ]

        if not suitable_nodes:
            return None

        # Best-fit: choose node with least available resources
        return min(
            suitable_nodes,
            key=lambda n: (n.cpu_available, n.memory_available),
        )


async def simulate_scheduling():
    """Simulate task scheduling."""
    print("\n" + "=" * 60)
    print("Task Scheduler Agent Example")
    print("=" * 60 + "\n")

    # Create scheduler agent
    config = {"schedule_interval": 0.5}
    scheduler = TaskSchedulerAgent("task-scheduler-1", config)

    # Register nodes
    nodes = [
        Node("node-1", cpu_available=4.0, memory_available=8.0, cpu_total=4.0, memory_total=8.0),
        Node("node-2", cpu_available=8.0, memory_available=16.0, cpu_total=8.0, memory_total=16.0),
        Node("node-3", cpu_available=2.0, memory_available=4.0, cpu_total=2.0, memory_total=4.0),
    ]

    for node in nodes:
        scheduler.register_node(node)

    print(f"Registered {len(nodes)} nodes\n")

    # Start scheduler
    await scheduler.start()

    print("Submitting tasks...\n")

    # Submit tasks
    tasks = [
        Task("task-1", cpu_required=2.0, memory_required=4.0, priority=1),
        Task("task-2", cpu_required=1.0, memory_required=2.0, priority=5),  # High priority
        Task("task-3", cpu_required=4.0, memory_required=8.0, priority=3),
        Task("task-4", cpu_required=1.0, memory_required=1.0, priority=2),
        Task("task-5", cpu_required=10.0, memory_required=20.0, priority=1),  # Won't fit
    ]

    for task in tasks:
        scheduler.submit_task(task)

    # Wait for scheduling
    await asyncio.sleep(3)

    # Stop scheduler
    await scheduler.stop()

    # Print results
    print("\n" + "=" * 60)
    print("Scheduling Results")
    print("=" * 60 + "\n")

    health = await scheduler.health_check()
    print(f"Tasks scheduled: {health['metrics']['tasks_completed']}")
    print(f"Tasks pending: {len(scheduler.task_queue)}")

    print("\nTask Assignments:")
    for task in tasks:
        if task.assigned_node:
            print(f"  - {task.task_id}: {task.assigned_node}")
        else:
            print(f"  - {task.task_id}: NOT SCHEDULED")

    print("\nNode Resource Usage:")
    for node in nodes:
        cpu_used = node.cpu_total - node.cpu_available
        memory_used = node.memory_total - node.memory_available
        print(
            f"  - {node.node_id}: "
            f"CPU {cpu_used:.1f}/{node.cpu_total:.1f}, "
            f"Memory {memory_used:.1f}/{node.memory_total:.1f}, "
            f"Tasks: {len(node.assigned_tasks)}"
        )

    print("\n" + "=" * 60)


if __name__ == "__main__":
    asyncio.run(simulate_scheduling())
