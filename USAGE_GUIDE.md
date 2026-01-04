# Jarvis Development - Usage Guide

## Overview

This guide explains how to use the JarvisCluster_Development repository to plan, track, and manage Jarvis development.

---

## Understanding the Repository Structure

### Design Documents (High-Level → Detailed)

1. **DESIGN_PLAN.md** - System architecture
   - Components and their responsibilities
   - Technology stack decisions
   - Design principles

2. **USE_CASES.md** - Real-world scenarios
   - Concrete examples of system usage
   - Component interaction flows
   - Decision logic and algorithms

3. **JARVIS_FILE_TREE.md** - Implementation blueprint
   - Complete file and directory structure
   - All Python files with their purpose
   - All functions within each file
   - Development priorities (P0-P3)
   - Estimated lines of code

4. **REQUIREMENTS.md** - Development standards
   - Coding conventions
   - Testing requirements
   - Quality gates

5. **ROADMAP.md** - Timeline and phases
   - 9 development phases
   - Week-by-week breakdown
   - Milestones and deliverables

6. **DEV_STATE.md** - Current progress
   - Component completion status
   - Blockers and issues
   - Next steps

---

## Development Workflow

### Phase 1: Planning (Before Coding)

1. **Review the Design**
   ```bash
   # Read these in order
   cat DESIGN_PLAN.md
   cat USE_CASES.md
   cat JARVIS_FILE_TREE.md
   ```

2. **Understand Your Current Phase**
   ```bash
   # Check the roadmap
   cat ROADMAP.md
   
   # Check current state
   cat DEV_STATE.md
   ```

3. **Identify What to Build**
   - Look at JARVIS_FILE_TREE.md
   - Find files marked with your current priority (e.g., [P0])
   - Note the functions you need to implement

### Phase 2: Development (While Coding)

1. **Follow the File Tree Structure**
   - Create files exactly as specified in JARVIS_FILE_TREE.md
   - Implement functions listed for each file
   - Use priorities to determine order (P0 → P1 → P2 → P3)

2. **Example: Building the Scheduler**
   ```
   From JARVIS_FILE_TREE.md:
   
   jarvis/scheduler/
   ├── scheduler.py [P0]
   │   └── Functions:
   │       ├── start() [P0]
   │       ├── stop() [P0]
   │       ├── schedule_task() [P0]
   │       └── process_queue() [P0]
   │
   ├── task_queue.py [P0]
   │   └── Functions:
   │       ├── enqueue() [P0]
   │       ├── dequeue() [P0]
   │       ├── peek() [P0]
   │       └── size() [P0]
   ```
   
   Create these files and implement these functions.

3. **Update Progress**
   - After completing a component, update DEV_STATE.md
   - Check off completed items in ROADMAP.md

### Phase 3: Tracking (Continuous)

1. **Run Automatic Tracking**
   ```bash
   # Your tracking script (which you write) will:
   # 1. Clone/pull the Jarvis implementation repo
   # 2. Analyze its structure
   # 3. Save a snapshot to tracking/snapshots/
   # 4. Generate metrics in tracking/metrics/
   ```

2. **Compare Against Plan**
   ```bash
   # Run the comparison tool
   python3 scripts/compare_tree.py \
     --desired JARVIS_FILE_TREE.md \
     --actual /path/to/jarvis/repo \
     --output tracking/reports
   
   # View the report
   cat tracking/reports/tree_comparison.md
   ```

3. **Visualize Progress**
   ```bash
   # Generate visual tree
   python3 scripts/visualize_tree.py \
     --input tracking/reports/tree_comparison.json \
     --output-html tracking/reports/tree_visual.html
   
   # Open in browser
   open tracking/reports/tree_visual.html
   ```

---

## Using the Comparison Tools

### compare_tree.py

**Purpose**: Compare your actual implementation against the desired structure.

**What it checks**:
- Which files exist vs. planned
- Completion by priority level (P0, P1, P2, P3)
- Missing critical files
- Extra files not in the plan

**Example output**:
```
Overall Completion: 45.3%

By Priority:
  P0: 87.0% (47/54)  ← MVP is mostly done!
  P1: 34.1% (14/41)  ← Working on core features
  P2: 10.7% (3/28)   ← Advanced features pending
  P3: 0.0% (0/4)     ← Future features
```

