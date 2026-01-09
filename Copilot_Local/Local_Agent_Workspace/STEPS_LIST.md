# Jarvis v0.1 - Complete Steps List

**Test-Based Development**: All steps follow TDD — write tests FIRST, then implement.

---

## Overview

Jarvis v0.1 is built in 4 major steps, each with multiple sub-tasks. Each step is small, focused, and completely specified with 20-40 test cases.

---

## Step 1: Basic CLI

**Goal**: Build a command-line interface that accepts user input.

**What You'll Create**:
- `jarvis/cli.py` — Command loop (< 500 lines)
- `tests/test_step_1.py` — 4 test cases

**Tests to Write**:
- [ ] test_echo_command — Input echoed back
- [ ] test_exit_command — Exit command works
- [ ] test_empty_input — Handles empty input gracefully
- [ ] test_multiple_commands — Chain of commands works

**Deliverables**:
- Working CLI loop
- Echo functionality
- Graceful exit

**Estimated Time**: 1-2 hours

---

## Step 2: Graph, Nodes, Edges

**Goal**: Build the core data structure — graphs with nodes and edges.

**What You'll Create**:
- `jarvis/graph.py` — Node, Edge, Graph classes (< 500 lines)
- `tests/test_step_2.py` — 20+ test cases
- Updated `jarvis/cli.py` with graph commands

**Tests to Write**:
- [ ] test_node_creation — Create nodes with id/label
- [ ] test_node_equality — Nodes equal by id
- [ ] test_edge_creation — Create edges between nodes
- [ ] test_graph_add_node — Add nodes to graph
- [ ] test_graph_add_edge — Add edges to graph
- [ ] test_graph_remove_node — Remove node and connected edges
- [ ] test_graph_remove_edge — Remove edge
- [ ] test_graph_serialization — to_dict/from_dict
- [ ] test_save_graph — JSON save/load
- [ ] test_load_example_graphs — Load test graphs
- [ ] test_cli_graph_commands — create_node, create_edge, display, save, load

**Deliverables**:
- Graph classes (Node, Edge, Graph)
- JSON serialization
- CLI commands for graph manipulation
- Ability to save/load graphs

**Estimated Time**: 2-4 hours

---

## Step 3: Code Observation

**Goal**: Teach Jarvis to observe folder structure and Python functions.

**What You'll Create**:
- `jarvis/observers.py` — FolderObserver, PythonObserver classes (< 500 lines)
- `tests/test_step_3.py` — 20 test cases (folder observation)
- `tests/test_step_3_2.py` — 20 test cases (function observation)
- METADATA files for all observed folders/files

**3.1 - Folder Observation Tests**:
- [ ] test_observe_test_folder — Scan folder, create nodes
- [ ] test_folder_nodes_created — Folder nodes exist
- [ ] test_file_nodes_created — File nodes exist
- [ ] test_folder_to_subfolder_edges — Edges from parent to subfolders
- [ ] test_folder_to_file_edges — Edges from folder to files
- [ ] test_metadata_files_created — METADATA files created
- [ ] test_metadata_file_format — METADATA is valid JSON
- [ ] test_observation_save — Save observation as graph

**3.2 - Function Observation Tests**:
- [ ] test_observe_functions_simple — Extract functions from .py file
- [ ] test_function_extraction_names — All functions found
- [ ] test_function_extraction_line_numbers — Line numbers captured
- [ ] test_python_observer_empty_file — Empty file handled
- [ ] test_python_observer_syntax_error — Syntax errors handled gracefully
- [ ] test_observe_with_python_files — Function nodes created
- [ ] test_function_node_creation — Function node IDs correct
- [ ] test_function_metadata_format — Function metadata correct
- [ ] test_file_metadata_updated — File METADATA includes function list

**Deliverables**:
- FolderObserver class (1 level deep scanning)
- PythonObserver class (AST-based function extraction)
- METADATA files (.metadata.json) for all folders/files
- CLI `observe` command
- Graph saving to observation.json

