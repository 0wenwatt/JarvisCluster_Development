# Instruction Snippets Database

**Centralized database of all instruction snippets. Used to generate agent jobs.**

---

## Concept

Instead of creating monolithic instruction files, we have:

1. **Reusable snippets** - Small, focused instruction pieces
2. **Snippets database** - Lists all available snippets and their properties
3. **Role definitions** - Describes what each role is
4. **Job templates** - Shows how to combine snippets for a job
5. **Job generator** - Creates specific jobs from templates and context

This allows:
- Reuse snippets across jobs
- Change a snippet once → affects all jobs that use it
- Generate specific jobs with context ("Coder for Step 14")
- Never generic ("you are a coder") always specific ("you are the coder for step 14")

---

## Database Structure

### Shared Snippets (All Roles/Jobs Use)

```yaml
shared:
  AGENT_WORKSPACE.md:
    category: standards
    description: "Workspace rules, what files allowed, progress tracking"
    applies_to: [all]
    always_include: true
    
  LOGGING_STANDARDS.md:
    category: standards
    description: "How to log findings, format, severity levels"
    applies_to: [all]
    always_include: true
    
  COMMUNICATION_STANDARDS.md:
    category: standards
    description: "How to report results to user"
    applies_to: [all, maintainer]
    priority: high
    context_dependent: false
```

### Designer Snippets

```yaml
designer:
  SCOPE.md:
    category: role
    description: "What Designer does and doesn't do"
    applies_to: [designer]
    always_include: true
    
  DESIGN_PROCESS.md:
    category: process
    description: "Step-by-step how to design"
    applies_to: [designer]
    always_include: true
    
  SPECIFICATION_TEMPLATE.md:
    category: template
    description: "Template for writing specifications"
    applies_to: [designer]
    always_include: true
    context_dependent: false
    
  DOCUMENTATION.md:
    category: standards
    description: "What to document and how"
    applies_to: [designer]
    always_include: true
```

### Coder Snippets

```yaml
coder:
  SCOPE.md:
    category: role
    description: "What Coder does and doesn't do"
    applies_to: [coder]
    always_include: true
    
  TDD_WORKFLOW.md:
    category: process
    description: "Test-first development workflow"
    applies_to: [coder]
    always_include: true
    
  CODE_STYLE.md:
    category: standards
    description: "Code style and quality standards"
    applies_to: [coder]
    always_include: true
    
  FILE_ORGANIZATION.md:
    category: standards
    description: "Production repo file organization"
    applies_to: [coder]
    always_include: true
    
  TESTING_REQUIREMENTS.md:
    category: standards
    description: "Test standards and coverage requirements"
    applies_to: [coder]
    always_include: true
    
  DOCUMENTATION_REQUIREMENTS.md:
    category: standards
    description: "Code documentation standards"
    applies_to: [coder]
    always_include: true
    
  ENVIRONMENT_SETUP.md:
    category: setup
    description: "Python environment setup"
    applies_to: [coder]
    always_include: false
    context_dependent: true
    context_triggers: [new_environment, fresh_setup]
```

### Maintainer Snippets

```yaml
maintainer:
  SCOPE.md:
    category: role
    description: "What Maintainer does"
    applies_to: [maintainer]
    always_include: true
    
  CONFORMANCE_CHECKLIST.md:
    category: checklist
    description: "What to verify"
    applies_to: [maintainer]
    always_include: true
    
  CODE_REVIEW.md:
    category: process
    description: "How to review code"
    applies_to: [maintainer]
    always_include: true
    
  TEST_VERIFICATION.md:
    category: process
    description: "How to verify tests"
    applies_to: [maintainer]
    always_include: true
    
  FILESYSTEM_CONFORMANCE.md:
    category: checklist
    description: "How to verify file organization"
    applies_to: [maintainer]
    always_include: false
    context_dependent: true
    context_triggers: [file_organization_check]
    
  DOCUMENTATION_REVIEW.md:
    category: checklist
    description: "How to review documentation"
    applies_to: [maintainer]
    always_include: false
    context_dependent: true
    context_triggers: [doc_check]
```

---

## Fields Explained

| Field | Type | Purpose |
|-------|------|---------|
| `category` | string | Type of snippet (role, process, standards, checklist, template, setup) |
| `description` | string | One-line description of what snippet covers |
| `applies_to` | array | Which roles this applies to [all, designer, coder, maintainer] |
| `always_include` | boolean | Should this always be in jobs for this role |
| `priority` | string | high/normal/low - order of inclusion |
| `context_dependent` | boolean | Does inclusion depend on context |
| `context_triggers` | array | What context triggers inclusion of this snippet |

---

## Example: Using the Database

### Designer Job for Step 14

```json
{
  "job_type": "designer",
  "role": "designer",
  "step": 14,
  "context": {
    "step_number": 14,
    "step_title": "Implement Clustering Algorithm",
    "related_steps": [13, 15],
    "previous_output": "Database schema from Step 13",
    "next_input_for": "Step 15 (testing)"
  }
}
```

Generator produces:

```
Include (always):
  shared/AGENT_WORKSPACE.md
  shared/LOGGING_STANDARDS.md
  shared/COMMUNICATION_STANDARDS.md
  designer/SCOPE.md
  designer/DESIGN_PROCESS.md
  designer/SPECIFICATION_TEMPLATE.md
  designer/DOCUMENTATION.md
  
Context-specific:
  designer/DESIGN_PROCESS.md (context: "You're designing Step 14 clustering algorithm")
  
Result: Specific job for Designer to create Step 14 spec
```

