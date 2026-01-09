# Configuration System

**Job generation from reusable snippets, roles, and context.**

---

## Overview

Instead of writing new job instructions from scratch each time, this system:

1. **Defines snippets** - Small, focused instruction pieces
2. **Configures roles** - What snippets go with each role
3. **Takes context** - Information specific to the job
4. **Generates job** - Combines snippets + context into complete instruction

---

## Files in This System

### Configuration Files

| File | Purpose | Type |
|------|---------|------|
| `snippets.yml` | Database of all snippets and their metadata | YAML |
| `roles.yml` | Role definitions and snippet assignments | YAML |
| `job_generator.py` | Python script to generate jobs | Python |

### Example Context Files

| File | Purpose | Use |
|------|---------|-----|
| `context_examples/context_step14_coder.json` | Example for Coder job | Reference |
| `context_examples/context_step14_designer.json` | Example for Designer job | Reference |
| `context_examples/context_step14_maintainer.json` | Example for Maintainer job | Reference |

---

## How It Works

### 1. snippets.yml - The Snippet Database

Defines all available snippets:

```yaml
designer:
  SCOPE.md:
    category: role
    description: What Designer does
    path: roles/designer/SCOPE.md
    applies_to: [designer]
    always_include: true  # Always in designer jobs
    
  DESIGN_PROCESS.md:
    category: process
    description: How to design
    path: roles/designer/DESIGN_PROCESS.md
    applies_to: [designer]
    always_include: true
    
  FILESYSTEM_RULES.md:
    category: standards
    description: File organization
    path: roles/designer/FILESYSTEM_RULES.md
    applies_to: [designer]
    always_include: false  # Optional
    context_dependent: true
    context_triggers: [file_organization_check]  # Include if context.file_organization_check=true
```

### 2. roles.yml - Role Configuration

Groups snippets by role:

```yaml
roles:
  coder:
    title: Coder
    always_include:
      - shared/AGENT_WORKSPACE.md
      - shared/LOGGING_STANDARDS.md
      - coder/SCOPE.md
      - coder/TDD_WORKFLOW.md
    optional:
      - coder/ENVIRONMENT_SETUP.md  # If context.fresh_environment=true
```

### 3. job_generator.py - The Generator

Python script that combines snippets + context:

```bash
# Generate Coder job for Step 14
python job_generator.py \
  --role coder \
  --step 14 \
  --title "Implement Clustering Algorithm" \
  --context context_examples/context_step14_coder.json

# Result: jobs/coder-step-14/ with:
#   - README.md (job instructions)
#   - job_metadata.json (configuration)
```

### 4. Context Files - Job-Specific Data

JSON files with information about the specific job:

```json
{
  "step_number": 14,
  "step_title": "Implement Clustering Algorithm",
  "related_steps": [13, 15],
  "dependencies": [
    "Data model from Step 13"
  ],
  "fresh_environment": false,
  "file_organization_check": true
}
```

---

## Using the System

### Generate a Coder Job

```bash
cd .github/copilot-instructions/config

python job_generator.py \
  --role coder \
  --step 14 \
  --title "Implement Clustering Algorithm" \
  --context context_examples/context_step14_coder.json \
  --output-dir ../../../generated_jobs
```

Result:
```
generated_jobs/coder-step-14/
├── README.md                    (Job instructions - START HERE)
├── job_metadata.json            (Job configuration)
└── Agent_Workspace/             (Agent creates this)
    ├── README.md               (Progress tracking)
    └── FINDINGS.md             (If applicable)
```

### What the Generated README Contains

```markdown
# Job: Coder - Step 14: Implement Clustering Algorithm

Generated: 2026-01-09 14:30:00

## Your Role
You are the **Coder** for this step.
See: roles/coder/COMPLETE_ROLE.md

## Context
- Step: 14
- Title: Implement Clustering Algorithm
- Related Steps: 13, 15, 16

## Dependencies
- Data model from Step 13
- Numpy and scipy libraries

## Designer Specification
See: Copilot_Development_Instructions/Step_14/specification.md

## Required Reading

### Shared Standards
- [AGENT_WORKSPACE](../../shared/AGENT_WORKSPACE.md)
- [LOGGING_STANDARDS](../../shared/LOGGING_STANDARDS.md)

### Role-Specific Guidance
- [SCOPE](../../roles/coder/SCOPE.md)
- [COMPLETE_ROLE](../../roles/coder/COMPLETE_ROLE.md)
- [TDD_WORKFLOW](../../roles/coder/TDD_WORKFLOW.md)
...
```

---

## Configuration: snippets.yml

### Snippet Metadata

Each snippet has:

| Field | Type | Meaning |
|-------|------|---------|
| `category` | string | Type: role, process, standards, checklist, template, setup, overview |
| `description` | string | One-line description |
| `path` | string | Path to actual snippet file |
| `applies_to` | list | [all, designer, coder, maintainer] |
| `always_include` | bool | Always include in jobs for this role |
| `priority` | string | high/normal/low - order of inclusion |
| `context_dependent` | bool | Include based on context? |
| `context_triggers` | list | Context keys that trigger inclusion |
| `status` | string | created, not_created_yet |

