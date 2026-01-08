# Agent Configuration for Jarvis

This directory contains configuration files for Jarvis agents.

## Overview

Agent configurations define:
- Which agents to run
- Agent-specific settings
- Resource limits
- Monitoring intervals
- Event subscriptions

## Configuration Files

### `agents.yaml`

Main configuration file that defines all agents in the system:

```yaml
agents:
  health_monitor:
    enabled: true
    type: monitoring
    config:
      check_interval: 5
      heartbeat_timeout: 30
      failure_threshold: 3

  task_scheduler:
    enabled: true
    type: scheduling
    config:
      schedule_interval: 1
      max_queue_size: 1000
```

### Environment-Specific Configs

- `development.yaml`: Development environment
- `production.yaml`: Production environment
- `testing.yaml`: Testing environment

## Configuration Schema

### Agent Definition

```yaml
agent_name:
  enabled: bool              # Whether to start this agent
  type: string               # Agent type (monitoring, scheduling, etc.)
  config:                    # Agent-specific configuration
    key: value
```

### Common Configuration Options

All agents support these options:

```yaml
config:
  check_interval: int        # Seconds between checks (monitoring agents)
  log_level: string          # Log level (DEBUG, INFO, WARNING, ERROR)
  max_retries: int           # Maximum retry attempts
  retry_backoff: int         # Retry backoff in seconds
```

## Agent Types

### Monitoring Agents

Monitor cluster health and resources:

```yaml
health_monitor:
  enabled: true
  type: monitoring
  config:
    check_interval: 5        # Check every 5 seconds
    heartbeat_timeout: 30    # Node timeout in seconds
    failure_threshold: 3     # Failures before marking node down
```

### Scheduling Agents

Handle task scheduling:

```yaml
task_scheduler:
  enabled: true
  type: scheduling
  config:
    schedule_interval: 1     # Schedule tasks every second
    max_queue_size: 1000     # Maximum pending tasks
    algorithm: "best_fit"    # Scheduling algorithm
```

### Recovery Agents

Handle failure recovery:

```yaml
recovery_agent:
  enabled: true
  type: recovery
  config:
    recovery_timeout: 60     # Timeout for recovery attempts
    max_recovery_attempts: 3 # Maximum recovery attempts
    reschedule_delay: 5      # Delay before rescheduling
```

## Loading Configuration

### Python

```python
import yaml
from pathlib import Path

def load_agent_config(env: str = "development") -> dict:
    config_file = Path(f"config/agents/{env}.yaml")
    with open(config_file) as f:
        return yaml.safe_load(f)

config = load_agent_config("production")
```

### Creating Agents from Config

```python
from agent_manager import AgentManager

manager = AgentManager()
config = load_agent_config()

for agent_id, agent_config in config["agents"].items():
    if agent_config.get("enabled", True):
        await manager.create_agent(
            agent_id=agent_id,
            agent_type=agent_config["type"],
            config=agent_config["config"]
        )
```

## Validation

Validate configuration before loading:

```bash
# Using yamllint
yamllint config/agents/*.yaml

# Using custom validator
python scripts/validate_agent_config.py config/agents/production.yaml
```

## Best Practices

1. **Use Environment Variables**: For secrets and environment-specific values
2. **Version Control**: Commit default configs, exclude sensitive data
3. **Documentation**: Document all config options
4. **Validation**: Validate configs before deployment
5. **Defaults**: Provide sensible defaults for all options

## Examples

See example configurations:
- `examples/health_monitor.yaml`: Health monitoring
- `examples/task_scheduler.yaml`: Task scheduling
- `examples/recovery.yaml`: Failure recovery

## Related Documentation

- [src/agents/README.md](../../src/agents/README.md) - Agent framework
- [REQUIREMENTS.md](../../REQUIREMENTS.md) - Configuration requirements
