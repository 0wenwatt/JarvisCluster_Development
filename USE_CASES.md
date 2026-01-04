# Jarvis Use Cases and Interaction Flows

## Document Purpose

This document bridges the gap between high-level design (DESIGN_PLAN.md) and implementation details. It provides concrete examples of how users and system components interact to accomplish real-world tasks.

---

## Use Case Categories

1. **Basic Task Management** - Core scheduling functionality
2. **Resource Management** - Node and resource handling
3. **Monitoring and Observability** - System health and metrics
4. **Failure Scenarios** - Error handling and recovery
5. **Advanced Features** - Multi-node, priorities, dependencies

---

## Use Case 1: Submit and Execute a Simple Task

### Actors
- User (via CLI/API)
- API Server
- Scheduler
- Worker Node
- Task Executor

### Preconditions
- Jarvis cluster is running
- At least one worker node is registered and available
- User has authentication credentials

### Flow

```
User → API Server: POST /tasks
                   {
                     "name": "data-processing-job",
                     "image": "python:3.9",
                     "command": ["python", "process.py"],
                     "resources": {
                       "cpu": "1000m",
                       "memory": "512Mi"
                     }
                   }

API Server → Scheduler: Enqueue task
                        Validate resources
                        Generate task ID

Scheduler → State Store: Persist task metadata
                         Status: PENDING

Scheduler → Scheduler: Resource matching algorithm
                       Find suitable node

Scheduler → Worker Node: Assign task (via gRPC)
                         Task ID: task-abc123
                         Execution spec

Worker Node → Task Executor: Pull container image
                             Create container
                             Execute command

Task Executor → Worker Node: Report status changes
                              PENDING → RUNNING → COMPLETED

Worker Node → Scheduler: Status updates (heartbeat)

Scheduler → State Store: Update task status

API Server ← Scheduler: Task completed successfully

User ← API Server: GET /tasks/task-abc123
                   Status: COMPLETED
```

### Postconditions
- Task executed successfully
- Task status updated to COMPLETED
- Logs available for retrieval
- Resources freed on worker node

### Components Involved
- `api_server.py` (API handler)
- `scheduler/task_queue.py` (Task queuing)
- `scheduler/resource_matcher.py` (Resource allocation)
- `state/state_manager.py` (Persistence)
- `worker/task_executor.py` (Execution)
- `worker/node_agent.py` (Worker coordination)

---

## Use Case 2: Multi-Node Task Distribution

### Scenario
User submits 10 tasks, and Jarvis distributes them across 3 worker nodes based on available resources.

### Flow

```
User → API Server: POST /tasks/batch
                   [Task1, Task2, ..., Task10]

API Server → Scheduler: Batch enqueue
                        Validate all tasks

Scheduler → State Store: Persist all tasks
                         Status: PENDING for all

Scheduler → Scheduler: For each task:
                       - Calculate resource requirements
                       - Score available nodes
                       - Select best node
                       - Consider load balancing

Scheduler → Worker Node 1: Assign [Task1, Task4, Task7]
         → Worker Node 2: Assign [Task2, Task5, Task8]
         → Worker Node 3: Assign [Task3, Task6, Task9, Task10]

[Parallel Execution on all nodes]

Worker Nodes → Scheduler: Continuous status updates

Scheduler → State Store: Update all task statuses

User ← API Server: GET /tasks?batch_id=batch-xyz
                   [All tasks with current status]
```

### Decision Logic (Scheduler)

```python
def select_node_for_task(task, available_nodes):
    """
    Score each node based on:
    1. Available resources (CPU, memory)
    2. Current load
    3. Task affinity rules
    4. Network locality
    """
    scores = {}
    for node in available_nodes:
        if node.has_sufficient_resources(task):
            score = calculate_score(
                resource_fit=node.resource_availability,
                load=node.current_load,
                affinity=check_affinity(task, node),
                locality=network_distance(task, node)
            )
            scores[node] = score
    
    return max(scores, key=scores.get)
```

### Components Involved
- `scheduler/batch_scheduler.py`
- `scheduler/node_scorer.py`
- `scheduler/load_balancer.py`

---

## Use Case 3: Task with Priority Scheduling

### Scenario
High-priority task arrives while normal tasks are queued. System should schedule high-priority task first.

### Flow