**Recommendations**:
- If P0 < 100%, focus there first
- Don't start P2 until P1 is largely complete
- Use missing files list to prioritize work

### visualize_tree.py

**Purpose**: Create visual representations of the file tree.

**Features**:
- **ASCII Tree**: Simple text visualization
  ```
  jarvis/
  └── ✓ api/ [P0]
      ├── ✓ __init__.py [P0]
      ├── ✓ server.py [P0]
      └── ✗ routes/ [P0]
          └── ✗ tasks.py [P0]
  ```
  ✓ = implemented, ✗ = missing

- **HTML Interactive View**:
  - Collapsible tree structure
  - Color-coded priorities
  - Filter by priority or status
  - Search for specific files
  - Real-time statistics

---

## Priority System Explained

### P0 - MVP Critical (Phase 1)
**Goal**: Get basic functionality working

**Example files**:
- `api/server.py` - API server
- `scheduler/task_queue.py` - Task queuing
- `scheduler/scheduler.py` - Basic scheduler
- `worker/task_executor.py` - Execute tasks
- `state/state_manager.py` - In-memory state

**When to build**: Week 3-5 (Phase 1)

**Milestone**: Can submit a task via API and execute it on a single node

### P1 - Core Features (Phase 2-3)
**Goal**: Production-ready core system

**Example files**:
- `state/node_registry.py` - Track multiple nodes
- `monitor/heartbeat_monitor.py` - Node health
- `scheduler/load_balancer.py` - Distribute tasks
- `worker/resource_monitor.py` - Resource tracking

**When to build**: Week 6-11 (Phases 2-3)

**Milestone**: Multi-node cluster with persistence and monitoring

### P2 - Advanced Features (Phase 4-5)
**Goal**: Enhanced functionality

**Example files**:
- `scheduler/priority_queue.py` - Priority scheduling
- `dag/dag_manager.py` - Workflow dependencies
- `monitor/metrics_collector.py` - Observability
- `api/routes/metrics.py` - Metrics API

**When to build**: Week 12-18 (Phases 4-5)

**Milestone**: Advanced scheduling, DAGs, full observability

### P3 - Future Features (Phase 6+)
**Goal**: Nice-to-have features

**Example files**:
- `autoscaler/` - Auto-scaling
- `auth/` - Authentication/authorization
- Multi-cluster support

**When to build**: Week 19+ (Phase 6-9)

**Milestone**: Production polish and advanced features

---

## Best Practices

### 1. Follow the Order

**Do this**:
```
Phase 1 (P0): Complete task queue → scheduler → worker → API
Phase 2 (P1): Add multi-node → monitoring → persistence
Phase 3 (P1): Complete persistence layer
...
```

**Don't do this**:
```
❌ Start with autoscaling (P3) before basic scheduling (P0)
❌ Implement DAGs (P2) before multi-node support (P1)
❌ Build auth (P2) before core API (P0)
```

### 2. Implement All Functions in a File

When you create a file, implement all the functions listed for it in JARVIS_FILE_TREE.md.

**Example**: If you create `scheduler/task_queue.py`, implement:
- `enqueue()`
- `dequeue()`
- `peek()`
- `size()`
- `clear()`

### 3. Track Progress Regularly

```bash
# After each component
python3 scripts/compare_tree.py --actual /path/to/jarvis --output tracking/reports

# Review recommendations
cat tracking/reports/tree_comparison.md

# Update DEV_STATE.md
vim DEV_STATE.md
```

### 4. Use the File Tree as Your Checklist

Print out JARVIS_FILE_TREE.md and check off each file/function as you complete it.

---

## Common Workflows

### Workflow 1: Starting a New Phase

```bash
# 1. Review phase goals
cat ROADMAP.md | grep "Phase X"

# 2. Find files for this phase
cat JARVIS_FILE_TREE.md | grep "\[P0\]"  # or P1, P2, P3

# 3. Create first file
mkdir -p jarvis/scheduler
touch jarvis/scheduler/scheduler.py

# 4. Implement functions (see JARVIS_FILE_TREE.md)
vim jarvis/scheduler/scheduler.py

# 5. Test
python -m pytest tests/unit/test_scheduler.py

# 6. Check progress
python3 scripts/compare_tree.py
```

