"""
Monitoring Agent Template for Jarvis

Use this template for creating monitoring agents that periodically check
system state and emit events when issues are detected.

Instructions:
1. Copy this file and rename it
2. Replace MyMonitoringAgent with your agent name
3. Implement the check() method with your monitoring logic
4. Define thresholds and conditions in config
5. Emit events when issues are detected
"""

import asyncio
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.base_agent import Event, MonitoringAgent


class MyMonitoringAgent(MonitoringAgent):
    """
    [MONITORING AGENT NAME]

    Brief description of what this agent monitors.

    This agent monitors:
    - [Resource/Metric 1]
    - [Resource/Metric 2]
    - [Resource/Metric 3]

    Emits events:
    - [event_type_1]: When [condition]
    - [event_type_2]: When [condition]

    Configuration:
        check_interval: int - Seconds between checks
        [threshold_name]: value - Threshold for alerts
    """

    def __init__(self, agent_id: str, config: Dict[str, Any]):
        """
        Initialize the monitoring agent.

        Args:
            agent_id: Unique identifier for this agent
            config: Agent configuration dictionary
        """
        super().__init__(agent_id, config)

        # Configuration
        self.warning_threshold = config.get("warning_threshold", 70)
        self.critical_threshold = config.get("critical_threshold", 90)

        # State
        self.last_check_time: datetime = None
        self.alerts_sent: List[str] = []

        self.logger.info(
            "Monitoring agent initialized",
            extra={
                "agent_id": self.agent_id,
                "check_interval": self.check_interval,
                "warning_threshold": self.warning_threshold,
                "critical_threshold": self.critical_threshold,
            },
        )

    async def check(self):
        """
        Perform monitoring check.

        Implement your monitoring logic here. This method is called
        periodically based on check_interval.
        """
        self.logger.debug("Performing monitoring check", extra={"agent_id": self.agent_id})

        self.last_check_time = datetime.now()

        try:
            # Collect metrics
            metrics = await self._collect_metrics()

            # Check thresholds
            await self._check_thresholds(metrics)

        except Exception as e:
            self.logger.error(
                "Error during monitoring check",
                exc_info=True,
                extra={"agent_id": self.agent_id, "error": str(e)},
            )
            self.metrics.errors_encountered += 1

    async def _collect_metrics(self) -> Dict[str, Any]:
        """
        Collect metrics to monitor.

        Returns:
            Dictionary of metrics

        Example:
            {
                "cpu_usage": 75.5,
                "memory_usage": 82.3,
                "disk_usage": 60.0
            }
        """
        # Implement metric collection here
        # This is where you'd query system state, APIs, etc.

        metrics = {
            "example_metric": 50.0,  # Replace with actual metrics
        }

        self.logger.debug(
            "Metrics collected",
            extra={"agent_id": self.agent_id, "metrics": metrics},
        )

        return metrics

    async def _check_thresholds(self, metrics: Dict[str, Any]):
        """
        Check if metrics exceed thresholds.

        Args:
            metrics: Collected metrics
        """
        for metric_name, value in metrics.items():
            # Check critical threshold
            if value >= self.critical_threshold:
                await self._emit_critical_alert(metric_name, value)

            # Check warning threshold
            elif value >= self.warning_threshold:
                await self._emit_warning_alert(metric_name, value)

    async def _emit_warning_alert(self, metric_name: str, value: float):
        """
        Emit a warning alert event.

        Args:
            metric_name: Name of the metric
            value: Current value
        """
        event = Event(
            event_type="monitoring_warning",
            source=self.agent_id,
            data={
                "metric": metric_name,
                "value": value,
                "threshold": self.warning_threshold,
                "severity": "warning",
            },
            timestamp=datetime.now(),
        )

        self.logger.warning(
            "Warning threshold exceeded",
            extra={
                "agent_id": self.agent_id,
                "metric": metric_name,
                "value": value,
                "threshold": self.warning_threshold,
            },
        )

        # In a real implementation, this would publish to event bus
        self.alerts_sent.append(event.event_type)

    async def _emit_critical_alert(self, metric_name: str, value: float):
        """
        Emit a critical alert event.

        Args:
            metric_name: Name of the metric
            value: Current value
        """
        event = Event(
            event_type="monitoring_critical",
            source=self.agent_id,
            data={
                "metric": metric_name,
                "value": value,
                "threshold": self.critical_threshold,
                "severity": "critical",
            },
            timestamp=datetime.now(),
        )

        self.logger.error(
            "Critical threshold exceeded",
            extra={
                "agent_id": self.agent_id,
                "metric": metric_name,
                "value": value,
                "threshold": self.critical_threshold,
            },
        )

        # In a real implementation, this would publish to event bus
        self.alerts_sent.append(event.event_type)


# Example usage
async def main():
    """Example of using the monitoring agent."""
    # Configure the agent
    config = {
        "check_interval": 2,
        "warning_threshold": 70,
        "critical_threshold": 90,
    }

    # Create agent
    agent = MyMonitoringAgent("monitor-1", config)

    # Start agent
    await agent.start()

    # Let it run for a bit
    await asyncio.sleep(10)

    # Stop agent
    await agent.stop()

    # Check results
    health = await agent.health_check()
    print(f"Agent health: {health}")
    print(f"Alerts sent: {len(agent.alerts_sent)}")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    asyncio.run(main())