**Estimated Time**: 4-6 hours

---

## Step 4: Execution Engine

**Goal**: Enable Jarvis to execute chains of functions.

**What You'll Create**:
- `jarvis/test_functions.py` — 5 utility functions (< 500 lines)
- `jarvis/execution.py` — ExecutionEngine class (< 500 lines)
- `tests/test_step_4_1.py` — 18 test cases (functions)
- `tests/test_step_4_2.py` — 20+ test cases (execution)
- Updated `jarvis/cli.py` with `run` command

**4.1 - Test Functions Tests**:
- [ ] test_add_basic — add(2, 3) → 5
- [ ] test_add_floats — add(2.5, 3.5) → 6.0
- [ ] test_multiply_basic — multiply(4, 5) → 20
- [ ] test_concat_basic — concat("hello", "world") → "helloworld"
- [ ] test_uppercase_basic — uppercase("jarvis") → "JARVIS"
- [ ] test_length_basic — length("hello") → 5
- [ ] test_function_signatures — All functions have type hints

**4.2 - Execution Engine Tests**:
- [ ] test_execution_engine_simple_add — Execute single function
- [ ] test_execution_engine_two_step_chain — Execute add → multiply
- [ ] test_execution_engine_three_step_chain — Execute longer chains
- [ ] test_execution_engine_string_chain — concat → uppercase
- [ ] test_execution_engine_load_graph — Load and execute graph
- [ ] test_execution_engine_missing_start_node — Error handling
- [ ] test_execution_engine_missing_function — Function lookup errors
- [ ] test_correct_input_passing — Outputs passed to next function
- [ ] test_cli_run_command — CLI `run` command works

**Deliverables**:
- 5 test functions (add, multiply, concat, uppercase, length)
- ExecutionEngine class (function lookup, chaining, execution)
- CLI `run` command
- Function chain execution via graph

**Estimated Time**: 3-4 hours

---

## Summary

| Step | File | Classes/Functions | Tests | Time |
|------|------|------------------|-------|------|
| 1 | `cli.py` | 1 (CLI) | 4 | 1-2h |
| 2 | `graph.py` | 3 (Node, Edge, Graph) | 20+ | 2-4h |
| 3 | `observers.py` | 2 (Folder, Python) | 40+ | 4-6h |
| 4 | `test_functions.py` + `execution.py` | 5 funcs + 1 class | 40+ | 3-4h |

**Total Estimated Time**: 10-16 hours

**Total Test Cases**: 100+

---

## Key Principles

✅ **TDD (Test-Driven Development)**
- Write tests FIRST
- Implementation comes after
- All tests must pass

✅ **Minimal Code**
- Keep each file < 500 lines
- Focus on essentials
- No extra features

✅ **Python Stdlib Only**
- No external dependencies
- Use built-in modules
- No pip installs needed

✅ **Small, Focused Steps**
- Each step is independent
- Clear deliverables
- Complete specifications

---

## v0.2: Integration & Graph as Database

**Focus**: Everything works TOGETHER. Graph is the central database. Metadata enriches the graph.

### Step 5: Folder Tree → Graph Conversion

**Goal**: Integrate FolderObserver output INTO the Graph. Graph becomes the single source of truth.

**What You'll Create**:
- `jarvis/converters.py` — FolderToGraphConverter class (< 300 lines)
- `tests/test_step_5.py` — 20+ test cases
- Enhanced `jarvis/cli.py` with `observe folder` command

**Tests to Write**:
- [ ] test_converter_single_folder — One folder → graph nodes
- [ ] test_converter_subfolder_hierarchy — Nested folders → parent/child edges
- [ ] test_converter_files_in_folder — Files → nodes
- [ ] test_converter_folder_to_file_edges — Edges folder→file
- [ ] test_converter_complete_tree — Full tree structure preserved
- [ ] test_converter_metadata_nodes — METADATA files → nodes too
- [ ] test_graph_folder_ids — Node IDs use folder paths
- [ ] test_graph_serialization_consistency — Save/load preserves structure
- [ ] test_cli_observe_folder — `observe <path>` creates graph
- [ ] test_observe_update_graph — Updating existing graph works
- [ ] test_large_folder_tree — 100+ files/folders handled
- [ ] test_folder_with_symlinks — Symlinks handled (skip them)
- [ ] test_permission_errors_graceful — Missing permissions handled

