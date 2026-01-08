"""
Example: Health Monitoring Agent

This example demonstrates a monitoring agent that checks node health
and detects failures in a Jarvis cluster.

Run this example:
    python3 src/examples/agents/health_monitor_example.py
"""

import asyncio
import logging
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base_agent import Event, MonitoringAgent

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


class Node:
    """Mock node class for demonstration."""

    def __init__(self, node_id: str):
        """Initialize node."""
        self.node_id = node_id
        self.last_heartbeat = datetime.now()
        self.status = "healthy"
        self.cpu_usage = 0.0
        self.memory_usage = 0.0

    def send_heartbeat(self):
        """Simulate sending a heartbeat."""
        self.last_heartbeat = datetime.now()

    def is_responsive(self, timeout_seconds: int = 30) -> bool:
        """Check if node is responsive based on heartbeat."""
        elapsed = (datetime.now() - self.last_heartbeat).total_seconds()
        return elapsed < timeout_seconds


class HealthMonitorAgent(MonitoringAgent):
    """
    Health monitoring agent that checks node heartbeats and status.

    This agent:
    - Monitors node heartbeats
    - Detects unresponsive nodes
    - Tracks node health metrics
    - Emits events when issues are detected
    """

    def __init__(self, agent_id: str, config: Dict):
        """Initialize health monitor agent."""
        super().__init__(agent_id, config)

        # Configuration
        self.heartbeat_timeout = config.get("heartbeat_timeout", 30)
        self.failure_threshold = config.get("failure_threshold", 3)

        # State
        self.nodes: Dict[str, Node] = {}
        self.failure_counts: Dict[str, int] = {}
        self.events: List[Event] = []

    def register_node(self, node: Node):
        """
        Register a node for monitoring.

        Args:
            node: Node to monitor
        """
        self.nodes[node.node_id] = node
        self.failure_counts[node.node_id] = 0

        self.logger.info(
            "Node registered for monitoring",
            extra={"node_id": node.node_id},
        )

    def unregister_node(self, node_id: str):
        """
        Unregister a node from monitoring.

        Args:
            node_id: ID of node to unregister
        """
        if node_id in self.nodes:
            del self.nodes[node_id]
            del self.failure_counts[node_id]

            self.logger.info(
                "Node unregistered from monitoring",
                extra={"node_id": node_id},
            )

    async def check(self):
        """
        Perform health check on all registered nodes.

        This is the main monitoring logic that runs periodically.
        """
        self.logger.debug(
            "Performing health check",
            extra={"node_count": len(self.nodes)},
        )

        for node_id, node in self.nodes.items():
            await self._check_node(node)

    async def _check_node(self, node: Node):
        """
        Check health of a single node.

        Args:
            node: Node to check
        """
        is_responsive = node.is_responsive(self.heartbeat_timeout)

        if not is_responsive:
            # Node is not responsive
            self.failure_counts[node.node_id] += 1

            self.logger.warning(
                "Node unresponsive",
                extra={
                    "node_id": node.node_id,
                    "failure_count": self.failure_counts[node.node_id],
                    "last_heartbeat": node.last_heartbeat.isoformat(),
                },
            )

            # Check if we've exceeded failure threshold
            if self.failure_counts[node.node_id] >= self.failure_threshold:
                await self._handle_node_failure(node)

        else:
            # Node is responsive - reset failure count
            if self.failure_counts[node.node_id] > 0:
                self.logger.info(
                    "Node recovered",
                    extra={"node_id": node.node_id},
                )
                self.failure_counts[node.node_id] = 0

    async def _handle_node_failure(self, node: Node):
        """
        Handle a node failure.

        Args:
            node: Failed node
        """
        self.logger.error(
            "Node failure detected",
            extra={
                "node_id": node.node_id,
                "failure_count": self.failure_counts[node.node_id],
            },
        )

        # Mark node as unhealthy
        node.status = "unhealthy"

        # Create and emit failure event
        event = Event(
            event_type="node_failure",
            source=self.agent_id,
            data={
                "node_id": node.node_id,
                "failure_count": self.failure_counts[node.node_id],
                "last_heartbeat": node.last_heartbeat.isoformat(),
            },
            timestamp=datetime.now(),
        )

        self.events.append(event)

        # In a real implementation, this would publish to an event bus
        self.logger.info(
            "Node failure event emitted",
            extra={"node_id": node.node_id, "event_type": event.event_type},
        )


async def simulate_cluster():
    """Simulate a cluster with nodes and monitoring."""
    print("\n" + "=" * 60)
    print("Health Monitor Agent Example")
    print("=" * 60 + "\n")

    # Create health monitor agent
    config = {
        "check_interval": 2,  # Check every 2 seconds
        "heartbeat_timeout": 5,  # 5 second timeout
        "failure_threshold": 2,  # 2 failures = node down
    }

    monitor = HealthMonitorAgent("health-monitor-1", config)

    # Create and register nodes
    nodes = [Node(f"node-{i}") for i in range(1, 4)]

    for node in nodes:
        monitor.register_node(node)

    print(f"Registered {len(nodes)} nodes for monitoring\n")

    # Start the monitor
    await monitor.start()

    print("Simulating cluster operations...\n")

    # Simulate 10 seconds of operation
    for i in range(10):
        await asyncio.sleep(1)

        # Simulate different scenarios
        if i < 3:
            # All nodes send heartbeats
            for node in nodes:
                node.send_heartbeat()
            print(f"[{i}s] All nodes healthy")

        elif i < 6:
            # Node-2 stops sending heartbeats
            nodes[0].send_heartbeat()
            nodes[2].send_heartbeat()
            # nodes[1] doesn't send heartbeat (simulating failure)
            print(f"[{i}s] Node-2 not responding...")

        else:
            # Node-2 recovers
            for node in nodes:
                node.send_heartbeat()
            print(f"[{i}s] Node-2 recovered")

    # Stop the monitor
    await monitor.stop()

    # Print results
    print("\n" + "=" * 60)
    print("Monitoring Results")
    print("=" * 60 + "\n")

    health = await monitor.health_check()
    print(f"Events detected: {len(monitor.events)}")
    print(f"Agent status: {health['status']}")
    print(f"Events processed: {health['metrics']['events_processed']}")

    if monitor.events:
        print("\nFailure Events:")
        for event in monitor.events:
            print(f"  - {event.event_type}: {event.data['node_id']}")

    print("\nNode Status:")
    for node in nodes:
        print(f"  - {node.node_id}: {node.status}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    asyncio.run(simulate_cluster())