### Workflow 2: Weekly Status Check

```bash
# 1. Run comparison
python3 scripts/compare_tree.py

# 2. Generate visualization
python3 scripts/visualize_tree.py

# 3. Review reports
open tracking/reports/tree_visual.html

# 4. Update DEV_STATE.md with progress
vim DEV_STATE.md

# 5. Commit updates
git add DEV_STATE.md tracking/
git commit -m "Weekly progress update"
```

### Workflow 3: Checking What to Build Next

```bash
# 1. Check current completion
python3 scripts/compare_tree.py

# 2. View missing files sorted by priority
cat tracking/reports/tree_comparison.md | grep "Missing Files"

# 3. Pick the highest priority missing file
# 4. Find it in JARVIS_FILE_TREE.md to see required functions
# 5. Implement it
```

---

## Integration with Your Tracking Software

Your automatic tracking software should:

1. **Run periodically** (e.g., daily via cron)
2. **Snapshot the implementation repo** to `tracking/snapshots/`
3. **Run the comparison tool** to generate reports
4. **Store metrics over time** in `tracking/metrics/`
5. **Generate visualizations** for dashboards

Example cron entry:
```cron
# Run daily at midnight
0 0 * * * /path/to/your-tracking-script.sh
```

Your tracking script should:
```bash
#!/bin/bash
cd /path/to/JarvisCluster_Development

# Pull latest from implementation repo
git -C /path/to/jarvis pull

# Run comparison
python3 scripts/compare_tree.py \
  --actual /path/to/jarvis \
  --output tracking/reports

# Generate visualization
python3 scripts/visualize_tree.py

# Commit tracking data
git add tracking/
git commit -m "Auto-update: $(date)"
git push
```

---

## Troubleshooting

### Issue: Comparison shows 0% completion

**Cause**: Path to implementation repo is wrong

**Solution**:
```bash
# Check the path exists
ls /path/to/jarvis

# Use absolute path
python3 scripts/compare_tree.py --actual /absolute/path/to/jarvis
```

### Issue: Missing files not shown correctly

**Cause**: File tree markdown format changed

**Solution**: Ensure JARVIS_FILE_TREE.md uses the exact format:
```
├── filename.py [P0]
└── other.py [P1]
```

### Issue: Functions not detected

**Cause**: Python file doesn't use standard def syntax

**Solution**: Use standard function definitions:
```python
def function_name():  # ✓ Detected
    pass

function = lambda: None  # ✗ Not detected
```

---

## Quick Reference

### Essential Commands

```bash
# Compare implementation to plan
python3 scripts/compare_tree.py --actual /path/to/jarvis

# Generate visualization
python3 scripts/visualize_tree.py

# View current phase
grep "Current Phase" DEV_STATE.md

# List P0 files
grep "\[P0\]" JARVIS_FILE_TREE.md
```

### Essential Files

- **JARVIS_FILE_TREE.md** - Your implementation checklist
- **USE_CASES.md** - How components work together
- **DEV_STATE.md** - Current progress
- **tree_comparison.md** - Latest comparison report

### Directory Layout

```
JarvisCluster_Development/
├── JARVIS_FILE_TREE.md     ← Your blueprint
├── USE_CASES.md             ← Component interactions
├── DEV_STATE.md             ← Track progress here
├── scripts/
│   ├── compare_tree.py      ← Run this often
│   └── visualize_tree.py    ← Create visuals
└── tracking/
    └── reports/
        ├── tree_comparison.md    ← Read this
        └── tree_visual.html      ← View this
```

---

## Next Steps

1. **Read the design documents** in order
2. **Understand the file tree structure** (JARVIS_FILE_TREE.md)
3. **Start implementing P0 files** following the tree
4. **Run comparisons regularly** to track progress
5. **Update DEV_STATE.md** with your progress

---

**Need help?** Check USE_CASES.md for examples of how components interact.

**Lost track?** Run `python3 scripts/compare_tree.py` to see where you are.

**Ready to code?** Start with P0 files from JARVIS_FILE_TREE.md.