**Deliverables**:
- FolderToGraphConverter class
- Folder tree fully represented in Graph
- CLI `observe folder <path>` command
- Graph as central storage for folder structure

**Estimated Time**: 2-3 hours

---

### Step 6: Function Scraper → Graph Conversion

**Goal**: Integrate PythonObserver output INTO the Graph. Functions now queryable via graph.

**What You'll Create**:
- `jarvis/converters.py` expanded — FunctionToGraphConverter class
- `tests/test_step_6.py` — 25+ test cases
- Enhanced `jarvis/cli.py` with `observe functions` command

**Tests to Write**:
- [ ] test_converter_single_function — Function → graph node
- [ ] test_converter_function_metadata — Function details stored
- [ ] test_converter_line_numbers — Line numbers captured
- [ ] test_converter_file_to_function_edges — Edges file→function
- [ ] test_converter_multiple_functions — Multiple functions → multiple nodes
- [ ] test_converter_function_signatures — Parameters + return types stored
- [ ] test_converter_function_dependencies — Function calls → edges
- [ ] test_graph_function_lookup — Find all functions in file
- [ ] test_graph_function_query — Query function by name across repo
- [ ] test_cli_observe_functions — `observe functions <path>` works
- [ ] test_observe_update_existing_functions — Re-observing updates nodes
- [ ] test_large_codebase_100_functions — 100+ functions handled
- [ ] test_complex_function_signatures — Type hints, *args, **kwargs handled
- [ ] test_syntax_error_file_recovery — One bad file doesn't break rest
- [ ] test_graph_interop_folders_and_functions — Both in same graph

**Deliverables**:
- FunctionToGraphConverter class
- Functions represented as graph nodes
- Function metadata (signature, line numbers, calls)
- CLI `observe functions <path>` command
- Graph now contains both folder structure AND functions

**Estimated Time**: 2-4 hours

---

### Step 7: Metadata Files & Manager

**Goal**: Create metadata files BY HAND, create manager to handle them, attach to graph.

**What You'll Create**:
- `jarvis/metadata_manager.py` — MetadataManager class (< 400 lines)
- `tests/test_step_7.py` — 25+ test cases
- Example METADATA files (created by hand during tests)
- Enhanced `jarvis/cli.py` with `metadata` commands

**Tests to Write**:
- [ ] test_metadata_file_format — METADATA.json structure correct
- [ ] test_metadata_file_load — Load existing METADATA file
- [ ] test_metadata_file_save — Save METADATA file
- [ ] test_metadata_node_description — Add description to node
- [ ] test_metadata_node_tags — Add tags/labels to node
- [ ] test_metadata_node_owner — Add ownership info
- [ ] test_metadata_node_status — Add status (planned, done, deprecated)
- [ ] test_metadata_inheritance — Child nodes inherit parent metadata
- [ ] test_metadata_file_folder_metadata — METADATA for folders
- [ ] test_metadata_file_function_metadata — METADATA for functions
- [ ] test_metadata_graph_integration — Metadata attached to graph nodes
- [ ] test_metadata_query — Query nodes by tag/status/owner
- [ ] test_metadata_bulk_update — Update multiple nodes at once
- [ ] test_metadata_merge_files — Combine METADATA from multiple files
- [ ] test_cli_metadata_show — Show metadata for node
- [ ] test_cli_metadata_edit — Edit metadata via CLI
- [ ] test_metadata_validation — Invalid metadata rejected
- [ ] test_metadata_conflicts — Conflicting metadata handled

