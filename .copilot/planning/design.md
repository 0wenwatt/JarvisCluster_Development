# Design & Architecture

**Parent**: [Planning Index](index.md)  
**Level**: 3 (Topic Detail)

---

## 📋 Summary

This document provides a summary of Jarvis system architecture, component design, and technical decisions. It consolidates information from DESIGN_PLAN.md and related architectural documents.

---

## 🏗️ System Architecture

### High-Level Overview

Jarvis is a cluster management system with a distributed architecture:

```
┌─────────────────────────────────────────────────────────────┐
│                     Control Plane                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Scheduler  │  │  Orchestrator│  │    Monitor   │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                            │
                ┌───────────┴───────────┐
                │                       │
┌───────────────▼──────────┐  ┌────────▼──────────────┐
│      Worker Nodes        │  │    Data Layer         │
│  ┌──────┐  ┌──────┐     │  │  ┌──────┐  ┌──────┐  │
│  │ Node │  │ Node │ ... │  │  │ State│  │ Logs │  │
│  └──────┘  └──────┘     │  │  └──────┘  └──────┘  │
└──────────────────────────┘  └─────────────────────┘
```

---

## 🧩 Core Components

### 1. API Layer
**Purpose**: External interface for cluster interaction  
**Priority**: P0 (MVP Critical)  
**Technology**: FastAPI (Python)

**Responsibilities**:
- Accept and validate HTTP requests
- Route requests to appropriate handlers
- Return formatted responses
- Handle authentication (P2)
- Rate limiting (P2)

**Key Endpoints**:
- `POST /tasks` - Submit task
- `GET /tasks/{id}` - Get task status
- `GET /health` - Health check
- `GET /nodes` - List worker nodes (P1)

**Location in Implementation**: `jarvis/api/`

---

### 2. Scheduler
**Purpose**: Intelligent task distribution and workload balancing  
**Priority**: P0 (basic), P1-P2 (advanced)  
**Technology**: Python with asyncio

**Responsibilities**:
- Maintain task queue (FIFO initially, priority later)
- Match tasks to available worker nodes
- Load balancing across nodes
- Handle scheduling policies
- Retry failed tasks

**Key Algorithms**:
- Resource matching (P0): Find nodes with sufficient resources
- Load balancing (P1): Round-robin, least-loaded
- Priority scheduling (P2): Priority queue with preemption
- Bin packing (P2): Optimize resource utilization

**Location in Implementation**: `jarvis/scheduler/`

---

### 3. State Manager
**Purpose**: Centralized state tracking and persistence  
**Priority**: P0 (in-memory), P1 (persistent)  
**Technology**: In-memory (Phase 1), etcd (Phase 3)

**Responsibilities**:
- Track all tasks and their states
- Maintain node registry
- Store cluster configuration
- Provide state queries
- Handle persistence

**State Tracked**:
- Task metadata and status
- Worker node registry and health
- Cluster configuration
- Historical data (P2)

**Location in Implementation**: `jarvis/state/`

---

### 4. Worker
**Purpose**: Task execution on individual nodes  
**Priority**: P0 (basic execution), P1 (monitoring)  
**Technology**: Python with Docker API

**Responsibilities**:
- Register with scheduler
- Execute assigned tasks in containers
- Monitor local resource usage
- Report task status
- Send heartbeats

**Execution Flow**:
1. Receive task assignment
2. Pull container image
3. Create and start container
4. Monitor execution
5. Report completion/failure
6. Cleanup resources

**Location in Implementation**: `jarvis/worker/`

---

### 5. Monitor
**Purpose**: Health tracking and observability  
**Priority**: P1 (basic), P2 (full observability)  
**Technology**: Python with Prometheus

**Responsibilities**:
- Heartbeat monitoring
- Detect node failures
- Collect metrics
- Generate alerts
- Export to Prometheus

**Metrics Collected**:
- Node health and availability
- Task execution stats
- Resource utilization
- Scheduler performance
- System throughput

**Location in Implementation**: `jarvis/monitor/`

---

### 6. DAG Manager
**Purpose**: Workflow and dependency management  
**Priority**: P2 (Advanced feature)  
**Technology**: Python with graph algorithms

**Responsibilities**:
- Parse DAG definitions
- Validate DAG structure (no cycles)
- Resolve task dependencies
- Schedule tasks in correct order
- Handle partial failures

**Location in Implementation**: `jarvis/dag/`

---

## 🔧 Technology Stack

### Core Technologies
- **Language**: Python 3.9+
- **API Framework**: FastAPI
- **Async Runtime**: asyncio
- **Container Runtime**: Docker
- **State Storage**: 
  - Phase 1: In-memory (Python dict)
  - Phase 3: etcd or Consul
- **Message Queue**: Redis Streams or RabbitMQ (P1)

### Supporting Technologies
- **Metrics**: Prometheus + Grafana (P2)
- **Logging**: Python logging with structured output (P0)
- **Configuration**: YAML files (P0)
- **Testing**: pytest (P0)
- **Deployment**: Docker, Kubernetes (P2)

---

## 🔄 Data Flows

### Task Submission Flow
```
Client
  ↓ POST /tasks
API Server
  ↓ Validate & enqueue
Scheduler (Task Queue)
  ↓ Match resources
Resource Matcher
  ↓ Select node
Worker Node
  ↓ Execute in container
Task Executor
  ↓ Report status
State Manager
  ↓ Update state
API Server
  ↓ GET /tasks/{id}
Client
```

### Heartbeat Flow
```
Worker Node
  ↓ Periodic heartbeat
Monitor (Heartbeat Listener)
  ↓ Update last seen
State Manager (Node Registry)
  ↓ Check threshold
Monitor (Failure Detector)
  ↓ If timeout
Scheduler (Task Recovery)
  ↓ Reschedule tasks
Available Nodes
```

---

## 🎯 Design Principles

### 1. Distributed by Default
- No single point of failure
- Leader election for control plane (P3)
- Data replication across nodes (P3)

### 2. API-First Design
- All functionality via REST APIs
- Clear versioning (v1, v2, etc.)
- Comprehensive OpenAPI docs

### 3. Container-Native
- All tasks run in containers
- Docker as execution environment
- Kubernetes-compatible (future)

### 4. Modular Architecture
- Clear component boundaries
- Pluggable schedulers (P2)
- Extensible via plugins (P3)

### 5. Cloud-Agnostic
- No cloud-specific dependencies (P0-P1)
- Multi-cloud support (P3)
- On-premise friendly

---

## 📊 Component Dependencies

```
Build/Test Order:
1. utils → exceptions → constants
2. state (memory backend) → config
3. scheduler (basic) → state
4. worker → scheduler communication
5. api → scheduler + state
6. monitor → scheduler + worker
7. dag → scheduler
```

---

## 🔗 Detailed Documentation

For complete architectural details, see:
- **Full Design**: [/DESIGN_PLAN.md](../../DESIGN_PLAN.md)
- **Use Cases**: [/USE_CASES.md](../../USE_CASES.md)
- **Architecture Docs**: [/docs/architecture/](../../docs/architecture/)
- **ADRs**: [/docs/adr/](../../docs/adr/)

For implementation structure:
- **File Tree**: [/JARVIS_FILE_TREE.md](../../JARVIS_FILE_TREE.md)
- **Implementation Guide**: [../implementation/core-components.md](../implementation/core-components.md)

---

**Source Documents**: DESIGN_PLAN.md, docs/architecture/, docs/adr/  
**Last Updated**: 2026-01-08  
**Status**: Current as of Phase 0  
**Next**: Return to [Planning Index](index.md) or [Main Index](../INDEX.md)
