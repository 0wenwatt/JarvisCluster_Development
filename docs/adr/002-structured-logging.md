# 2. Structured Logging with Correlation IDs

Date: 2026-01-08

## Status

Accepted

## Context

In a distributed system like Jarvis with multiple agents and components running across different nodes, traditional logging approaches have limitations:

- **Unstructured logs**: Difficult to parse and analyze programmatically
- **Lost context**: Hard to trace requests across components
- **Debugging difficulty**: Cannot correlate events across the system
- **Analysis challenges**: Text-based logs require complex regex for querying
- **Performance impact**: String formatting happens even when logs aren't used

Requirements:
- Trace requests through the entire system
- Correlate events across multiple agents
- Enable programmatic log analysis
- Support log aggregation systems (ELK, Loki)
- Minimal performance overhead
- Sensitive data protection

## Decision

We will implement **structured logging with correlation IDs**:

1. **Structured Logging**:
   - Use JSON format for all logs
   - Include context as structured fields, not in message strings
   - Use logging extras for additional data
   - Separate message from metadata

2. **Correlation IDs**:
   - Generate UUID for each request/operation
   - Propagate through all components
   - Store in context variables (Python contextvars)
   - Include in all log entries
   - Pass in API headers (X-Correlation-ID)

3. **Implementation**:
   - Custom logging filters for correlation ID injection
   - Structured logger wrapper class
   - Configuration templates for different environments
   - Sensitive data filtering

4. **Log Levels**:
   - DEBUG: Detailed diagnostic information
   - INFO: General informational messages
   - WARNING: Warning messages, recoverable issues
   - ERROR: Error messages, operation failed
   - CRITICAL: Critical issues, system unusable

## Consequences

### Positive

- **Traceability**: Can follow a request through the entire system
- **Queryability**: Can query logs programmatically with JSON tools
- **Analysis**: Easy integration with log aggregation systems
- **Debugging**: Correlation IDs make debugging distributed systems easier
- **Performance**: Lazy evaluation with % formatting reduces overhead
- **Context preservation**: No loss of context information
- **Machine-readable**: Automated alerting and analysis

### Negative

- **Storage overhead**: JSON logs are larger than plain text
- **Human readability**: JSON is harder to read for humans
- **Learning curve**: Team needs to learn structured logging patterns
- **Configuration complexity**: More configuration than basic logging
- **Tool requirements**: Need JSON-capable log viewers

### Neutral

- **Log rotation**: Still needed, same as before
- **Log retention**: Same policies apply
- **Development vs. production**: Different formats for different environments

## Alternatives Considered

### Alternative 1: Plain Text Logging

**Description**: Traditional string-based logging with printf-style formatting

**Pros**:
- Simple to implement
- Easy to read
- Familiar to all developers
- Small log files

**Cons**:
- Difficult to parse programmatically
- No structured context
- Cannot trace across system
- Regex required for analysis
- Lost type information

**Why not chosen**: Doesn't meet requirements for distributed tracing and analysis

### Alternative 2: OpenTelemetry Traces Only

**Description**: Use OpenTelemetry for all observability, no separate logging

**Pros**:
- Industry standard
- Rich tooling ecosystem
- Built-in distributed tracing
- Powerful querying

**Cons**:
- Additional infrastructure required (Jaeger, Zipkin)
- Steeper learning curve
- May be overkill for initial deployment
- Not all information fits trace model
- Higher operational complexity

**Why not chosen**: Good for future, but structured logging provides 80% of benefits with less complexity

### Alternative 3: Log Everything to Database

**Description**: Write all logs directly to a database (PostgreSQL, etc.)

**Pros**:
- Easy to query with SQL
- No need for log aggregation
- Built-in indexing
- ACID guarantees

**Cons**:
- Database becomes bottleneck
- Expensive at scale
- Difficult to rotate/archive
- Not designed for high-throughput logging
- Database failure affects logging

**Why not chosen**: Databases are not optimized for logging workload

## Implementation

Implementation plan:

1. **Week 1: Core Utilities**
   - Create logging_utils.py with correlation ID support
   - Implement CorrelationIdFilter
   - Create SensitiveDataFilter
   - Add StructuredLogger wrapper

2. **Week 2: Configuration**
   - Create logging configuration templates
   - Development config (colorized console)
   - Production config (JSON to file)
   - Testing config

3. **Week 3: Integration**
   - Update all components to use structured logging
   - Add correlation ID propagation
   - Update API to handle X-Correlation-ID header
   - Add examples and documentation

4. **Week 4: Validation**
   - Test with log aggregation system
   - Performance benchmarking
   - Documentation review
   - Team training

**Dependencies**:
- python-json-logger package
- PyYAML for configuration
- contextvars for correlation ID storage

## Validation

Success will be measured by:

- **Traceability**: 100% of requests traceable via correlation ID
- **Query time**: Find logs for correlation ID in < 1 second
- **Performance**: < 5% overhead compared to standard logging
- **Adoption**: All components using structured logging within 1 month
- **Debugging time**: 50% reduction in time to debug distributed issues

Metrics to track:
- Average time to find related logs
- Number of correlation ID propagation failures
- Log volume and storage costs
- Team satisfaction with logging

## References

- [config/logging/README.md](../../config/logging/README.md) - Logging configuration guide
- [src/utilities/logging_utils.py](../../src/utilities/logging_utils.py) - Logging utilities
- [The Twelve-Factor App: Logs](https://12factor.net/logs)
- [Structured Logging Best Practices](https://www.loggly.com/ultimate-guide/python-logging-basics/)
- [Python Logging Documentation](https://docs.python.org/3/library/logging.html)
