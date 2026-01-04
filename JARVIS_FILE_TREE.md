# Jarvis Implementation File Tree

## Purpose

This document defines the **desired end-goal** file tree structure for the Jarvis implementation repository. Each component, module, file, and function is listed with its development priority, allowing comparison between planned and actual implementation.

---

## Development Priority Legend

- **P0** - MVP Critical (Phase 1): Must have for basic functionality
- **P1** - Core Features (Phase 2-3): Essential for production use
- **P2** - Advanced Features (Phase 4-5): Enhanced functionality
- **P3** - Optional Features (Phase 6+): Nice-to-have, future enhancements

---

## Complete File Tree Structure

```
jarvis/
│
├── README.md                                    [P0] Project overview
├── LICENSE                                      [P0] License file
├── setup.py                                     [P0] Package setup
├── requirements.txt                             [P0] Python dependencies
├── requirements-dev.txt                         [P0] Development dependencies
├── .gitignore                                   [P0] Git ignore rules
├── .github/                                     [P1] GitHub configuration
│   ├── workflows/                               [P1] CI/CD workflows
│   │   ├── ci.yml                               [P1] Continuous integration
│   │   ├── tests.yml                            [P1] Test automation
│   │   └── security.yml                         [P2] Security scanning
│   └── PULL_REQUEST_TEMPLATE.md                 [P1] PR template
│
├── config/                                      [P0] Configuration files
│   ├── default.yaml                             [P0] Default configuration
│   ├── development.yaml                         [P0] Dev environment config
│   ├── production.yaml                          [P1] Prod environment config
│   └── schema.yaml                              [P1] Config validation schema
│
├── docs/                                        [P1] Documentation
│   ├── architecture.md                          [P1] Architecture overview
│   ├── api-reference.md                         [P1] API documentation
│   ├── deployment.md                            [P2] Deployment guide
│   ├── development.md                           [P0] Development setup
│   └── troubleshooting.md                       [P2] Troubleshooting guide
│
├── scripts/                                     [P1] Utility scripts
│   ├── setup-dev.sh                             [P0] Dev environment setup
│   ├── run-tests.sh                             [P0] Test runner
│   ├── build.sh                                 [P1] Build script
│   └── deploy.sh                                [P2] Deployment script
│
├── jarvis/                                      [P0] Main package
│   ├── __init__.py                              [P0] Package initialization
│   ├── __main__.py                              [P0] CLI entry point
│   ├── config.py                                [P0] Configuration management
│   ├── constants.py                             [P0] Global constants
│   ├── exceptions.py                            [P0] Custom exceptions
│   └── version.py                               [P0] Version information
│
├── jarvis/api/                                  [P0] API Server
│   ├── __init__.py                              [P0] API package init
│   ├── server.py                                [P0] Main server application
│   │   └── Functions:
│   │       ├── create_app()                     [P0] Create FastAPI/Flask app
│   │       ├── configure_middleware()           [P1] Setup middleware
│   │       ├── register_routes()                [P0] Register all routes
│   │       └── start_server()                   [P0] Start HTTP server
│   │
│   ├── routes/                                  [P0] API route handlers
│   │   ├── __init__.py                          [P0]
│   │   ├── tasks.py                             [P0] Task endpoints
│   │   │   └── Functions:
│   │   │       ├── submit_task()                [P0] POST /tasks
│   │   │       ├── get_task()                   [P0] GET /tasks/{id}
│   │   │       ├── list_tasks()                 [P0] GET /tasks
│   │   │       ├── cancel_task()                [P1] DELETE /tasks/{id}
│   │   │       ├── get_task_logs()              [P1] GET /tasks/{id}/logs
│   │   │       └── submit_batch()               [P1] POST /tasks/batch
│   │   │
│   │   ├── nodes.py                             [P1] Node endpoints
│   │   │   └── Functions:
│   │   │       ├── list_nodes()                 [P1] GET /nodes
│   │   │       ├── get_node()                   [P1] GET /nodes/{id}
│   │   │       ├── drain_node()                 [P2] POST /nodes/{id}/drain
│   │   │       └── cordon_node()                [P2] POST /nodes/{id}/cordon
│   │   │
│   │   ├── health.py                            [P0] Health check endpoints
│   │   │   └── Functions:
│   │   │       ├── health_check()               [P0] GET /health
│   │   │       ├── readiness_check()            [P1] GET /ready
│   │   │       └── liveness_check()             [P1] GET /alive
│   │   │
│   │   ├── metrics.py                           [P2] Metrics endpoints
│   │   │   └── Functions:
│   │   │       ├── get_metrics()                [P2] GET /metrics
│   │   │       └── get_cluster_stats()          [P2] GET /stats
│   │   │
│   │   └── dags.py                              [P2] DAG workflow endpoints
│   │       └── Functions:
│   │           ├── submit_dag()                 [P2] POST /dags
│   │           ├── get_dag()                    [P2] GET /dags/{id}
│   │           └── list_dags()                  [P2] GET /dags
│   │
│   ├── models/                                  [P0] API data models
│   │   ├── __init__.py                          [P0]
│   │   ├── task.py                              [P0] Task request/response models
│   │   ├── node.py                              [P1] Node models
│   │   ├── error.py                             [P0] Error response models
│   │   └── dag.py                               [P2] DAG models
│   │
│   ├── validators.py                            [P0] Input validation
│   │   └── Functions:
│   │       ├── validate_task_request()          [P0]
│   │       ├── validate_resource_spec()         [P0]
│   │       └── validate_dag_structure()         [P2]
│   │
│   └── middleware.py                            [P1] API middleware
│       └── Functions:
│           ├── auth_middleware()                [P2] Authentication
│           ├── rate_limit_middleware()          [P2] Rate limiting
│           ├── logging_middleware()             [P1] Request logging
│           └── error_handler_middleware()       [P1] Error handling
│
├── jarvis/scheduler/                            [P0] Scheduler Component
│   ├── __init__.py                              [P0]
│   ├── scheduler.py                             [P0] Main scheduler
│   │   └── Functions:
│   │       ├── start()                          [P0] Start scheduler loop
│   │       ├── stop()                           [P0] Stop scheduler
│   │       ├── schedule_task()                  [P0] Schedule single task
│   │       ├── schedule_batch()                 [P1] Schedule multiple tasks
│   │       └── process_queue()                  [P0] Process task queue
│   │
│   ├── task_queue.py                            [P0] Task queue management
│   │   └── Functions:
│   │       ├── enqueue()                        [P0] Add task to queue
│   │       ├── dequeue()                        [P0] Get next task
│   │       ├── peek()                           [P0] View next task
│   │       ├── size()                           [P0] Queue size
│   │       └── clear()                          [P1] Clear queue
│   │
│   ├── priority_queue.py                        [P2] Priority-based queue
│   │   └── Functions:
│   │       ├── enqueue_with_priority()          [P2]
│   │       ├── dequeue_highest()                [P2]
│   │       └── reorder()                        [P2]
│   │
│   ├── resource_matcher.py                      [P0] Resource matching
│   │   └── Functions:
│   │       ├── find_suitable_node()             [P0] Find node for task
│   │       ├── check_resource_availability()    [P0] Check resources
│   │       ├── calculate_fit_score()            [P1] Score node fitness
│   │       └── filter_nodes()                   [P1] Filter by constraints
│   │
│   ├── node_scorer.py                           [P1] Node scoring algorithms
│   │   └── Functions:
│   │       ├── score_node()                     [P1] Overall node score
│   │       ├── resource_score()                 [P1] Resource availability
│   │       ├── load_score()                     [P1] Current load
│   │       ├── affinity_score()                 [P2] Affinity rules
│   │       └── locality_score()                 [P2] Network locality
│   │
│   ├── load_balancer.py                         [P1] Load balancing
│   │   └── Functions:
│   │       ├── balance_tasks()                  [P1] Distribute tasks
│   │       ├── round_robin()                    [P1] Round-robin algorithm
│   │       ├── least_loaded()                   [P1] Least loaded algorithm
│   │       └── random_selection()               [P1] Random algorithm
│   │
│   ├── scheduler_policy.py                      [P2] Scheduling policies
│   │   └── Functions:
│   │       ├── get_policy()                     [P2] Get current policy
│   │       ├── set_policy()                     [P2] Set policy
│   │       ├── bin_packing_policy()             [P2] Bin packing
│   │       └── spread_policy()                  [P2] Spread tasks
│   │
│   ├── retry_manager.py                         [P1] Task retry handling
│   │   └── Functions:
│   │       ├── should_retry()                   [P1] Check if retry
│   │       ├── calculate_backoff()              [P1] Backoff delay
│   │       ├── retry_task()                     [P1] Retry failed task
│   │       └── mark_permanently_failed()        [P1] Mark as failed
│   │
│   ├── retry_policy.py                          [P1] Retry policies
│   │   └── Functions:
│   │       ├── load_policy()                    [P1] Load retry config
│   │       ├── is_retryable_error()             [P1] Check error type
│   │       └── get_max_retries()                [P1] Get retry limit
│   │
│   └── task_recovery.py                         [P1] Task recovery
│       └── Functions:
│           ├── recover_tasks()                  [P1] Recover failed tasks
│           ├── find_orphaned_tasks()            [P1] Find orphaned
│           └── reschedule_tasks()               [P1] Reschedule tasks
│
├── jarvis/worker/                               [P0] Worker Node Component
│   ├── __init__.py                              [P0]
│   ├── node_agent.py                            [P0] Worker node agent
│   │   └── Functions:
│   │       ├── start()                          [P0] Start agent
│   │       ├── stop()                           [P0] Stop agent
│   │       ├── register_node()                  [P0] Register with scheduler
│   │       ├── send_heartbeat()                 [P0] Send heartbeat
│   │       ├── receive_task()                   [P0] Accept task assignment
│   │       └── report_status()                  [P0] Report task status
│   │
│   ├── task_executor.py                         [P0] Task execution
│   │   └── Functions:
│   │       ├── execute_task()                   [P0] Execute task
│   │       ├── pull_image()                     [P0] Pull container image
│   │       ├── create_container()               [P0] Create container
│   │       ├── start_container()                [P0] Start container
│   │       ├── wait_for_completion()            [P0] Wait for task
│   │       ├── get_exit_code()                  [P0] Get result
│   │       ├── cleanup_container()              [P0] Cleanup
│   │       └── kill_task()                      [P1] Force kill task
│   │
│   ├── resource_monitor.py                      [P1] Resource monitoring
│   │   └── Functions:
│   │       ├── collect_metrics()                [P1] Collect all metrics
│   │       ├── get_cpu_usage()                  [P1] CPU metrics
│   │       ├── get_memory_usage()               [P1] Memory metrics
│   │       ├── get_disk_usage()                 [P1] Disk metrics
│   │       ├── get_network_stats()              [P2] Network stats
│   │       └── get_available_resources()        [P0] Available resources
│   │
│   └── log_collector.py                         [P1] Log collection
│       └── Functions:
│           ├── collect_logs()                   [P1] Collect task logs
│           ├── stream_logs()                    [P1] Stream logs
│           ├── store_logs()                     [P1] Store logs
│           └── cleanup_old_logs()               [P2] Cleanup logs
│
├── jarvis/state/                                [P0] State Management
│   ├── __init__.py                              [P0]
│   ├── state_manager.py                         [P0] State manager
│   │   └── Functions:
│   │       ├── initialize()                     [P0] Initialize state
│   │       ├── save_task()                      [P0] Persist task
│   │       ├── get_task()                       [P0] Retrieve task
│   │       ├── update_task()                    [P0] Update task
│   │       ├── delete_task()                    [P1] Delete task
│   │       ├── list_tasks()                     [P0] List tasks
│   │       └── query_tasks()                    [P1] Query tasks
│   │
│   ├── node_registry.py                         [P1] Node registry
│   │   └── Functions:
│   │       ├── register_node()                  [P1] Register node
│   │       ├── unregister_node()                [P1] Remove node
│   │       ├── get_node()                       [P1] Get node info
│   │       ├── list_nodes()                     [P1] List all nodes
│   │       ├── update_node_status()             [P1] Update status
│   │       └── get_available_nodes()            [P1] Get active nodes
│   │
│   ├── backend/                                 [P1] Storage backends
│   │   ├── __init__.py                          [P1]
│   │   ├── base.py                              [P1] Base backend interface
│   │   ├── memory.py                            [P0] In-memory (dev/test)
│   │   ├── etcd.py                              [P1] etcd backend
│   │   ├── consul.py                            [P2] Consul backend
│   │   └── postgres.py                          [P2] PostgreSQL backend
│   │
│   └── migrations.py                            [P2] Data migrations
│       └── Functions:
│           ├── migrate()                        [P2] Run migrations
│           ├── rollback()                       [P2] Rollback migration
│           └── get_version()                    [P2] Current version
│
├── jarvis/monitor/                              [P1] Monitoring Component
│   ├── __init__.py                              [P1]
│   ├── heartbeat_monitor.py                     [P1] Heartbeat monitoring
│   │   └── Functions:
│   │       ├── start()                          [P1] Start monitoring
│   │       ├── check_node_health()              [P1] Check node health
│   │       ├── handle_node_failure()            [P1] Handle failure
│   │       └── send_warning_alert()             [P1] Send warning
│   │
│   ├── metrics_collector.py                     [P2] Metrics collection
│   │   └── Functions:
│   │       ├── collect_scheduler_metrics()      [P2]
│   │       ├── collect_worker_metrics()         [P2]
│   │       ├── collect_task_metrics()           [P2]
│   │       └── aggregate_metrics()              [P2]
│   │
│   ├── prometheus_exporter.py                   [P2] Prometheus exporter
│   │   └── Functions:
│   │       ├── export_metrics()                 [P2] Export to Prometheus
│   │       ├── register_metrics()               [P2] Register metrics
│   │       └── start_exporter()                 [P2] Start HTTP server
│   │
│   └── alerting.py                              [P2] Alerting system
│       └── Functions:
│           ├── send_alert()                     [P2] Send alert
│           ├── check_alert_rules()              [P2] Check rules
│           └── configure_channels()             [P2] Setup channels
│
├── jarvis/dag/                                  [P2] DAG Workflow Component
│   ├── __init__.py                              [P2]
│   ├── dag_manager.py                           [P2] DAG manager
│   │   └── Functions:
│   │       ├── create_dag()                     [P2] Create DAG
│   │       ├── execute_dag()                    [P2] Execute DAG
│   │       ├── check_ready_tasks()              [P2] Find ready tasks
│   │       └── mark_dag_complete()              [P2] Complete DAG
│   │
│   ├── dependency_resolver.py                   [P2] Dependency resolution
│   │   └── Functions:
│   │       ├── resolve_dependencies()           [P2]
│   │       ├── build_graph()                    [P2] Build dep graph
│   │       ├── topological_sort()               [P2] Sort tasks
│   │       └── check_satisfied()                [P2] Check deps
│   │
│   └── dag_validator.py                         [P2] DAG validation
│       └── Functions:
│           ├── validate_dag()                   [P2] Validate DAG
│           ├── check_cycles()                   [P2] Detect cycles
│           └── validate_task_refs()             [P2] Check references
│
├── jarvis/autoscaler/                           [P3] Autoscaling Component
│   ├── __init__.py                              [P3]
│   ├── load_monitor.py                          [P3] Load monitoring
│   │   └── Functions:
│   │       ├── monitor_load()                   [P3] Monitor cluster load
│   │       ├── calculate_metrics()              [P3] Calculate metrics
│   │       └── trigger_scaling()                [P3] Trigger scaling
│   │
│   ├── scaling_policy.py                        [P3] Scaling policies
│   │   └── Functions:
│   │       ├── evaluate_rules()                 [P3] Evaluate rules
│   │       ├── calculate_desired_nodes()        [P3] Calc nodes needed
│   │       └── check_cooldown()                 [P3] Check cooldown
│   │
│   └── cloud_provider.py                        [P3] Cloud provider API
│       └── Functions:
│           ├── create_instances()               [P3] Create nodes
│           ├── terminate_instances()            [P3] Remove nodes
│           ├── list_instances()                 [P3] List instances
│           └── wait_for_ready()                 [P3] Wait for boot
│
├── jarvis/auth/                                 [P2] Authentication/Authorization
│   ├── __init__.py                              [P2]
│   ├── authenticator.py                         [P2] Authentication
│   │   └── Functions:
│   │       ├── authenticate()                   [P2] Authenticate user
│   │       ├── validate_token()                 [P2] Validate token
│   │       └── generate_token()                 [P2] Generate token
│   │
│   └── authorizer.py                            [P2] Authorization
│       └── Functions:
│           ├── authorize()                      [P2] Check permission
│           ├── check_permission()               [P2] Check perm
│           └── get_user_roles()                 [P2] Get roles
│
├── jarvis/error/                                [P0] Error Handling
│   ├── __init__.py                              [P0]
│   ├── error_classifier.py                      [P1] Error classification
│   │   └── Functions:
│   │       ├── classify_error()                 [P1] Classify error
│   │       ├── is_retryable()                   [P1] Check retryable
│   │       └── get_error_category()             [P1] Get category
│   │
│   └── handlers.py                              [P1] Error handlers
│       └── Functions:
│           ├── handle_task_error()              [P1]
│           ├── handle_node_error()              [P1]
│           └── handle_api_error()               [P1]
│
├── jarvis/communication/                        [P1] Inter-component Communication
│   ├── __init__.py                              [P1]
│   ├── grpc/                                    [P1] gRPC communication
│   │   ├── __init__.py                          [P1]
│   │   ├── server.py                            [P1] gRPC server
│   │   ├── client.py                            [P1] gRPC client
│   │   └── protos/                              [P1] Protocol buffers
│   │       ├── scheduler.proto                  [P1]
│   │       ├── worker.proto                     [P1]
│   │       └── monitor.proto                    [P2]
│   │
│   └── http_client.py                           [P0] HTTP client
│       └── Functions:
│           ├── make_request()                   [P0]
│           ├── post()                           [P0]
│           ├── get()                            [P0]
│           └── delete()                         [P1]
│
├── jarvis/utils/                                [P0] Utility Functions
│   ├── __init__.py                              [P0]
│   ├── logging.py                               [P0] Logging utilities
│   │   └── Functions:
│   │       ├── setup_logging()                  [P0] Configure logging
│   │       ├── get_logger()                     [P0] Get logger
│   │       └── log_with_context()               [P1] Contextual logging
│   │
│   ├── time_utils.py                            [P0] Time utilities
│   │   └── Functions:
│   │       ├── now()                            [P0] Current time
│   │       ├── timestamp_to_datetime()          [P0]
│   │       ├── datetime_to_timestamp()          [P0]
│   │       └── format_duration()                [P1]
│   │
│   ├── validation.py                            [P0] Validation utilities
│   │   └── Functions:
│   │       ├── validate_resource_spec()         [P0]
│   │       ├── validate_id()                    [P0]
│   │       └── validate_config()                [P1]
│   │
│   └── serialization.py                         [P0] Serialization
│       └── Functions:
│           ├── serialize()                      [P0] Serialize object
│           ├── deserialize()                    [P0] Deserialize
│           ├── to_json()                        [P0] To JSON
│           └── from_json()                      [P0] From JSON
│
├── jarvis/cli/                                  [P1] Command Line Interface
│   ├── __init__.py                              [P1]
│   ├── main.py                                  [P1] CLI entry point
│   │   └── Functions:
│   │       ├── cli()                            [P1] Main CLI group
│   │       └── parse_args()                     [P1] Parse arguments
│   │
│   └── commands/                                [P1] CLI commands
│       ├── __init__.py                          [P1]
│       ├── task.py                              [P1] Task commands
│       │   └── Functions:
│       │       ├── submit()                     [P1] Submit task
│       │       ├── list()                       [P1] List tasks
│       │       ├── get()                        [P1] Get task
│       │       └── cancel()                     [P1] Cancel task
│       │
│       ├── node.py                              [P1] Node commands
│       │   └── Functions:
│       │       ├── list()                       [P1] List nodes
│       │       ├── get()                        [P1] Get node
│       │       └── drain()                      [P2] Drain node
│       │
│       └── cluster.py                           [P2] Cluster commands
│           └── Functions:
│               ├── status()                     [P2] Cluster status
│               └── stats()                      [P2] Cluster stats
│
└── tests/                                       [P0] Test Suite
    ├── __init__.py                              [P0]
    ├── conftest.py                              [P0] Pytest configuration
    │
    ├── unit/                                    [P0] Unit tests
    │   ├── __init__.py                          [P0]
    │   ├── test_task_queue.py                   [P0]
    │   ├── test_resource_matcher.py             [P0]
    │   ├── test_state_manager.py                [P0]
    │   ├── test_scheduler.py                    [P0]
    │   └── test_worker.py                       [P0]
    │
    ├── integration/                             [P1] Integration tests
    │   ├── __init__.py                          [P1]
    │   ├── test_api_scheduler.py                [P1]
    │   ├── test_scheduler_worker.py             [P1]
    │   └── test_multi_node.py                   [P1]
    │
    ├── e2e/                                     [P2] End-to-end tests
    │   ├── __init__.py                          [P2]
    │   ├── test_simple_task.py                  [P2]
    │   ├── test_multi_node_workflow.py          [P2]
    │   └── test_failure_recovery.py             [P2]
    │
    └── fixtures/                                [P0] Test fixtures
        ├── __init__.py                          [P0]
        ├── sample_tasks.py                      [P0]
        ├── mock_nodes.py                        [P0]
        └── test_data.json                       [P0]
```