**Example Metadata Files** (created by hand):
- `jarvis/.metadata.json` — Module description, version, author
- `jarvis/graph.py.metadata.json` — File overview, key functions
- `tests/.metadata.json` — Test structure, coverage notes

**Deliverables**:
- MetadataManager class (load, save, query, merge)
- METADATA.json file format specification
- 3+ example METADATA files created by hand
- CLI `metadata` commands
- Metadata enriches graph queries

**Estimated Time**: 2-3 hours

---

### Step 8: Integration Layer (Combine Everything)

**Goal**: Everything works together. Single workflow: CLI → observe → graph → execute.

**What You'll Create**:
- `jarvis/integration.py` — JarvisWorkflow class (< 400 lines)
- `tests/test_step_8.py` — 30+ test cases
- Enhanced `jarvis/cli.py` with end-to-end commands

**Tests to Write**:
- [ ] test_workflow_observe_folders_and_functions — Single `observe` scans both
- [ ] test_workflow_metadata_attached — Observed data includes metadata
- [ ] test_workflow_graph_central_database — Graph has all data
- [ ] test_workflow_query_folder_structure — Query folders via graph
- [ ] test_workflow_query_functions_by_tag — Find functions by metadata tag
- [ ] test_workflow_query_functions_by_file — Find functions in specific file
- [ ] test_workflow_query_by_owner — Find nodes owned by person
- [ ] test_workflow_query_by_status — Find deprecated/planned functions
- [ ] test_workflow_execution_chain_function_lookup — Execute functions found via observation
- [ ] test_workflow_execution_with_metadata — Execute with metadata context
- [ ] test_workflow_execution_error_recovery — Execution handles missing functions
- [ ] test_workflow_full_cycle_single_command — `analyze <path>` does everything
- [ ] test_workflow_persistence — Save/load full state
- [ ] test_workflow_incremental_update — Re-run observe on modified code
- [ ] test_workflow_large_project — 200+ files, 500+ functions
- [ ] test_cli_analyze_command — Single `analyze` command works
- [ ] test_cli_query_command — Query graph via CLI
- [ ] test_cli_execute_command — Execute via graph via CLI

**Core Workflow** (everything integrated):
1. User: `jarvis analyze <path>`
2. Jarvis: Observe folder structure → Graph
3. Jarvis: Observe functions → Graph
4. Jarvis: Load METADATA files → Enrich Graph
5. Jarvis: Show summary of what was found
6. User: Query graph, execute functions, explore metadata

**Deliverables**:
- JarvisWorkflow class
- `analyze` CLI command (end-to-end observation)
- `query` CLI command (graph queries)
- `execute` CLI command (from graph)
- All v0.1 + v0.2 modules working together
- Single source of truth: the Graph

**Estimated Time**: 3-4 hours

---

### Step 9: Full Interoperability Tests

**Goal**: Comprehensive testing. Everything works together. No edge cases left behind.

**What You'll Create**:
- `tests/test_step_9_interop.py` — 50+ integration tests
- `tests/fixtures/` — Test projects (small, medium, large)
- Integration test report

**Tests to Write** (High-level integration):
- [ ] test_full_cycle_small_project — Small repo (10 files, 20 functions)
- [ ] test_full_cycle_medium_project — Medium repo (50 files, 100 functions)
- [ ] test_full_cycle_large_project — Large repo (200 files, 500+ functions)
- [ ] test_graph_consistency_after_observe — Graph integrity
- [ ] test_metadata_consistency_all_files — All nodes have metadata
- [ ] test_execution_finds_all_functions — All functions discoverable
- [ ] test_query_performance_large_graph — Queries < 100ms on large data
- [ ] test_circular_dependencies_handled — Cycles don't crash
- [ ] test_missing_files_graceful — Deleted files handled gracefully
- [ ] test_modified_code_reobservation — Code changes detected
- [ ] test_concurrent_metadata_writes — Thread safety (if applicable)
- [ ] test_export_graph_all_formats — Save to JSON, dict, etc.
- [ ] test_import_external_graph — Load third-party graph format
- [ ] test_command_chain_scenario_1 — Realistic workflow 1
- [ ] test_command_chain_scenario_2 — Realistic workflow 2
- [ ] test_error_recovery_all_components — All errors recoverable
- [ ] test_performance_large_repo_1000_functions — Scalability test
- [ ] test_metadata_overrides_work — Local metadata > defaults

