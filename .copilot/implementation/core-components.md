# Core Components

**Parent**: [Implementation Index](index.md)  
**Level**: 3 (Topic Detail)

---

## 📋 Summary

This document details the MVP-critical components (P0 priority) that form the foundation of the Jarvis cluster management system. These must be built first and are essential for basic functionality.

---

## 🎯 MVP Scope (P0 Components)

The Minimum Viable Product consists of these core components:

1. **API Server** - External interface
2. **Scheduler** - Task queue and basic scheduling
3. **Worker** - Task execution on nodes
4. **State Manager** - In-memory state tracking
5. **Utilities** - Logging, config, exceptions

**MVP Goal**: Submit a task via API, have it scheduled to a worker node, executed in a container, and return status.

---

## 🔧 Component Breakdown

### 1. API Server (`jarvis/api/`)

**Files** (P0):
- `api/server.py` - Main server application
- `api/routes/tasks.py` - Task endpoints
- `api/routes/health.py` - Health check endpoints
- `api/models/task.py` - Request/response models
- `api/models/error.py` - Error models
- `api/validators.py` - Input validation

**Key Functions**:
```python
# api/server.py
create_app() -> FastAPI           # Create FastAPI application
register_routes()                 # Register all route handlers
start_server()                    # Start HTTP server

# api/routes/tasks.py
submit_task() -> TaskResponse     # POST /tasks - Submit new task
get_task(id) -> TaskResponse      # GET /tasks/{id} - Get task status
list_tasks() -> List[Task]        # GET /tasks - List all tasks

# api/routes/health.py
health_check() -> HealthResponse  # GET /health - Basic health check
```

**Dependencies**: State Manager, Scheduler

**Estimated LOC**: ~800 lines

---

### 2. Scheduler (`jarvis/scheduler/`)

**Files** (P0):
- `scheduler/scheduler.py` - Main scheduler loop
- `scheduler/task_queue.py` - FIFO task queue
- `scheduler/resource_matcher.py` - Resource matching logic

**Key Functions**:
```python
# scheduler/scheduler.py
start()                           # Start scheduler loop
stop()                            # Stop scheduler
schedule_task(task: Task)         # Schedule a single task
process_queue()                   # Main scheduling loop

# scheduler/task_queue.py
enqueue(task: Task)               # Add task to queue
dequeue() -> Optional[Task]       # Get next task
peek() -> Optional[Task]          # View next task
size() -> int                     # Queue size

# scheduler/resource_matcher.py
find_suitable_node(task, nodes) -> Optional[Node]
check_resource_availability(node, task) -> bool
```

**Scheduling Algorithm (P0)**:
1. Pull next task from FIFO queue
2. Find first node with sufficient resources
3. Assign task to node
4. Update state
5. Notify worker

**Dependencies**: State Manager, Task Queue

**Estimated LOC**: ~600 lines

---

### 3. Worker (`jarvis/worker/`)

**Files** (P0):
- `worker/node_agent.py` - Worker node agent
- `worker/task_executor.py` - Container-based execution

**Key Functions**:
```python
# worker/node_agent.py
start()                           # Start worker agent
stop()                            # Stop agent
register_node()                   # Register with scheduler
send_heartbeat()                  # Periodic heartbeat
receive_task(task)                # Accept task assignment
report_status(task, status)       # Report execution status

# worker/task_executor.py
execute_task(task) -> Result      # Execute task in container
pull_image(image)                 # Pull Docker image
create_container(task)            # Create container
start_container(container)        # Start execution
wait_for_completion()             # Wait for task
get_exit_code() -> int            # Get result
cleanup_container()               # Remove container
```

**Execution Flow**:
```
1. Receive task from scheduler
2. Pull container image (if needed)
3. Create container with task specs
4. Start container
5. Monitor execution
6. Capture exit code and logs
7. Report success/failure to scheduler
8. Cleanup container
```

**Dependencies**: Docker API, State Manager (for reporting)

**Estimated LOC**: ~500 lines

---

### 4. State Manager (`jarvis/state/`)

**Files** (P0):
- `state/state_manager.py` - Main state management
- `state/backend/memory.py` - In-memory storage backend

**Key Functions**:
```python
# state/state_manager.py
initialize()                      # Initialize state
save_task(task: Task)             # Persist task
get_task(id: str) -> Optional[Task]
update_task(id, updates)          # Update task state
list_tasks(filters) -> List[Task]
query_tasks(query) -> List[Task]

# state/backend/memory.py (P0 - In-memory implementation)
_store: Dict[str, Task]           # Internal storage
put(key, value)                   # Store value
get(key) -> Optional[Any]         # Retrieve value
delete(key)                       # Remove value
list_all() -> List[Any]           # List all items
```

**State Tracked**:
- Task ID, status, assigned node
- Task specification (image, command, resources)
- Task timestamps (submitted, started, completed)
- Task results (exit code, error message)

**Note**: Phase 1 uses in-memory storage. Phase 3 adds persistent backends (etcd, PostgreSQL).

**Dependencies**: None (foundation component)

**Estimated LOC**: ~400 lines

---

### 5. Utilities (`jarvis/utils/`)

