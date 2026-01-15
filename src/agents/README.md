# Agent Framework for Jarvis

This directory contains the agent framework for the Jarvis cluster management system. Agents are autonomous components that handle specific responsibilities within the cluster.

## Overview

The Jarvis agent framework provides a flexible, extensible architecture for building intelligent agents that:
- Monitor cluster state
- Make autonomous decisions
- Execute tasks and workflows
- Respond to events
- Coordinate with other agents

## Agent Types

### 1. Monitoring Agents
Monitor cluster health, resources, and performance:
- **Health Monitor Agent**: Tracks node health and heartbeats
- **Resource Monitor Agent**: Monitors CPU, memory, disk, network usage
- **Performance Monitor Agent**: Analyzes performance metrics and trends

### 2. Scheduling Agents
Handle task scheduling and placement:
- **Task Scheduler Agent**: Assigns tasks to nodes
- **Load Balancer Agent**: Balances workload across nodes
- **Priority Manager Agent**: Manages task priorities

### 3. Recovery Agents
Handle failures and recovery:
- **Failure Detection Agent**: Detects node and task failures
- **Recovery Agent**: Implements recovery strategies
- **Backup Agent**: Manages backups and snapshots

### 4. Optimization Agents
Optimize cluster performance:
- **Resource Optimizer Agent**: Optimizes resource allocation
- **Cost Optimizer Agent**: Minimizes operational costs
- **Performance Tuner Agent**: Tunes system parameters

### 5. Security Agents
Manage security and compliance:
- **Security Monitor Agent**: Monitors for security threats
- **Compliance Agent**: Ensures compliance with policies
- **Audit Agent**: Maintains audit trails

## Architecture

### Base Agent Class

All agents inherit from `BaseAgent`:

```python
class BaseAgent:
    """Base class for all Jarvis agents."""

    def __init__(self, agent_id: str, config: Dict):
        self.agent_id = agent_id
        self.config = config
        self.logger = get_logger(f"jarvis.agent.{agent_id}")

    async def start(self):
        """Start the agent."""
        pass

    async def stop(self):
        """Stop the agent gracefully."""
        pass

    async def run(self):
        """Main agent loop."""
        pass

    async def handle_event(self, event: Event):
        """Handle an event."""
        pass
```

### Agent Lifecycle

1. **Initialization**: Agent is created with configuration
2. **Start**: Agent starts and initializes resources
3. **Run**: Agent enters main loop, processing events and executing logic
4. **Stop**: Agent stops gracefully, cleaning up resources

### Agent Communication

Agents communicate through:
- **Event Bus**: Publish-subscribe event system
- **State Store**: Shared state repository
- **Message Queue**: Asynchronous message passing
- **Direct API Calls**: Synchronous communication

### Agent Configuration

Agents are configured via YAML files:

```yaml
agents:
  health_monitor:
    enabled: true
    type: monitoring
    interval: 5s
    config:
      heartbeat_timeout: 30s
      failure_threshold: 3
```

## Creating a New Agent

### 1. Extend BaseAgent

```python
from base_agent import BaseAgent

class MyCustomAgent(BaseAgent):
    """Custom agent implementation."""

    async def run(self):
        """Main agent logic."""
        while self.running:
            # Agent logic here
            await asyncio.sleep(self.config.get("interval", 10))
```

### 2. Implement Required Methods

- `start()`: Initialize resources
- `run()`: Main loop logic
- `stop()`: Cleanup
- `handle_event()`: Event handling (optional)

### 3. Add Configuration

Create `config/agents/my_custom_agent.yaml`:

```yaml
agent_id: my_custom_agent
type: custom
enabled: true
interval: 10s
config:
  # Custom configuration
  threshold: 80
```

### 4. Register Agent

Register in agent manager:

```python
agent_manager.register_agent_type("custom", MyCustomAgent)
agent_manager.create_agent("my_custom_agent", config)
```

## Agent Development Guidelines

### 1. Single Responsibility

Each agent should have a single, well-defined responsibility:
- ✅ Good: `HealthMonitorAgent` monitors node health
- ❌ Bad: `SuperAgent` monitors health, schedules tasks, and optimizes resources

### 2. Stateless When Possible

Agents should be stateless or store state in shared state store:
- Enables horizontal scaling
- Simplifies recovery
- Reduces complexity

### 3. Handle Failures Gracefully

Agents should:
- Catch and log exceptions
- Implement retry logic
- Fail gracefully without crashing

### 4. Use Structured Logging

Log with context for debugging:

```python
self.logger.info(
    "Task scheduled",
    extra={"task_id": task.id, "node_id": node.id}
)
```

### 5. Implement Health Checks

Provide health check endpoint:

```python
async def health_check(self) -> bool:
    """Return True if agent is healthy."""
    return self.running and self._is_healthy()
```

### 6. Respect Configuration

Use configuration for tuneable parameters:

```python
interval = self.config.get("check_interval", 10)
threshold = self.config.get("threshold", 80)
```

### 7. Emit Metrics

Emit metrics for monitoring:

```python
metrics.gauge("agent.tasks.active", len(self.active_tasks))
metrics.counter("agent.events.processed", 1)
```

## Testing Agents

### Unit Tests

Test agent logic in isolation:

```python
def test_health_monitor_detects_failure():
    agent = HealthMonitorAgent(config)
    node = MockNode(heartbeat_timeout=True)

    result = agent.check_node_health(node)

    assert result.status == "unhealthy"
```

### Integration Tests

Test agent interactions:

```python
async def test_agent_communication():
    event_bus = EventBus()
    agent1 = MonitorAgent(event_bus)
    agent2 = RecoveryAgent(event_bus)

    await agent1.start()
    await agent2.start()

    # Test event propagation
    await agent1.emit_event("node_failure", {"node_id": "node-1"})
    await asyncio.sleep(0.1)

    assert agent2.handled_events == 1
```

## Agent Patterns

### 1. Observer Pattern

Agent observes state and reacts:

```python
async def run(self):
    while self.running:
        state = await self.state_store.get_cluster_state()
        if self._detect_issue(state):
            await self._handle_issue()
        await asyncio.sleep(self.interval)
```

### 2. Event-Driven Pattern

Agent reacts to events:

```python
async def handle_event(self, event: Event):
    if event.type == "node_failure":
        await self._handle_node_failure(event.data)
    elif event.type == "task_complete":
        await self._handle_task_complete(event.data)
```

### 3. Producer-Consumer Pattern

Agent produces or consumes from queue:

```python
async def run(self):
    while self.running:
        task = await self.task_queue.get()
        await self._process_task(task)
```

### 4. Coordinator Pattern

Agent coordinates multiple agents:

```python
async def coordinate(self):
    results = await asyncio.gather(
        self.agent1.execute(),
        self.agent2.execute(),
        self.agent3.execute()
    )
    return self._aggregate_results(results)
```

## Examples

See `src/examples/agents/` for complete examples:
- `monitoring_agent_example.py`: Health monitoring
- `scheduler_agent_example.py`: Task scheduling
- `recovery_agent_example.py`: Failure recovery

## Templates

Use templates in `src/templates/agents/` to create new agents:
- `base_agent_template.py`: Basic agent structure
- `monitoring_agent_template.py`: Monitoring agent
- `event_driven_agent_template.py`: Event-driven agent

## Related Documentation

- [DESIGN_PLAN.md](../../DESIGN_PLAN.md) - System architecture
- [REQUIREMENTS.md](../../REQUIREMENTS.md) - Coding standards
- [config/agents/README.md](../../config/agents/README.md) - Agent configuration