---

## Development Order by Phase

### Phase 0: Foundation (Week 1-2)
```
- Setup repository structure
- README.md, LICENSE, .gitignore
- requirements.txt, setup.py
- config/default.yaml
- jarvis/__init__.py, constants.py, exceptions.py
- jarvis/utils/logging.py
- tests/conftest.py
```

### Phase 1: MVP - Single Node Scheduler (Week 3-5)
```
Core components marked [P0]:
1. jarvis/state/state_manager.py (in-memory backend)
2. jarvis/scheduler/task_queue.py
3. jarvis/scheduler/resource_matcher.py
4. jarvis/scheduler/scheduler.py
5. jarvis/worker/node_agent.py
6. jarvis/worker/task_executor.py
7. jarvis/api/server.py
8. jarvis/api/routes/tasks.py
9. jarvis/api/routes/health.py
10. All [P0] unit tests
```

### Phase 2: Multi-Node Support (Week 6-8)
```
Components marked [P1]:
1. jarvis/state/node_registry.py
2. jarvis/scheduler/node_scorer.py
3. jarvis/scheduler/load_balancer.py
4. jarvis/worker/resource_monitor.py
5. jarvis/monitor/heartbeat_monitor.py
6. jarvis/scheduler/task_recovery.py
7. jarvis/api/routes/nodes.py
8. jarvis/communication/grpc/* (gRPC implementation)
9. Integration tests
```

