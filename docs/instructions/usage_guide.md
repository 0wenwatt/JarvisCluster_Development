# Agent Instructions - Usage Guide

## Purpose

This guide provides instructions for AI agents and developers on how to effectively use the JarvisCluster_Development repository for collaborative development.

## For AI Agents

### Repository Overview

This repository serves as the central planning and tracking hub for the Jarvis cluster management system. It contains:

- **Design documents** - High-level architecture and system design
- **Development plans** - Roadmaps, requirements, and phase definitions
- **File structure blueprint** - Complete desired implementation structure
- **Tracking data** - Automated snapshots and progress metrics
- **Templates and placeholders** - Standard formats for consistency

### Key Documents to Review

1. **[DESIGN_PLAN.md](../../DESIGN_PLAN.md)** - Start here to understand system architecture
2. **[JARVIS_FILE_TREE.md](../../JARVIS_FILE_TREE.md)** - Complete implementation blueprint with priorities
3. **[USE_CASES.md](../../USE_CASES.md)** - Concrete examples of component interactions
4. **[REQUIREMENTS.md](../../REQUIREMENTS.md)** - Coding standards and quality requirements
5. **[ROADMAP.md](../../ROADMAP.md)** - Development phases and timeline
6. **[DEV_STATE.md](../../DEV_STATE.md)** - Current progress and status

### How to Use This Repository

#### When Planning Development

1. **Understand the architecture** by reading DESIGN_PLAN.md
2. **Identify current phase** from ROADMAP.md and DEV_STATE.md
3. **Find what to build next** using priority markers (P0, P1, P2, P3) in JARVIS_FILE_TREE.md
4. **Review use cases** in USE_CASES.md for context on component interactions

#### When Implementing Features

1. **Follow the file structure** exactly as specified in JARVIS_FILE_TREE.md
2. **Implement functions** listed for each file in the tree
3. **Use priority order**: P0 (MVP) → P1 (Core) → P2 (Advanced) → P3 (Future)
4. **Adhere to standards** defined in REQUIREMENTS.md

#### When Updating Progress

1. **Update DEV_STATE.md** with completed components
2. **Run comparison tools** (scripts/compare_tree.py) to track progress
3. **Document decisions** in docs/decisions/ using ADR format
4. **Log significant events** in logs/ directory

### Directory Structure for Agents

```
JarvisCluster_Development/
├── docs/
│   ├── instructions/        ← This directory: How to use the repo
│   ├── knowledge_base/      ← Architecture summaries and key decisions
│   ├── architecture/        ← Detailed architecture documentation
│   ├── decisions/           ← Architectural Decision Records (ADRs)
│   ├── examples/            ← Example configurations and use cases
│   └── guides/              ← How-to guides and tutorials
├── assets/                  ← Diagrams, images, visual aids
├── logs/                    ← Development logs and session records
├── src/                     ← Code examples and prototypes (not main implementation)
├── scripts/                 ← Utility scripts for comparison and tracking
├── tracking/                ← Auto-generated progress tracking data
└── config/                  ← Configuration files
```

### Best Practices for Agents

#### 1. Always Check Current State First
```bash
# Before making suggestions, review:
cat DEV_STATE.md          # Current progress
cat ROADMAP.md            # Current phase
grep "[P0]" JARVIS_FILE_TREE.md  # Priority 0 items
```

#### 2. Maintain Consistency
- Use the exact file names and structure from JARVIS_FILE_TREE.md
- Follow coding standards in REQUIREMENTS.md
- Keep documentation up to date

#### 3. Prioritize Correctly
- Focus on P0 items before P1
- Complete entire modules before moving to next
- Don't skip ahead to advanced features

#### 4. Document Decisions
When making architectural decisions, create an ADR:
```bash
# Location: docs/decisions/ADR-NNNN-title.md
# Use template from docs/decisions/ADR-0000-use-adrs.md
```