### Example: Optional Snippet

```yaml
coder:
  ENVIRONMENT_SETUP.md:
    category: setup
    description: Python environment setup
    path: roles/coder/ENVIRONMENT_SETUP.md
    applies_to: [coder]
    always_include: false  # Don't always include
    context_dependent: true  # Depends on context
    context_triggers: [fresh_environment, first_time]  # Include if these are true
    status: not_created_yet
```

Use:
```bash
# Fresh environment
python job_generator.py --role coder --step 14 \
  --context '{"fresh_environment": true}'
# Includes ENVIRONMENT_SETUP.md

# Existing environment
python job_generator.py --role coder --step 14
# Excludes ENVIRONMENT_SETUP.md
```

---

## Configuration: roles.yml

Groups snippets by role:

```yaml
roles:
  coder:
    title: Coder
    description: Implements code from specifications
    workspace: Jarvis
    
snippets_by_role:
  coder:
    always_include:  # Always in coder jobs
      - shared/AGENT_WORKSPACE.md
      - coder/SCOPE.md
      - coder/TDD_WORKFLOW.md
    optional:  # Included based on context
      - coder/ENVIRONMENT_SETUP.md
```

---

## Adding New Snippets

To add a new snippet:

1. **Create the snippet file** (e.g., `roles/designer/QUALITY_GATES.md`)

2. **Add to snippets.yml**:
   ```yaml
   designer:
     QUALITY_GATES.md:
       category: standards
       description: Quality gates and checklist
       path: roles/designer/QUALITY_GATES.md
       applies_to: [designer]
       always_include: true  # or false if conditional
   ```

3. **Update roles.yml** if needed:
   ```yaml
   snippets_by_role:
     designer:
       always_include:
         - designer/QUALITY_GATES.md  # Add here
   ```

4. Done! Jobs now automatically include it.

---

## Updating Shared Standards

To update a shared standard:

1. **Edit the snippet** (e.g., `shared/AGENT_WORKSPACE.md`)

2. All jobs that reference it automatically use new version!

No need to update individual job files.

---

## Context Examples

See `context_examples/` for templates:

- **context_step14_coder.json** - What context to pass for Coder job
- **context_step14_designer.json** - What context to pass for Designer job
- **context_step14_maintainer.json** - What context to pass for Maintainer job

Each shows what information the system needs to generate a specific job.

---

## The Generator Script

### Usage

```bash
python job_generator.py \
  --role {designer|coder|maintainer} \
  --step {number} \
  --title "{optional title}" \
  --context {json_context_file} \
  --config-dir {path_to_config} \
  --output-dir {where_to_save_job}
```

### Examples

**Designer job:**
```bash
python job_generator.py \
  --role designer \
  --step 14 \
  --title "Clustering Algorithm" \
  --context context_examples/context_step14_designer.json
```

**Coder job:**
```bash
python job_generator.py \
  --role coder \
  --step 14 \
  --title "Implement Clustering" \
  --context context_examples/context_step14_coder.json
```

**Maintainer job:**
```bash
python job_generator.py \
  --role maintainer \
  --step 14 \
  --context context_examples/context_step14_maintainer.json
```

### Output

```
✓ Job generated successfully
  Role: coder
  Step: 14
  Snippets included: 9

✓ Job created: jobs/coder-step-14
  - README.md (start here)
  - job_metadata.json (configuration)
```

---

## Key Benefits

✅ **Reusable snippets** - Use same snippet in many jobs  
✅ **One change propagates** - Update snippet, all jobs affected  
✅ **Context-aware** - Include snippets based on specific needs  
✅ **Specific jobs** - Never generic, always personalized  
✅ **Automated generation** - Create jobs with one command  
✅ **Consistent format** - All jobs follow same structure  
✅ **Easy to extend** - Add new snippets anytime  

---

## Workflow

```
1. Create context file
   context_step14_coder.json
   
2. Run generator
   python job_generator.py --role coder --step 14 \
     --context context_step14_coder.json
   
3. Job created
   jobs/coder-step-14/README.md
   
4. Agent starts job
   Read README.md
   Follow instructions
   Create Agent_Workspace/
   
5. Job complete
   Agent archives work
   You review REPORT.md
```

---

## Current Status

- [x] Configuration system designed
- [x] snippets.yml created
- [x] roles.yml created
- [x] job_generator.py script created
- [x] Example context files created
- [ ] Remaining snippets created (from role definitions)
- [ ] Job generation tested end-to-end

---

**System**: Configuration-driven job generation  
**Benefit**: Reusable, context-aware, one-command job creation  
**Key Files**: snippets.yml, roles.yml, job_generator.py