### Phase 3: State Persistence (Week 9-11)
```
1. jarvis/state/backend/etcd.py
2. jarvis/state/backend/base.py
3. Database schema setup
4. Data backup/restore utilities
5. Migration to persistent storage
```

### Phase 4: Advanced Scheduling (Week 12-15)
```
Components marked [P2]:
1. jarvis/scheduler/priority_queue.py
2. jarvis/scheduler/scheduler_policy.py
3. jarvis/dag/dag_manager.py
4. jarvis/dag/dependency_resolver.py
5. jarvis/dag/dag_validator.py
6. jarvis/api/routes/dags.py
7. Advanced scheduling tests
```

### Phase 5: Observability (Week 16-18)
```
1. jarvis/monitor/metrics_collector.py
2. jarvis/monitor/prometheus_exporter.py
3. jarvis/api/routes/metrics.py
4. Grafana dashboard configs
5. Alert rules configuration
```

### Phase 6+: Advanced Features (Week 19+)
```
Components marked [P3]:
1. jarvis/autoscaler/* (all files)
2. jarvis/auth/* (authentication/authorization)
3. Advanced failure handling
4. Multi-cluster support
```

---

## Module Dependencies Graph

```
Dependency Order (build/test order):
1. utils → exceptions → constants
2. state (memory backend) → config
3. scheduler (basic) → state
4. worker → scheduler communication
5. api → scheduler + state
6. monitor → scheduler + worker
7. dag → scheduler
8. autoscaler → monitor + scheduler
9. auth → api
```