```
Initial State:
- Queue: [TaskA (normal), TaskB (normal), TaskC (normal)]
- All nodes busy

User → API Server: POST /tasks
                   {
                     "name": "urgent-alert-processing",
                     "priority": "high",
                     ...
                   }

API Server → Scheduler: Enqueue with priority

Scheduler → Priority Queue: Insert task at high-priority position
                            New Queue:
                            [TaskD (high), TaskA (normal), TaskB (normal), TaskC (normal)]

[Node becomes available]

Scheduler → Scheduler: Dequeue next task
                       Select TaskD (highest priority)

Scheduler → Worker Node: Assign TaskD immediately

Worker Node → Task Executor: Execute TaskD before others
```

### Priority Queue Structure

```
Priority Queue:
├── Critical (P0) - SLA violations, system failures
├── High (P1)     - User-facing, time-sensitive
├── Normal (P2)   - Standard workloads
└── Low (P3)      - Background, maintenance tasks
```

### Components Involved
- `scheduler/priority_queue.py`
- `scheduler/scheduler_policy.py`

---

## Use Case 4: Task Failure and Retry

### Scenario
Task fails due to transient error (network timeout). System should automatically retry.

### Flow

```
Worker Node → Task Executor: Execute task
                             Result: FAILED
                             Error: "Connection timeout"

Task Executor → Worker Node: Report failure with error details

Worker Node → Scheduler: Task failed notification
                         Error details included

Scheduler → State Store: Update status to FAILED
                         Increment retry count

Scheduler → Retry Policy: Check if retry allowed
                          Current retry: 1
                          Max retries: 3
                          Result: RETRY

Scheduler → Scheduler: Calculate backoff delay
                       Delay = 2^retry_count seconds
                       Delay = 2 seconds

[Wait 2 seconds]

Scheduler → Task Queue: Re-enqueue task
                        Priority: Same as original

Scheduler → Worker Node: Assign task (attempt 2)

[If successful]
Worker Node → Scheduler: Task completed

Scheduler → State Store: Update status to COMPLETED
                         Final attempt: 2

[If all retries exhausted]
Scheduler → State Store: Update status to PERMANENTLY_FAILED
Scheduler → Alerting: Send alert for manual intervention
```

### Retry Policy Configuration

```yaml
retry_policy:
  max_attempts: 3
  backoff_strategy: exponential
  backoff_base: 2
  max_backoff: 300  # 5 minutes
  retryable_errors:
    - "ConnectionTimeout"
    - "ServiceUnavailable"
    - "TemporaryFailure"
  non_retryable_errors:
    - "InvalidInput"
    - "AuthenticationError"
    - "ResourceNotFound"
```

### Components Involved
- `scheduler/retry_manager.py`
- `scheduler/retry_policy.py`
- `error/error_classifier.py`

---

## Use Case 5: Node Failure and Task Rescheduling

### Scenario
Worker node crashes while executing tasks. System detects failure and reschedules tasks.

### Flow

```
Initial State:
- Worker Node 1: Running [TaskA, TaskB]
- Worker Node 2: Running [TaskC]
- Worker Node 3: Available

[Node 1 crashes - no heartbeat]

Scheduler → Heartbeat Monitor: Check node health
                                Node 1 last seen: 45 seconds ago
                                Threshold: 30 seconds
                                Result: NODE_UNHEALTHY

Scheduler → Node Registry: Mark Node 1 as OFFLINE
                           Remove from available nodes

Scheduler → Task Recovery: Find tasks on Node 1
                           Result: [TaskA (RUNNING), TaskB (RUNNING)]

Scheduler → State Store: Update task statuses
                         TaskA: RUNNING → PENDING (rescheduling)
                         TaskB: RUNNING → PENDING (rescheduling)

Scheduler → Scheduler: Re-evaluate task placement
                       TaskA → Assign to Node 3
                       TaskB → Assign to Node 2

Worker Nodes 2 & 3 → Task Executor: Execute rescheduled tasks

[Later - Node 1 recovers]

Worker Node 1 → Scheduler: Register/heartbeat
                           Status: HEALTHY

Scheduler → Node Registry: Mark Node 1 as AVAILABLE
                           Add to scheduling pool

Scheduler → Worker Node 1: Query orphaned tasks
                           Cleanup any lingering processes
```

### Heartbeat Mechanism

```python
class HeartbeatMonitor:
    def check_node_health(self, node_id):
        last_heartbeat = self.get_last_heartbeat(node_id)
        current_time = time.now()
        time_since_heartbeat = current_time - last_heartbeat
        
        if time_since_heartbeat > HEARTBEAT_TIMEOUT:
            self.handle_node_failure(node_id)
        elif time_since_heartbeat > HEARTBEAT_WARNING:
            self.send_warning_alert(node_id)
```