### Coder Job for Step 14

```json
{
  "job_type": "coder",
  "role": "coder",
  "step": 14,
  "context": {
    "step_number": 14,
    "step_title": "Implement Clustering Algorithm",
    "designer_spec": "[Link to Step 14 specification]",
    "related_steps": [13, 15],
    "dependencies": [
      "Database schema from Step 13",
      "Data models from Step 12"
    ],
    "fresh_environment": false
  }
}
```

Generator produces:

```
Include (always):
  shared/AGENT_WORKSPACE.md
  shared/LOGGING_STANDARDS.md
  shared/COMMUNICATION_STANDARDS.md
  coder/SCOPE.md
  coder/TDD_WORKFLOW.md
  coder/CODE_STYLE.md
  coder/FILE_ORGANIZATION.md
  coder/TESTING_REQUIREMENTS.md
  coder/DOCUMENTATION_REQUIREMENTS.md
  
Context-specific (because fresh_environment=false):
  (skip ENVIRONMENT_SETUP.md)
  
Result: Specific job for Coder to implement Step 14 from Designer's spec
```

### Maintainer Job for Step 14

```json
{
  "job_type": "maintainer",
  "role": "maintainer",
  "step": 14,
  "context": {
    "step_number": 14,
    "step_title": "Implement Clustering Algorithm",
    "designer_spec": "[Link to spec]",
    "coder_output": "[Link to code]",
    "check_file_organization": true,
    "check_documentation": true
  }
}
```

Generator produces:

```
Include (always):
  shared/AGENT_WORKSPACE.md
  shared/LOGGING_STANDARDS.md
  shared/COMMUNICATION_STANDARDS.md
  maintainer/SCOPE.md
  maintainer/CONFORMANCE_CHECKLIST.md
  maintainer/CODE_REVIEW.md
  maintainer/TEST_VERIFICATION.md
  
Context-specific (because check_file_organization=true):
  maintainer/FILESYSTEM_CONFORMANCE.md
  
Context-specific (because check_documentation=true):
  maintainer/DOCUMENTATION_REVIEW.md
  
Result: Specific job for Maintainer to review Step 14 implementation
```

---

## Current Snippets Available

### Shared (All Roles)
- [shared/AGENT_WORKSPACE.md](../../shared/AGENT_WORKSPACE.md)
- [shared/LOGGING_STANDARDS.md](../../shared/LOGGING_STANDARDS.md)
- [shared/COMMUNICATION_STANDARDS.md](../../shared/COMMUNICATION_STANDARDS.md)

### Designer Role
- [roles/designer/SCOPE.md](../../roles/designer/SCOPE.md)
- [roles/designer/COMPLETE_ROLE.md](../../roles/designer/COMPLETE_ROLE.md)
- (More to be created: DESIGN_PROCESS.md, SPECIFICATION_TEMPLATE.md, DOCUMENTATION.md, FILESYSTEM_RULES.md)

### Coder Role
- [roles/coder/SCOPE.md](../../roles/coder/SCOPE.md)
- [roles/coder/COMPLETE_ROLE.md](../../roles/coder/COMPLETE_ROLE.md)
- (More to be created: TDD_WORKFLOW.md, CODE_STYLE.md, FILE_ORGANIZATION.md, TESTING_REQUIREMENTS.md, DOCUMENTATION_REQUIREMENTS.md, ENVIRONMENT_SETUP.md)

### Maintainer Role
- [roles/maintainer/README.md](../../roles/maintainer/README.md)
- (Snippets not yet extracted from README files)

---

## How Job Generator Uses This

```python
def generate_job(job_type, role, step, context):
    """Generate a specific job based on type, role, step, and context."""
    
    snippets_to_include = []
    
    # Always include shared standards
    snippets_to_include.extend(db.get_snippets(applies_to="all"))
    
    # Always include role snippets marked always_include=true
    snippets_to_include.extend(
        db.get_snippets(applies_to=role, always_include=True)
    )
    
    # Conditionally include context-dependent snippets
    for snippet in db.get_snippets(context_dependent=True):
        if any(trigger in context for trigger in snippet.context_triggers):
            snippets_to_include.append(snippet)
    
    # Create job structure
    job = {
        'name': f"{role.title()} - Step {step}: {context.get('step_title')}",
        'role': role,
        'step': step,
        'context': context,
        'includes': snippets_to_include,
        'generated_at': datetime.now(),
        'unique_id': f"{role}_{step}_{context_hash}"
    }
    
    return job
```

---

## Benefits

✅ **One snippet, many jobs**  
✅ **Change snippet once, affects all jobs**  
✅ **Context-aware inclusion** (include snippets only when needed)  
✅ **Specific job generation** (never generic, always specific)  
✅ **Reusable configuration**  
✅ **Easy to extend** (add new snippets, update database)  

---

## Next Steps

1. Extract remaining role snippets from README files
2. Create snippets_database.yml with full configuration
3. Create role_definitions.yml with role metadata
4. Create job_generator.py script
5. Create example context configurations
6. Test job generation with real examples

---

**Database**: Centralized instruction snippets  
**Purpose**: Generate specific jobs from reusable components  
**Benefit**: One change propagates to all related jobs
