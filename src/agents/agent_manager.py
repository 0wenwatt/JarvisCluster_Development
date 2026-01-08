"""
Agent Manager for Jarvis Cluster Management System

The Agent Manager coordinates multiple agents, handles their lifecycle,
and facilitates communication between agents.

Example Usage:
    from agent_manager import AgentManager
    from monitoring_agent import HealthMonitorAgent

    manager = AgentManager()
    manager.register_agent_type("health_monitor", HealthMonitorAgent)

    config = {"check_interval": 5, "timeout": 30}
    await manager.create_agent("health-monitor-1", "health_monitor", config)

    await manager.start_all()
"""

import asyncio
import logging
from typing import Any, Callable, Dict, List, Optional, Type

from base_agent import BaseAgent, Event


class AgentManager:
    """
    Manages multiple agents in the Jarvis cluster.

    The Agent Manager:
    - Registers agent types
    - Creates and manages agent instances
    - Coordinates agent lifecycle (start, stop)
    - Facilitates agent communication via events
    - Monitors agent health
    """

    def __init__(self):
        """Initialize the agent manager."""
        self.logger = logging.getLogger("jarvis.agent_manager")

        # Registry of agent types (name -> class)
        self._agent_types: Dict[str, Type[BaseAgent]] = {}

        # Active agent instances (agent_id -> agent)
        self._agents: Dict[str, BaseAgent] = {}

        # Event bus for agent communication
        self._event_queue: asyncio.Queue = asyncio.Queue()
        self._event_subscribers: Dict[str, List[BaseAgent]] = {}

        # Manager state
        self.running = False

        self.logger.info("Agent manager initialized")

    def register_agent_type(self, name: str, agent_class: Type[BaseAgent]):
        """
        Register an agent type.

        Args:
            name: Name to register the agent type under
            agent_class: Agent class (must inherit from BaseAgent)

        Example:
            manager.register_agent_type("health_monitor", HealthMonitorAgent)
        """
        if not issubclass(agent_class, BaseAgent):
            raise ValueError(f"Agent class must inherit from BaseAgent: {agent_class}")

        self._agent_types[name] = agent_class
        self.logger.info(
            "Agent type registered",
            extra={"agent_type": name, "class": agent_class.__name__},
        )

    async def create_agent(
        self, agent_id: str, agent_type: str, config: Dict[str, Any]
    ) -> BaseAgent:
        """
        Create a new agent instance.

        Args:
            agent_id: Unique identifier for the agent
            agent_type: Type of agent (must be registered)
            config: Agent configuration

        Returns:
            Created agent instance

        Raises:
            ValueError: If agent_type not registered or agent_id already exists

        Example:
            config = {"check_interval": 5}
            agent = await manager.create_agent("health-1", "health_monitor", config)
        """
        if agent_id in self._agents:
            raise ValueError(f"Agent already exists: {agent_id}")

        if agent_type not in self._agent_types:
            raise ValueError(f"Unknown agent type: {agent_type}")

        agent_class = self._agent_types[agent_type]
        agent = agent_class(agent_id, config)

        self._agents[agent_id] = agent

        self.logger.info(
            "Agent created",
            extra={"agent_id": agent_id, "agent_type": agent_type},
        )

        return agent

    async def start_agent(self, agent_id: str):
        """
        Start a specific agent.

        Args:
            agent_id: ID of agent to start

        Raises:
            ValueError: If agent not found
        """
        if agent_id not in self._agents:
            raise ValueError(f"Agent not found: {agent_id}")

        agent = self._agents[agent_id]
        await agent.start()

        self.logger.info("Agent started", extra={"agent_id": agent_id})

    async def stop_agent(self, agent_id: str):
        """
        Stop a specific agent.

        Args:
            agent_id: ID of agent to stop

        Raises:
            ValueError: If agent not found
        """
        if agent_id not in self._agents:
            raise ValueError(f"Agent not found: {agent_id}")

        agent = self._agents[agent_id]
        await agent.stop()

        self.logger.info("Agent stopped", extra={"agent_id": agent_id})

    async def remove_agent(self, agent_id: str):
        """
        Stop and remove an agent.

        Args:
            agent_id: ID of agent to remove
        """
        if agent_id in self._agents:
            await self.stop_agent(agent_id)
            del self._agents[agent_id]

            self.logger.info("Agent removed", extra={"agent_id": agent_id})

    async def start_all(self):
        """Start all registered agents."""
        self.logger.info(f"Starting {len(self._agents)} agents")

        tasks = [agent.start() for agent in self._agents.values()]
        await asyncio.gather(*tasks, return_exceptions=True)

        self.running = True
        self.logger.info("All agents started")

    async def stop_all(self):
        """Stop all agents gracefully."""
        self.logger.info(f"Stopping {len(self._agents)} agents")

        self.running = False

        tasks = [agent.stop() for agent in self._agents.values()]
        await asyncio.gather(*tasks, return_exceptions=True)

        self.logger.info("All agents stopped")

    def get_agent(self, agent_id: str) -> Optional[BaseAgent]:
        """
        Get an agent by ID.

        Args:
            agent_id: Agent identifier

        Returns:
            Agent instance or None if not found
        """
        return self._agents.get(agent_id)

    def list_agents(self) -> List[Dict[str, Any]]:
        """
        List all agents with their status.

        Returns:
            List of agent information dictionaries
        """
        return [
            {
                "agent_id": agent.agent_id,
                "agent_type": agent.agent_type.value,
                "status": agent.status.value,
            }
            for agent in self._agents.values()
        ]

    async def publish_event(self, event: Event):
        """
        Publish an event to all subscribed agents.

        Args:
            event: Event to publish

        Example:
            event = Event(
                event_type="node_failure",
                source="monitor",
                data={"node_id": "node-1"},
                timestamp=datetime.now()
            )
            await manager.publish_event(event)
        """
        self.logger.debug(
            "Publishing event",
            extra={"event_type": event.event_type, "source": event.source},
        )

        # Get subscribers for this event type
        subscribers = self._event_subscribers.get(event.event_type, [])

        # Send event to all subscribers
        tasks = [agent.handle_event(event) for agent in subscribers]
        await asyncio.gather(*tasks, return_exceptions=True)

    def subscribe(self, agent_id: str, event_type: str):
        """
        Subscribe an agent to an event type.

        Args:
            agent_id: ID of agent to subscribe
            event_type: Type of event to subscribe to

        Raises:
            ValueError: If agent not found

        Example:
            manager.subscribe("recovery-agent-1", "node_failure")
        """
        if agent_id not in self._agents:
            raise ValueError(f"Agent not found: {agent_id}")

        agent = self._agents[agent_id]

        if event_type not in self._event_subscribers:
            self._event_subscribers[event_type] = []

        if agent not in self._event_subscribers[event_type]:
            self._event_subscribers[event_type].append(agent)

            self.logger.debug(
                "Agent subscribed to event",
                extra={"agent_id": agent_id, "event_type": event_type},
            )

    def unsubscribe(self, agent_id: str, event_type: str):
        """
        Unsubscribe an agent from an event type.

        Args:
            agent_id: ID of agent to unsubscribe
            event_type: Type of event to unsubscribe from
        """
        if agent_id not in self._agents:
            return

        agent = self._agents[agent_id]

        if event_type in self._event_subscribers:
            subscribers = self._event_subscribers[event_type]
            if agent in subscribers:
                subscribers.remove(agent)

                self.logger.debug(
                    "Agent unsubscribed from event",
                    extra={"agent_id": agent_id, "event_type": event_type},
                )

    async def health_check(self) -> Dict[str, Any]:
        """
        Check health of all agents.

        Returns:
            Dictionary with health status of all agents
        """
        health_checks = {}

        for agent_id, agent in self._agents.items():
            try:
                health = await agent.health_check()
                health_checks[agent_id] = health
            except Exception as e:
                health_checks[agent_id] = {
                    "healthy": False,
                    "error": str(e),
                }

        overall_healthy = all(
            status.get("healthy", False) for status in health_checks.values()
        )

        return {
            "overall_healthy": overall_healthy,
            "total_agents": len(self._agents),
            "agents": health_checks,
        }
