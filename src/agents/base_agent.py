"""
Base Agent Classes for Jarvis Cluster Management System

This module provides the base classes and interfaces for building agents
in the Jarvis cluster management system.

Example Usage:
    from base_agent import BaseAgent, AgentStatus

    class MyAgent(BaseAgent):
        async def run(self):
            while self.running:
                # Agent logic
                await asyncio.sleep(10)

    agent = MyAgent("my-agent", config)
    await agent.start()
"""

import asyncio
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional


class AgentStatus(Enum):
    """Agent status enumeration."""

    INITIALIZING = "initializing"
    RUNNING = "running"
    PAUSED = "paused"
    STOPPING = "stopping"
    STOPPED = "stopped"
    ERROR = "error"


class AgentType(Enum):
    """Agent type enumeration."""

    MONITORING = "monitoring"
    SCHEDULING = "scheduling"
    RECOVERY = "recovery"
    OPTIMIZATION = "optimization"
    SECURITY = "security"
    CUSTOM = "custom"


@dataclass
class AgentMetrics:
    """Agent metrics data class."""

    events_processed: int = 0
    tasks_completed: int = 0
    errors_encountered: int = 0
    uptime_seconds: float = 0.0
    last_activity: Optional[datetime] = None


@dataclass
class Event:
    """Event data class for agent communication."""

    event_type: str
    source: str
    data: Dict[str, Any]
    timestamp: datetime
    correlation_id: Optional[str] = None