### Components Involved
- `monitor/heartbeat_monitor.py`
- `scheduler/task_recovery.py`
- `node/node_registry.py`

---

## Use Case 6: Task with Dependencies (DAG)

### Scenario
Data pipeline with dependencies: Extract → Transform → Load

### Flow

```
User → API Server: POST /tasks/dag
                   {
                     "name": "etl-pipeline",
                     "tasks": [
                       {
                         "id": "extract",
                         "command": ["python", "extract.py"],
                         "dependencies": []
                       },
                       {
                         "id": "transform",
                         "command": ["python", "transform.py"],
                         "dependencies": ["extract"]
                       },
                       {
                         "id": "load",
                         "command": ["python", "load.py"],
                         "dependencies": ["transform"]
                       }
                     ]
                   }

API Server → Scheduler: Create DAG workflow
                        Validate no cycles

Scheduler → DAG Manager: Build dependency graph
                         Topological sort: extract → transform → load

Scheduler → State Store: Persist DAG and all tasks
                         extract: PENDING
                         transform: WAITING (depends on extract)
                         load: WAITING (depends on transform)

Scheduler → Worker Node: Assign "extract" task only

Worker Node → Scheduler: extract COMPLETED

Scheduler → DAG Manager: Check dependent tasks
                         transform dependencies satisfied

Scheduler → State Store: Update transform status to PENDING

Scheduler → Worker Node: Assign "transform" task

Worker Node → Scheduler: transform COMPLETED

Scheduler → DAG Manager: Check dependent tasks
                         load dependencies satisfied

Scheduler → State Store: Update load status to PENDING

Scheduler → Worker Node: Assign "load" task

Worker Node → Scheduler: load COMPLETED

Scheduler → DAG Manager: All tasks complete
                         Mark DAG as COMPLETED

User ← API Server: GET /dags/etl-pipeline
                   Status: COMPLETED
                   All tasks: COMPLETED
```

### DAG Dependency Resolution

```python
class DAGManager:
    def check_ready_tasks(self, dag_id):
        """Find tasks whose dependencies are all satisfied"""
        dag = self.get_dag(dag_id)
        ready_tasks = []
        
        for task in dag.tasks:
            if task.status == 'WAITING':
                dependencies = task.dependencies
                all_complete = all(
                    self.get_task_status(dep) == 'COMPLETED'
                    for dep in dependencies
                )
                if all_complete:
                    ready_tasks.append(task)
        
        return ready_tasks
```

### Components Involved
- `scheduler/dag_manager.py`
- `scheduler/dependency_resolver.py`
- `scheduler/dag_validator.py`

---

## Use Case 7: Resource Monitoring and Metrics

### Scenario
System continuously collects and exposes metrics for monitoring dashboards.

### Flow

```
[Continuous Loop]

Worker Node → Resource Monitor: Collect local metrics
                                CPU: 45%
                                Memory: 2.3GB / 8GB
                                Disk: 120GB / 500GB
                                Network: 1.2MB/s

Resource Monitor → Metrics Store: Push metrics
                                   Timestamp: 2026-01-04T21:35:00Z

Worker Node → Scheduler: Include metrics in heartbeat

Scheduler → Metrics Store: Push control plane metrics
                           Queue depth: 12
                           Scheduling rate: 150 tasks/min
                           Average latency: 45ms

Metrics Store → Prometheus: Export metrics in Prometheus format

Grafana ← Prometheus: Query metrics
                      Build dashboards
                      Evaluate alert rules

[Alert triggered if CPU > 80%]

Prometheus → Alert Manager: CPU high on Worker Node 2

Alert Manager → Notification: Send Slack message
                              Page on-call engineer
```

### Key Metrics

```python
# Scheduler Metrics
scheduler_queue_depth = Gauge('scheduler_queue_depth', 'Tasks in queue')
scheduler_throughput = Counter('scheduler_tasks_scheduled', 'Tasks scheduled')
scheduler_latency = Histogram('scheduler_latency_seconds', 'Scheduling latency')

# Worker Metrics
worker_cpu_usage = Gauge('worker_cpu_usage_percent', 'CPU usage', ['node_id'])
worker_memory_usage = Gauge('worker_memory_bytes', 'Memory usage', ['node_id'])
worker_task_count = Gauge('worker_active_tasks', 'Active tasks', ['node_id'])

# Task Metrics
task_duration = Histogram('task_duration_seconds', 'Task execution time')
task_failures = Counter('task_failures_total', 'Failed tasks', ['error_type'])
```

### Components Involved
- `monitor/resource_monitor.py`
- `monitor/metrics_collector.py`
- `monitor/prometheus_exporter.py`