---

## File Count by Component

| Component | Files | Functions (approx) | Priority |
|-----------|-------|-------------------|----------|
| API Server | 12 | 35 | P0 |
| Scheduler | 9 | 45 | P0-P2 |
| Worker | 4 | 20 | P0-P1 |
| State Management | 7 | 25 | P0-P2 |
| Monitoring | 4 | 20 | P1-P2 |
| DAG Workflow | 3 | 15 | P2 |
| Autoscaler | 3 | 12 | P3 |
| Auth | 2 | 8 | P2 |
| Error Handling | 2 | 8 | P0-P1 |
| Communication | 5 | 15 | P1 |
| Utils | 4 | 15 | P0 |
| CLI | 4 | 12 | P1-P2 |
| Tests | 15+ | 100+ | P0-P2 |
| **TOTAL** | **~74 files** | **~330 functions** | |

---

## Lines of Code Estimate

| Component | Estimated LOC |
|-----------|--------------|
| Core (API + Scheduler + Worker + State) | 8,000 |
| Monitoring + Observability | 2,000 |
| DAG + Advanced Scheduling | 1,500 |
| Autoscaling | 1,000 |
| Auth + Security | 1,500 |
| Utils + CLI | 1,500 |
| Tests | 10,000 |
| **TOTAL** | **~25,500 LOC** |

---

## Critical Path for MVP

The minimum viable product requires these files in order:

1. **Foundation (Week 1)**
   - Repository setup
   - Configuration management
   - Logging utilities
   - Exception definitions

2. **State Layer (Week 2)**
   - In-memory state manager
   - Task models
   - Basic persistence

3. **Scheduler Core (Week 3)**
   - Task queue (FIFO)
   - Resource matcher (simple)
   - Main scheduler loop

4. **Worker Core (Week 4)**
   - Node agent
   - Task executor (container support)
   - Status reporting

5. **API Layer (Week 5)**
   - HTTP server
   - Task submission endpoint
   - Task status endpoint
   - Health check endpoint

---

## Comparison Metrics

When comparing planned vs. actual implementation, track:

1. **File Completion**: Files present vs. files planned
2. **Function Completion**: Functions implemented vs. planned
3. **Phase Progress**: Current phase vs. planned phase
4. **Priority Adherence**: P0 complete before P1, etc.
5. **Dependency Satisfaction**: Dependencies met before dependent code
6. **Test Coverage**: Tests written for implemented code

---

**Document Status**: Living Document - Update as design evolves  
**Last Updated**: 2026-01-04  
**Version**: 1.0  
**Owner**: Development Team
