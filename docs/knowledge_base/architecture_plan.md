# Architecture Plan - Knowledge Base

## Overview

This document provides a consolidated summary of the Jarvis cluster management system architecture, extracted from the main design documents for quick reference.

## High-Level Architecture

### System Components

Jarvis consists of several key subsystems that work together to provide cluster management capabilities:

```
┌─────────────────────────────────────────────────────────────┐
│                        Jarvis Cluster                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   API Layer  │  │  Scheduler   │  │   Monitor    │     │
│  │              │  │              │  │              │     │
│  │  - REST API  │  │ - Task Queue │  │ - Heartbeat  │     │
│  │  - Routes    │  │ - Balancer   │  │ - Metrics    │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │    State     │  │    Worker    │  │     DAG      │     │
│  │              │  │              │  │              │     │
│  │ - Registry   │  │ - Executor   │  │ - Manager    │     │
│  │ - Persistence│  │ - Resources  │  │ - Resolver   │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Component Responsibilities

#### 1. API Layer
- **Purpose**: External interface for task submission and cluster management
- **Key Functions**: Accept HTTP requests, validate input, route to appropriate handlers
- **Priority**: P0 (MVP Critical)
- **Files**: `api/server.py`, `api/routes/`

#### 2. Scheduler
- **Purpose**: Intelligent task distribution and workload balancing
- **Key Functions**: Queue management, priority scheduling, load balancing, node selection
- **Priority**: P0 (MVP Core), P1-P2 (Advanced features)
- **Files**: `scheduler/scheduler.py`, `scheduler/task_queue.py`, `scheduler/load_balancer.py`

#### 3. State Manager
- **Purpose**: Centralized state tracking and persistence
- **Key Functions**: Node registry, task state, cluster metadata, persistence layer
- **Priority**: P0 (In-memory), P1 (Persistence)
- **Files**: `state/state_manager.py`, `state/node_registry.py`, `state/persistence.py`

#### 4. Worker
- **Purpose**: Task execution on individual nodes
- **Key Functions**: Execute tasks, monitor resources, report status
- **Priority**: P0 (Basic execution), P1 (Resource monitoring)
- **Files**: `worker/task_executor.py`, `worker/resource_monitor.py`

#### 5. Monitor
- **Purpose**: Health tracking and observability
- **Key Functions**: Heartbeat monitoring, metrics collection, alerting
- **Priority**: P1 (Basic monitoring), P2 (Full observability)
- **Files**: `monitor/heartbeat_monitor.py`, `monitor/metrics_collector.py`

#### 6. DAG Manager
- **Purpose**: Workflow and dependency management
- **Key Functions**: DAG validation, dependency resolution, workflow execution
- **Priority**: P2 (Advanced feature)
- **Files**: `dag/dag_manager.py`, `dag/dag_validator.py`

## Technology Stack

### Core Technologies
- **Language**: Python 3.9+
- **API Framework**: FastAPI
- **Async Runtime**: asyncio
- **State Storage**: Redis (Phase 1), PostgreSQL (Phase 3)
- **Message Queue**: RabbitMQ or Redis Streams

### Supporting Technologies
- **Metrics**: Prometheus + Grafana
- **Logging**: Structured logging with Python logging module
- **Configuration**: YAML-based config files
- **Deployment**: Docker + Kubernetes (later phases)

## Data Flow

### Task Submission Flow
```
1. Client → API (POST /tasks)
2. API → Scheduler (validate & enqueue)
3. Scheduler → Task Queue (priority-based)
4. Scheduler → Worker Selection (load balancing)
5. Worker → Task Execution
6. Worker → State Manager (status updates)
7. State Manager → API (status for client)
```

### Node Health Monitoring Flow
```
1. Worker Node → Heartbeat (periodic ping)
2. Heartbeat Monitor → Validation (check intervals)
3. Monitor → State Manager (update node status)
4. State Manager → Scheduler (node availability)
```

### Workflow (DAG) Execution Flow
```
1. Client → API (POST /workflows with DAG)
2. API → DAG Manager (validate structure)
3. DAG Manager → Dependency Resolver (topological sort)
4. Resolver → Scheduler (submit tasks in order)
5. Scheduler → Workers (execute with dependencies)
6. Workers → DAG Manager (completion tracking)
```

## Design Principles

### 1. Modularity
- Each component is independent with clear interfaces
- Components communicate via well-defined APIs
- Easy to test, maintain, and extend

### 2. Scalability
- Horizontal scaling of worker nodes
- Stateless API layer for load balancing
- Distributed state management

### 3. Reliability
- Fault tolerance through retries and failover
- State persistence for recovery
- Health monitoring and automatic recovery

### 4. Performance
- Asynchronous operations where possible
- Efficient queue management
- Resource-aware scheduling

### 5. Observability
- Comprehensive logging
- Metrics collection at all levels
- Distributed tracing support

## Development Phases Summary

### Phase 0: Foundation (Current)
- Repository setup
- Design documentation
- Development tools

### Phase 1: MVP - Single Node (Weeks 3-5)
**Goal**: Basic task submission and execution on one node
- Core API endpoints
- Simple FIFO task queue
- Single worker executor
- In-memory state

### Phase 2: Multi-Node Support (Weeks 6-8)
**Goal**: Distribute tasks across multiple workers
- Node registration and discovery
- Load balancing
- Basic health monitoring

### Phase 3: State Persistence (Weeks 9-11)
**Goal**: Survive restarts and failures
- Database integration
- State recovery
- Task history

### Phase 4: Advanced Scheduling (Weeks 12-14)
**Goal**: Intelligent task distribution
- Priority queues
- Resource-based scheduling
- Fair scheduling policies

### Phase 5: Observability (Weeks 15-18)
**Goal**: Full monitoring and metrics
- Prometheus integration
- Grafana dashboards
- Alerting system

### Phase 6-9: Production Readiness
- High availability
- Security hardening
- Performance optimization
- Advanced features (autoscaling, DAGs, etc.)

## Key Architectural Decisions

### ADR-0001: Use Python for Implementation
**Context**: Need a language for rapid development with good library support  
**Decision**: Python 3.9+ with type hints  
**Rationale**: Fast development, rich ecosystem, async support, strong for data processing

### ADR-0002: Use FastAPI for API Layer
**Context**: Need modern, fast API framework  
**Decision**: FastAPI with Pydantic validation  
**Rationale**: Async support, automatic docs, type safety, high performance

### ADR-0003: Redis for Initial State Storage
**Context**: Need fast state storage for MVP  
**Decision**: Redis for Phase 1-2, migrate to PostgreSQL in Phase 3  
**Rationale**: Simple setup, fast in-memory, good for prototyping

### ADR-0004: Priority-Based Development
**Context**: Need to deliver value incrementally  
**Decision**: P0→P1→P2→P3 priority system  
**Rationale**: Focus on MVP first, add features incrementally

## File Organization

The complete file structure is documented in [JARVIS_FILE_TREE.md](../../JARVIS_FILE_TREE.md). Key directories:

```
jarvis/
├── api/              # API layer (P0)
├── scheduler/        # Task scheduling (P0-P2)
├── state/            # State management (P0-P1)
├── worker/           # Task execution (P0-P1)
├── monitor/          # Health & metrics (P1-P2)
├── dag/              # Workflow management (P2)
├── utils/            # Shared utilities (P0)
└── config/           # Configuration (P0)
```

## Integration Points

### External Systems
- **Redis**: State storage and pub/sub
- **PostgreSQL**: Persistent storage (Phase 3+)
- **Prometheus**: Metrics collection
- **Grafana**: Visualization
- **Docker**: Containerization
- **Kubernetes**: Orchestration (Phase 8+)

### Internal APIs
- **Scheduler API**: Task submission, status queries
- **State API**: State reads/writes, node registry
- **Worker API**: Task execution, resource reporting
- **Monitor API**: Health checks, metrics

## Security Considerations

### Phase 7+: Security Hardening
- Authentication and authorization
- API rate limiting
- Input validation and sanitization
- Secure communication (TLS)
- Secrets management
- Audit logging

## Performance Targets

### MVP (Phase 1)
- Handle 10 concurrent tasks
- Sub-second task submission
- Single node deployment

### Production (Phase 8+)
- Handle 1000+ concurrent tasks
- <100ms API response time
- 100+ worker nodes
- 99.9% uptime

## Monitoring and Metrics

### Key Metrics
- **Task Metrics**: Submission rate, completion rate, failure rate, queue length
- **Worker Metrics**: CPU usage, memory usage, task execution time, availability
- **System Metrics**: API latency, scheduler latency, state sync time
- **Business Metrics**: SLA compliance, resource utilization, cost efficiency

### Health Checks
- API endpoint health
- Scheduler queue health
- Worker node health
- Database connection health
- Redis connection health

## Disaster Recovery

### Backup Strategy (Phase 3+)
- Regular state backups
- Transaction logs
- Point-in-time recovery
- Cross-region replication (Phase 8+)

### Failure Scenarios
- **Single worker failure**: Task requeue and retry
- **Scheduler failure**: Standby scheduler promotion
- **Database failure**: Switch to replica
- **Network partition**: Graceful degradation

## Future Enhancements

### Phase 9+ Potential Features
- Multi-tenancy support
- Autoscaling based on load
- Machine learning for task optimization
- Cross-cluster task scheduling
- Advanced DAG features (loops, conditionals)
- Cost optimization algorithms

## References

For more detailed information, refer to:
- [DESIGN_PLAN.md](../../DESIGN_PLAN.md) - Complete architecture documentation
- [USE_CASES.md](../../USE_CASES.md) - Concrete usage examples
- [JARVIS_FILE_TREE.md](../../JARVIS_FILE_TREE.md) - Complete file structure
- [REQUIREMENTS.md](../../REQUIREMENTS.md) - Technical requirements
- [ROADMAP.md](../../ROADMAP.md) - Development timeline
- [docs/decisions/](../decisions/) - Architectural Decision Records

---

**Last Updated**: 2026-01-08  
**Architecture Version**: 1.0  
**Status**: Phase 0 - Foundation