---

## Use Case 8: Auto-scaling Based on Load

### Scenario
Queue depth increases, system automatically requests more worker nodes.

### Flow

```
Scheduler → Load Monitor: Check current load
                          Queue depth: 500 tasks
                          Average wait time: 10 minutes
                          Active nodes: 3
                          Total capacity: 30 concurrent tasks

Load Monitor → Scaling Policy: Evaluate scaling rules
                               Rule 1: queue_depth > 100 → scale up
                               Rule 2: avg_wait > 5min → scale up
                               Both triggered!

Scaling Policy → Autoscaler: Calculate desired nodes
                             Current: 3 nodes
                             Desired: 6 nodes (2x scale)
                             Add: 3 nodes

Autoscaler → Cloud API: Request 3 new instances
                        Instance type: m5.xlarge
                        Region: us-east-1

Cloud API → Autoscaler: Instances created
                        Node IDs: [node-4, node-5, node-6]

[New nodes boot and start worker agent]

Worker Nodes (new) → Scheduler: Register nodes
                                Report resources
                                Status: AVAILABLE

Scheduler → Node Registry: Add nodes to pool
                           Total nodes: 6

Scheduler → Scheduler: Redistribute tasks
                       Utilize new capacity

[Later - Load decreases]

Load Monitor → Scaling Policy: Queue depth: 5 tasks
                               Nodes: 6
                               Utilization: 20%
                               Evaluation: Scale down

Autoscaler → Scheduler: Drain nodes [node-4, node-5, node-6]
                        No new tasks assigned

Scheduler → Worker Nodes: Wait for tasks to complete

Worker Nodes → Scheduler: All tasks completed
                          Nodes idle

Autoscaler → Cloud API: Terminate instances
                        [node-4, node-5, node-6]
```

### Scaling Policy Example

```yaml
autoscaling:
  enabled: true
  min_nodes: 1
  max_nodes: 20
  
  scale_up_rules:
    - metric: queue_depth
      threshold: 100
      action: add_nodes
      count: 2
    - metric: average_wait_time
      threshold: 300  # 5 minutes
      action: add_nodes
      count: 1
  
  scale_down_rules:
    - metric: cluster_utilization
      threshold: 30  # percent
      cooldown: 600  # 10 minutes
      action: remove_nodes
      count: 1
```

### Components Involved
- `autoscaler/load_monitor.py`
- `autoscaler/scaling_policy.py`
- `autoscaler/cloud_provider.py`

---

## Component Interaction Summary

### Primary Data Flows

```
1. Task Submission Flow
   User → API → Scheduler → State → Worker

2. Status Update Flow
   Worker → Scheduler → State → API → User

3. Monitoring Flow
   Worker → Monitor → Metrics Store → Dashboard

4. Failure Detection Flow
   Heartbeat Monitor → Scheduler → Task Recovery → Worker

5. Autoscaling Flow
   Monitor → Autoscaler → Cloud Provider → Scheduler
```

### Component Dependencies

```
Core Components (MVP - Phase 1):
├── API Server
│   └── Depends on: Scheduler, State Store
├── Scheduler
│   └── Depends on: State Store, Node Registry
├── Worker Node
│   └── Depends on: Task Executor
└── State Store
    └── Depends on: None (foundation)

Advanced Components (Later Phases):
├── DAG Manager
│   └── Depends on: Scheduler, Dependency Resolver
├── Autoscaler
│   └── Depends on: Load Monitor, Cloud Provider API
├── Monitor
│   └── Depends on: Metrics Collector, Prometheus
└── Retry Manager
    └── Depends on: Scheduler, Retry Policy
```

---

## Module Mapping to Use Cases

| Use Case | Primary Modules | Priority |
|----------|----------------|----------|
| UC1: Simple Task | API, Scheduler, Worker, State | P0 (MVP) |
| UC2: Multi-Node | Scheduler, Node Registry, Load Balancer | P1 |
| UC3: Priority | Priority Queue, Scheduler Policy | P2 |
| UC4: Retry | Retry Manager, Error Classifier | P1 |
| UC5: Node Failure | Heartbeat Monitor, Task Recovery | P1 |
| UC6: Dependencies | DAG Manager, Dependency Resolver | P2 |
| UC7: Monitoring | Resource Monitor, Metrics Collector | P1 |
| UC8: Autoscaling | Load Monitor, Autoscaler | P3 |

---

**Document Status**: Living Document  
**Last Updated**: 2026-01-04  
**Version**: 1.0  
**Owner**: Development Team