**Real-World Scenarios** (as tests):
- Scenario 1: "Analyze Flask project" (observe → metadata → query → execute)
- Scenario 2: "Find all deprecated functions" (metadata query + report)
- Scenario 3: "Execute function chain from repo" (discover → load → execute)
- Scenario 4: "Update project structure" (re-observe → merge graphs → report changes)

**Deliverables**:
- 50+ comprehensive interoperability tests
- Test fixtures (small, medium, large projects)
- Performance benchmarks
- Confidence that all components work together

**Estimated Time**: 4-5 hours

---

## v0.2 Summary

| Step | Focus | Classes/Functions | Tests | Time |
|------|-------|------------------|-------|------|
| 5 | Folder → Graph | FolderToGraphConverter | 13+ | 2-3h |
| 6 | Functions → Graph | FunctionToGraphConverter | 15+ | 2-4h |
| 7 | Metadata Manager | MetadataManager | 18+ | 2-3h |
| 8 | Integration Layer | JarvisWorkflow | 18+ | 3-4h |
| 9 | Interop Tests | (test fixtures) | 50+ | 4-5h |

**Total Estimated Time**: 13-19 hours

**Total Test Cases**: 114+

**Key Achievement**: Graph is the central database. Everything works together.

---

## v0.3: Query, Analysis & Reporting (Future)

Once v0.2 is done, consider:
- Advanced graph queries (find patterns, dependencies)
- Code analysis (complexity, test coverage)
- Reporting (HTML reports, metrics)
- Visualization (graph diagrams, dependency trees)
- Workflow planning (execution order, optimization)

But v0.2 first: **get everything working together.**

---

## Development Workflow (v0.1 + v0.2)

1. **Choose a step** from the list above
2. **Write tests first** (all test cases listed)
3. **Implement code** to pass tests
4. **Document in Agent_Workspace** what you learned
5. **Confirm all tests pass**
6. **Move to next step**

Each step builds on previous. No skipping. Tests ensure nothing breaks.

---

## Key Principles (Still Apply)

✅ **TDD (Test-Driven Development)**
- Write tests FIRST
- Implementation comes after
- All tests must pass

✅ **Integration Focus** (NEW for v0.2)
- Every step combines with existing code
- Graph is the central database
- No isolated features

✅ **Metadata Everywhere** (NEW for v0.2)
- Metadata enriches graph data
- Makes nodes queryable and useful
- Example METADATA files created by hand

✅ **Minimal Code**
- Keep each file < 400-500 lines
- Focus on essentials
- No extra features

✅ **Python Stdlib Only**
- No external dependencies
- Use built-in modules
- No pip installs needed

---

## Progress Tracking

**v0.1 Completion** (Steps 1-4):
- ✅ Step 1: CLI
- ✅ Step 2: Graph
- ✅ Step 3: Observation (folders + functions)
- ✅ Step 4: Execution

**v0.2 Planning** (Steps 5-9):
- ⏳ Step 5: Folder → Graph (ready to start)
- ⏳ Step 6: Functions → Graph
- ⏳ Step 7: Metadata Manager
- ⏳ Step 8: Integration Layer
- ⏳ Step 9: Full Interop Tests

**v0.3 Planning** (Future):
- ⏹️ Advanced queries
- ⏹️ Analysis & reporting
- ⏹️ Visualization

---

## For Developers

When starting Step 5+, remember:
1. **Everything goes INTO the Graph** — no isolated data structures
2. **Metadata is key** — create example METADATA files by hand first
3. **Tests test integration** — not just individual features
4. **Graph remains central** — all modules read/write via graph
5. **Combine before creating** — integrate before adding new features