#### 5. Track Progress
Update DEV_STATE.md after significant changes:
- Completed components
- Blocked items
- Next steps
- Known issues

### Working with the Tracking System

The repository includes automated tracking tools in the `scripts/` directory:

#### compare_tree.py
Compares actual implementation against JARVIS_FILE_TREE.md
```bash
python3 scripts/compare_tree.py \
  --desired JARVIS_FILE_TREE.md \
  --actual /path/to/jarvis \
  --output tracking/reports
```

**Use this to:**
- Check completion percentage
- Identify missing files
- Verify implementation order
- Get recommendations for next steps

#### visualize_tree.py
Creates visual representations of progress
```bash
python3 scripts/visualize_tree.py \
  --input tracking/reports/tree_comparison.json \
  --output-html tracking/reports/tree_visual.html
```

**Use this to:**
- Generate interactive HTML views
- Create ASCII tree diagrams
- Filter by priority level
- Search for specific components

### Common Agent Tasks

#### Task: Suggesting Next Implementation Step
1. Check current phase in DEV_STATE.md
2. Find incomplete P0 or P1 items in JARVIS_FILE_TREE.md
3. Review related use cases in USE_CASES.md
4. Suggest specific file and functions to implement
5. Reference coding standards from REQUIREMENTS.md

#### Task: Reviewing Code Structure
1. Compare against JARVIS_FILE_TREE.md
2. Verify priority order is followed
3. Check for missing required functions
4. Validate against REQUIREMENTS.md standards

#### Task: Updating Documentation
1. Update DEV_STATE.md with progress
2. Create ADRs for significant decisions
3. Add examples to docs/examples/ if helpful
4. Update logs/ with development notes

#### Task: Analyzing Progress
1. Run compare_tree.py
2. Review completion percentages
3. Identify bottlenecks or missing dependencies
4. Suggest priority adjustments if needed

### Integration with Other Systems

This repository is designed to integrate with:

1. **Implementation Repository** - Actual Jarvis codebase (separate repo)
2. **Tracking Software** - Automated progress monitoring
3. **CI/CD Pipelines** - Validation and testing
4. **Documentation Sites** - Published documentation

### Templates Available

- **ADR Template**: docs/decisions/ADR-0000-use-adrs.md
- **Report Template**: tracking/templates/report-template.md
- **README Templates**: Throughout docs/ subdirectories

### Getting Help

- **Architecture Questions**: Review DESIGN_PLAN.md and docs/knowledge_base/
- **Implementation Details**: Check JARVIS_FILE_TREE.md and USE_CASES.md
- **Standards Questions**: Consult REQUIREMENTS.md
- **Progress Questions**: Check DEV_STATE.md and tracking/reports/

## For Human Developers

See the main [USAGE_GUIDE.md](../../USAGE_GUIDE.md) in the repository root for detailed developer workflow instructions.

## Quick Reference

### Essential Files by Purpose

| Purpose | File | Description |
|---------|------|-------------|
| Architecture | DESIGN_PLAN.md | System design and components |
| Implementation | JARVIS_FILE_TREE.md | Complete file structure with priorities |
| Examples | USE_CASES.md | Real-world usage scenarios |
| Standards | REQUIREMENTS.md | Coding and quality standards |
| Timeline | ROADMAP.md | Development phases |
| Progress | DEV_STATE.md | Current status |
| Tracking | tracking/reports/ | Automated progress reports |

### Priority Levels

- **P0**: MVP Critical - Must have for basic functionality
- **P1**: Core Features - Essential for production use
- **P2**: Advanced Features - Enhanced functionality
- **P3**: Future Features - Nice-to-have additions

### Phase Overview

- **Phase 0**: Foundation and Planning
- **Phase 1**: MVP - Single Node Scheduler
- **Phase 2**: Multi-Node Support
- **Phase 3**: State Persistence
- **Phase 4-5**: Advanced Features
- **Phase 6-9**: Production Hardening

---

**Last Updated**: 2026-01-08
**Repository Version**: 1.0