**Files** (P0):
- `utils/logging.py` - Logging utilities
- `utils/time_utils.py` - Time helpers
- `utils/validation.py` - Validation functions
- `utils/serialization.py` - JSON serialization

**Key Functions**:
```python
# utils/logging.py
setup_logging(config)             # Configure logging
get_logger(name) -> Logger        # Get logger instance

# utils/time_utils.py
now() -> datetime                 # Current timestamp
timestamp_to_datetime(ts)         # Convert timestamp
format_duration(seconds) -> str   # Human-readable duration

# utils/validation.py
validate_resource_spec(spec)      # Validate resources
validate_id(id: str) -> bool      # Validate ID format

# utils/serialization.py
to_json(obj) -> str               # Serialize to JSON
from_json(json_str) -> Any        # Deserialize from JSON
```

**Dependencies**: None (foundation utilities)

**Estimated LOC**: ~300 lines

---

### 6. Configuration & Foundation

**Files** (P0):
- `jarvis/__init__.py` - Package initialization
- `jarvis/config.py` - Configuration management
- `jarvis/constants.py` - Global constants
- `jarvis/exceptions.py` - Custom exceptions
- `jarvis/version.py` - Version info

**Key Components**:
```python
# config.py
load_config(path: str) -> Config  # Load YAML config
get_config() -> Config            # Get current config

# exceptions.py
class TaskError(Exception)        # Task-related errors
class SchedulerError(Exception)   # Scheduler errors
class WorkerError(Exception)      # Worker errors
class StateError(Exception)       # State management errors

# constants.py
TASK_STATUS_PENDING = "pending"
TASK_STATUS_RUNNING = "running"
TASK_STATUS_COMPLETED = "completed"
TASK_STATUS_FAILED = "failed"
```

**Dependencies**: None

**Estimated LOC**: ~200 lines

---

## 📊 MVP Statistics

| Component | Files | Functions | LOC | Complexity |
|-----------|-------|-----------|-----|------------|
| API Server | 6 | ~12 | 800 | Medium |
| Scheduler | 3 | ~15 | 600 | Medium |
| Worker | 2 | ~12 | 500 | Medium |
| State Manager | 2 | ~10 | 400 | Low |
| Utilities | 4 | ~12 | 300 | Low |
| Foundation | 5 | ~8 | 200 | Low |
| **Total P0** | **22** | **~69** | **~2,800** | **Medium** |

---

## 🔄 Component Integration

### Data Flow Example: Task Submission
```
1. Client → API Server
   POST /tasks {image: "ubuntu", command: "echo hello"}

2. API Server → Validators
   validate_task_request(request)

3. API Server → State Manager
   save_task(task) [status: pending]

4. API Server → Scheduler
   schedule_task(task)

5. Scheduler → Task Queue
   enqueue(task)

6. Scheduler Loop → Resource Matcher
   find_suitable_node(task, available_nodes)

7. Scheduler → Worker Agent
   send_task_assignment(task, node)

8. Worker → Task Executor
   execute_task(task)

9. Worker → State Manager
   update_task(task_id, status: running)

10. Task Executor → Docker
    create_container(), start_container()

11. Task Completes → Worker
    get_exit_code(), cleanup()

12. Worker → State Manager
    update_task(task_id, status: completed, result: 0)

13. Client → API Server
    GET /tasks/{id} → {status: completed, result: 0}
```

---

## 🏗️ Build Order

The components must be built in this order due to dependencies:

```
Phase 1 (Week 1): Foundation
1. jarvis/constants.py
2. jarvis/exceptions.py
3. jarvis/utils/logging.py
4. jarvis/config.py

Phase 2 (Week 2): State Layer
5. jarvis/utils/serialization.py
6. jarvis/state/backend/memory.py
7. jarvis/state/state_manager.py

Phase 3 (Week 3): Scheduler
8. jarvis/scheduler/task_queue.py
9. jarvis/scheduler/resource_matcher.py
10. jarvis/scheduler/scheduler.py

Phase 4 (Week 4): Worker
11. jarvis/worker/task_executor.py
12. jarvis/worker/node_agent.py

Phase 5 (Week 5): API
13. jarvis/api/models/
14. jarvis/api/validators.py
15. jarvis/api/routes/
16. jarvis/api/server.py
```

---

## 🧪 Testing Requirements

Each component needs unit tests (P0):

```
tests/unit/
├── test_task_queue.py        # Test queue operations
├── test_resource_matcher.py  # Test resource matching
├── test_state_manager.py     # Test state operations
├── test_scheduler.py         # Test scheduling logic
└── test_worker.py            # Test task execution (mocked Docker)
```

**Minimum Coverage**: 70% for P0 components

---

## 🔗 Related Documentation

- **Full File Tree**: [/JARVIS_FILE_TREE.md](../../JARVIS_FILE_TREE.md) - Complete specification
- **Architecture**: [../planning/design.md](../planning/design.md) - System design
- **Dependencies**: [dependencies.md](dependencies.md) - Module dependencies

---

**Source**: JARVIS_FILE_TREE.md  
**Last Updated**: 2026-01-08  
**Phase**: Phase 1 - MVP  
**Status**: Specification complete, implementation pending  
**Next**: Return to [Implementation Index](index.md) or [Main Index](../INDEX.md)