class BaseAgent(ABC):
    """
    Base class for all Jarvis agents.

    All agents should inherit from this class and implement the required
    abstract methods. The base class provides:
    - Lifecycle management (start, stop)
    - Configuration management
    - Logging
    - Metrics collection
    - Event handling

    Example:
        class MyAgent(BaseAgent):
            async def run(self):
                while self.running:
                    await self._do_work()
                    await asyncio.sleep(10)

            async def _do_work(self):
                # Agent-specific logic
                pass
    """

    def __init__(
        self,
        agent_id: str,
        config: Dict[str, Any],
        agent_type: AgentType = AgentType.CUSTOM,
    ):
        """
        Initialize the agent.

        Args:
            agent_id: Unique identifier for this agent
            config: Agent configuration dictionary
            agent_type: Type of agent
        """
        self.agent_id = agent_id
        self.config = config
        self.agent_type = agent_type

        # Set up logging
        self.logger = logging.getLogger(f"jarvis.agent.{agent_id}")

        # Agent state
        self.status = AgentStatus.INITIALIZING
        self.running = False
        self.start_time: Optional[datetime] = None
        self.metrics = AgentMetrics()

        # Task handle for main loop
        self._run_task: Optional[asyncio.Task] = None

        self.logger.info(
            "Agent initialized",
            extra={
                "agent_id": self.agent_id,
                "agent_type": self.agent_type.value,
            },
        )

    async def start(self):
        """
        Start the agent.

        This method initializes resources and starts the main agent loop.
        Override this method to add custom initialization logic, but make
        sure to call super().start().
        """
        if self.running:
            self.logger.warning("Agent already running", extra={"agent_id": self.agent_id})
            return

        self.logger.info("Starting agent", extra={"agent_id": self.agent_id})

        try:
            self.running = True
            self.start_time = datetime.now()
            self.status = AgentStatus.RUNNING

            # Start the main agent loop
            self._run_task = asyncio.create_task(self._run_wrapper())

            self.logger.info("Agent started", extra={"agent_id": self.agent_id})

        except Exception as e:
            self.status = AgentStatus.ERROR
            self.logger.error(
                "Failed to start agent",
                exc_info=True,
                extra={"agent_id": self.agent_id, "error": str(e)},
            )
            raise

    async def stop(self):
        """
        Stop the agent gracefully.

        This method stops the main agent loop and cleans up resources.
        Override this method to add custom cleanup logic, but make sure
        to call super().stop().
        """
        if not self.running:
            self.logger.warning("Agent not running", extra={"agent_id": self.agent_id})
            return

        self.logger.info("Stopping agent", extra={"agent_id": self.agent_id})

        try:
            self.status = AgentStatus.STOPPING
            self.running = False

            # Wait for main loop to finish
            if self._run_task:
                self._run_task.cancel()
                try:
                    await self._run_task
                except asyncio.CancelledError:
                    pass

            self.status = AgentStatus.STOPPED

            self.logger.info("Agent stopped", extra={"agent_id": self.agent_id})

        except Exception as e:
            self.status = AgentStatus.ERROR
            self.logger.error(
                "Error stopping agent",
                exc_info=True,
                extra={"agent_id": self.agent_id, "error": str(e)},
            )
            raise

    async def _run_wrapper(self):
        """
        Wrapper around the run method with error handling.

        This wrapper ensures that exceptions in the agent loop are caught
        and logged properly.
        """
        try:
            await self.run()
        except asyncio.CancelledError:
            self.logger.info("Agent run loop cancelled", extra={"agent_id": self.agent_id})
        except Exception as e:
            self.status = AgentStatus.ERROR
            self.logger.error(
                "Agent run loop failed",
                exc_info=True,
                extra={"agent_id": self.agent_id, "error": str(e)},
            )

    @abstractmethod
    async def run(self):
        """
        Main agent loop.

        This method contains the main logic of the agent. It should run
        continuously while self.running is True.

        Example:
            async def run(self):
                while self.running:
                    # Do work
                    await self._process_events()
                    await asyncio.sleep(self.config.get("interval", 10))
        """
        pass

    async def handle_event(self, event: Event):
        """
        Handle an event.

        Override this method to implement event handling. The base
        implementation just logs the event.

        Args:
            event: Event to handle
        """
        self.logger.debug(
            "Received event",
            extra={
                "agent_id": self.agent_id,
                "event_type": event.event_type,
                "source": event.source,
            },
        )
        self.metrics.events_processed += 1
        self.metrics.last_activity = datetime.now()

    async def health_check(self) -> Dict[str, Any]:
        """
        Perform health check.

        Returns:
            Dictionary with health status information

        Example:
            {
                "healthy": True,
                "status": "running",
                "uptime_seconds": 123.45,
                "metrics": {...}
            }
        """
        uptime = (
            (datetime.now() - self.start_time).total_seconds() if self.start_time else 0.0
        )

        return {
            "agent_id": self.agent_id,
            "healthy": self.status == AgentStatus.RUNNING,
            "status": self.status.value,
            "uptime_seconds": uptime,
            "metrics": {
                "events_processed": self.metrics.events_processed,
                "tasks_completed": self.metrics.tasks_completed,
                "errors_encountered": self.metrics.errors_encountered,
            },
        }

    def get_config(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value.

        Args:
            key: Configuration key
            default: Default value if key not found

        Returns:
            Configuration value or default
        """
        return self.config.get(key, default)


class MonitoringAgent(BaseAgent):
    """
    Base class for monitoring agents.

    Monitoring agents observe cluster state and emit events when issues
    are detected.
    """

    def __init__(self, agent_id: str, config: Dict[str, Any]):
        """Initialize monitoring agent."""
        super().__init__(agent_id, config, AgentType.MONITORING)
        self.check_interval = config.get("check_interval", 10)

    async def run(self):
        """Run monitoring loop."""
        while self.running:
            try:
                await self.check()
                await asyncio.sleep(self.check_interval)
            except Exception as e:
                self.logger.error(
                    "Error in monitoring check",
                    exc_info=True,
                    extra={"agent_id": self.agent_id, "error": str(e)},
                )
                self.metrics.errors_encountered += 1

    @abstractmethod
    async def check(self):
        """
        Perform monitoring check.

        This method should be implemented by subclasses to perform
        specific monitoring tasks.
        """
        pass


class SchedulingAgent(BaseAgent):
    """
    Base class for scheduling agents.

    Scheduling agents handle task scheduling and placement decisions.
    """

    def __init__(self, agent_id: str, config: Dict[str, Any]):
        """Initialize scheduling agent."""
        super().__init__(agent_id, config, AgentType.SCHEDULING)

    async def schedule_task(self, task: Dict[str, Any]) -> Optional[str]:
        """
        Schedule a task.

        Args:
            task: Task to schedule

        Returns:
            Node ID where task was scheduled, or None if scheduling failed
        """
        raise NotImplementedError("Subclasses must implement schedule_task")


class RecoveryAgent(BaseAgent):
    """
    Base class for recovery agents.

    Recovery agents handle failure detection and recovery strategies.
    """

    def __init__(self, agent_id: str, config: Dict[str, Any]):
        """Initialize recovery agent."""
        super().__init__(agent_id, config, AgentType.RECOVERY)

    async def recover(self, failure: Dict[str, Any]) -> bool:
        """
        Recover from a failure.

        Args:
            failure: Failure information

        Returns:
            True if recovery was successful, False otherwise
        """
        raise NotImplementedError("Subclasses must implement recover")
