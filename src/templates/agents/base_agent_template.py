"""
Basic Agent Template for Jarvis

Use this template as a starting point for creating new agents.

Instructions:
1. Copy this file and rename it
2. Replace MyAgent with your agent name
3. Implement the run() method with your agent logic
4. Add any additional methods needed
5. Update the docstrings

Example:
    class DataProcessorAgent(BaseAgent):
        async def run(self):
            while self.running:
                data = await self.fetch_data()
                await self.process_data(data)
                await asyncio.sleep(self.config.get("interval", 10))
"""

import asyncio
import logging
import sys
from pathlib import Path
from typing import Any, Dict

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.base_agent import BaseAgent, Event


class MyAgent(BaseAgent):
    """
    [AGENT NAME] Agent

    Brief description of what this agent does.

    This agent:
    - [Responsibility 1]
    - [Responsibility 2]
    - [Responsibility 3]

    Configuration:
        interval: int - Seconds between operations
        [other_config]: type - Description
    """

    def __init__(self, agent_id: str, config: Dict[str, Any]):
        """
        Initialize the agent.

        Args:
            agent_id: Unique identifier for this agent
            config: Agent configuration dictionary
        """
        super().__init__(agent_id, config)

        # Configuration
        self.interval = config.get("interval", 10)

        # State
        # Add any state variables your agent needs

        self.logger.info(
            "MyAgent initialized",
            extra={"agent_id": self.agent_id, "interval": self.interval},
        )

    async def start(self):
        """
        Start the agent.

        Override this method if you need custom initialization logic.
        Make sure to call super().start().
        """
        # Custom initialization here
        # ...

        # Call parent start
        await super().start()

    async def stop(self):
        """
        Stop the agent.

        Override this method if you need custom cleanup logic.
        Make sure to call super().stop().
        """
        # Custom cleanup here
        # ...

        # Call parent stop
        await super().stop()

    async def run(self):
        """
        Main agent loop.

        Implement your agent's main logic here. This method runs continuously
        while self.running is True.
        """
        while self.running:
            try:
                # Main agent logic here
                await self._do_work()

                # Wait before next iteration
                await asyncio.sleep(self.interval)

            except Exception as e:
                self.logger.error(
                    "Error in agent loop",
                    exc_info=True,
                    extra={"agent_id": self.agent_id, "error": str(e)},
                )
                self.metrics.errors_encountered += 1

    async def _do_work(self):
        """
        Perform agent work.

        This is a helper method to keep the run() method clean.
        Implement your agent's main logic here.
        """
        self.logger.debug("Performing work", extra={"agent_id": self.agent_id})

        # Your agent logic here
        # ...

        self.metrics.tasks_completed += 1

    async def handle_event(self, event: Event):
        """
        Handle an event.

        Override this method if your agent needs to respond to events.

        Args:
            event: Event to handle
        """
        await super().handle_event(event)

        # Handle specific event types
        if event.event_type == "example_event":
            await self._handle_example_event(event)

    async def _handle_example_event(self, event: Event):
        """Handle example event."""
        self.logger.info(
            "Handling example event",
            extra={"agent_id": self.agent_id, "event_data": event.data},
        )

        # Event handling logic here
        # ...


# Example usage
async def main():
    """Example of using the agent."""
    # Configure the agent
    config = {
        "interval": 5,
        # Add your configuration here
    }

    # Create agent
    agent = MyAgent("my-agent-1", config)

    # Start agent
    await agent.start()

    # Let it run for a bit
    await asyncio.sleep(15)

    # Stop agent
    await agent.stop()

    # Check health
    health = await agent.health_check()
    print(f"Agent health: {health}")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    asyncio.run(main())
