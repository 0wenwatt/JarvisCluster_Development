# Logging Configuration for JarvisCluster_Development

This directory contains logging configuration templates and examples for the Jarvis cluster management system.

## Overview

Proper logging is critical for:
- Debugging issues in distributed systems
- Performance monitoring and analysis
- Audit trails and compliance
- Incident response and troubleshooting

## Configuration Files

### `logging_config.yaml`

Standard logging configuration using Python's logging module format. Includes:
- Multiple handlers (console, file, rotating file)
- Different log levels per component
- Structured JSON logging format
- Correlation ID support for distributed tracing

### `development.yaml`

Development environment logging configuration:
- Debug level logging
- Console output with colors
- Detailed stack traces
- SQL query logging (if applicable)

### `production.yaml`

Production environment logging configuration:
- Info level logging (Warning/Error for most modules)
- File output with rotation
- Structured JSON format for log aggregation
- Sensitive data filtering

## Log Levels

Follow these guidelines for log levels:

| Level | When to Use | Example |
|-------|-------------|---------|
| **DEBUG** | Detailed diagnostic information | Variable values, function entry/exit |
| **INFO** | General informational messages | Task scheduled, node registered |
| **WARNING** | Warning messages, recoverable issues | High memory usage, slow response |
| **ERROR** | Error messages, operation failed | Failed to connect to database |
| **CRITICAL** | Critical issues, system unusable | System out of memory, data corruption |

## Best Practices

### 1. Use Structured Logging

```python
# Good: Structured with context
logger.info(
    "Task scheduled successfully",
    extra={
        "task_id": task.id,
        "node_id": node.id,
        "priority": task.priority,
        "duration_ms": duration
    }
)

# Bad: Unstructured string interpolation
logger.info(f"Task {task.id} scheduled on {node.id}")
```

### 2. Include Context

Always include relevant context:
- Request/correlation IDs for distributed tracing
- User IDs for audit trails
- Resource IDs (task, node, cluster)
- Timing information (duration, timestamp)

### 3. Don't Log Sensitive Data

Never log:
- Passwords or secrets
- API keys or tokens
- Personal identifiable information (PII)
- Credit card numbers
- Full connection strings with credentials

### 4. Use Appropriate Log Levels

```python
# DEBUG: Detailed diagnostic info
logger.debug("Processing task queue", extra={"queue_size": len(queue)})

# INFO: Normal operations
logger.info("Node registered", extra={"node_id": node_id})

# WARNING: Potential issues
logger.warning("High queue depth detected", extra={"depth": len(queue)})

# ERROR: Operation failed
logger.error("Failed to execute task", exc_info=True, extra={"task_id": task_id})

# CRITICAL: System-level failure
logger.critical("State store unreachable", extra={"attempts": retry_count})
```

### 5. Log at Boundaries

Log at system boundaries:
- API requests and responses
- Message queue operations
- Database queries
- External service calls
- Component lifecycle events (start/stop)

## Correlation IDs

Use correlation IDs to trace requests through distributed systems:

```python
import uuid
from contextvars import ContextVar

correlation_id: ContextVar[str] = ContextVar('correlation_id')

def set_correlation_id(cid: str = None):
    """Set correlation ID for current context."""
    if cid is None:
        cid = str(uuid.uuid4())
    correlation_id.set(cid)
    return cid

def get_correlation_id() -> str:
    """Get correlation ID for current context."""
    return correlation_id.get(None)
```

## Log Rotation

Configure log rotation to prevent disk space issues:

```yaml
handlers:
  rotating_file:
    class: logging.handlers.RotatingFileHandler
    filename: logs/jarvis.log
    maxBytes: 10485760  # 10MB
    backupCount: 10
    formatter: json
```

## Integration with ELK/Loki

For production deployments, integrate with log aggregation systems:

### Elasticsearch + Logstash + Kibana (ELK)

```yaml
handlers:
  logstash:
    class: logstash.TCPLogstashHandler
    host: logstash.example.com
    port: 5000
    version: 1
```

### Grafana Loki

```yaml
handlers:
  loki:
    class: logging_loki.LokiHandler
    url: http://loki.example.com:3100/loki/api/v1/push
    tags: {"application": "jarvis", "environment": "production"}
```

## Testing Logging

Test that logging works correctly:

```python
def test_logging_includes_task_id(caplog):
    """Test that task operations log task ID."""
    with caplog.at_level(logging.INFO):
        scheduler.schedule_task(task_id="task-123")

    assert "task-123" in caplog.text
    assert any(record.task_id == "task-123" for record in caplog.records)
```

## Performance Considerations

### 1. Lazy Formatting

```python
# Good: Lazy formatting (only evaluated if logged)
logger.debug("Task details: %s", expensive_function())

# Bad: Eager formatting (always evaluated)
logger.debug(f"Task details: {expensive_function()}")
```

### 2. Avoid Excessive Logging

```python
# Bad: Logging in tight loops
for item in large_list:
    logger.debug(f"Processing item {item}")  # Don't do this!

# Good: Log summary
logger.debug(f"Processing {len(large_list)} items")
# ... process items ...
logger.debug(f"Completed processing {len(large_list)} items")
```

### 3. Asynchronous Logging

For high-throughput systems, use asynchronous logging:

```yaml
handlers:
  async_file:
    class: logging.handlers.QueueHandler
    queue: !QueueListener
      handlers:
        - !FileHandler
          filename: logs/jarvis.log
```

## Monitoring Logs

Set up alerts for important log patterns:

```yaml
# Example Prometheus Alertmanager rule
- alert: HighErrorRate
  expr: rate(log_messages_total{level="error"}[5m]) > 10
  annotations:
    summary: High error rate in logs
```

## Related Documents

- [REQUIREMENTS.md](../../REQUIREMENTS.md) - Observability requirements
- [DESIGN_PLAN.md](../../DESIGN_PLAN.md) - Logging architecture
