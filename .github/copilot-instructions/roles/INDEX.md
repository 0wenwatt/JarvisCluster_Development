# Roles System Index

**Navigation guide for role-based instruction snippets.**

---

## The Three Roles

### 🎨 [Designer Role](designer/)
**Create design, specs, plans, documentation**

You work in: `JarvisCluster_Development/`

**Key snippets**:
- [Designer README](designer/README.md) - Role overview
- [Designer INDEX](designer/INDEX.md) - All snippets

**What you deliver**:
- Specification documents
- Test cases
- Design documentation
- Planning documents

---

### 💻 [Coder Role](coder/)
**Implement code from specifications**

You work in: `Jarvis/` (production repo)

**Key snippets**:
- [Coder README](coder/README.md) - Role overview
- [Coder INDEX](coder/INDEX.md) - All snippets

**What you deliver**:
- Implementation code
- Test suite
- Code documentation
- Clean workspace

---

### ✓ [Maintainer Role](maintainer/)
**Verify code conforms to specifications**

You review: Both repos (specs + code)

**Key snippets**:
- [Maintainer README](maintainer/README.md) - Role overview
- [Maintainer INDEX](maintainer/INDEX.md) - All snippets

**What you deliver**:
- Approval or rejection
- Issue reports
- Feedback and guidance

---

## Workflow: Designer → Coder → Maintainer

```
DESIGNER
  ↓
  Creates: Specification + Test Cases
  Delivers to: Coder
  
CODER (receives spec)
  ↓
  Creates: Tests (test-first)
  Creates: Implementation code
  Delivers to: Maintainer
  
MAINTAINER (receives spec + code)
  ↓
  Verifies: Code matches spec?
  Verifies: Tests pass?
  Verifies: Quality good?
  Decision: APPROVE or REQUEST CHANGES
  Delivers to: You (acceptance)
```

---

## Finding What You Need

### I need to give a job to an Agent...

**Designer Job**?
→ Go to [Designer Role](designer/README.md)
→ Use snippets from [Designer INDEX](designer/INDEX.md)

**Coder Job**?
→ Go to [Coder Role](coder/README.md)
→ Use snippets from [Coder INDEX](coder/INDEX.md)

**Maintainer Job**?
→ Go to [Maintainer Role](maintainer/README.md)
→ Use snippets from [Maintainer INDEX](maintainer/INDEX.md)

---

### I need a specific snippet...

**Designer snippets**:
- SCOPE.md - What Designer does
- DESIGN_PROCESS.md - How to design
- SPECIFICATION_TEMPLATE.md - How to write specs
- DOCUMENTATION.md - What to document
- FILESYSTEM_RULES.md - Design repo organization

**Coder snippets**:
- SCOPE.md - What Coder does
- ENVIRONMENT_SETUP.md - Python setup
- TDD_WORKFLOW.md - Test-first process
- CODE_STYLE.md - Code standards
- FILE_ORGANIZATION.md - Production repo organization
- TESTING_REQUIREMENTS.md - Test standards
- DOCUMENTATION_REQUIREMENTS.md - Doc standards

**Maintainer snippets**:
- SCOPE.md - What Maintainer does
- CONFORMANCE_CHECKLIST.md - What to verify
- CODE_REVIEW.md - How to review
- TEST_VERIFICATION.md - How to test
- FILESYSTEM_CONFORMANCE.md - File organization check
- DOCUMENTATION_REVIEW.md - Doc review

---

## Creating Job Instructions

### Template for Designer Job

```markdown
# Designer Job: [Task]

## Your Task
[What needs designing]

## Requirements
- Read [Designer Role](roles/designer/README.md)
- Read [Designer/SCOPE.md](roles/designer/SCOPE.md)
- Read [Designer/DESIGN_PROCESS.md](roles/designer/DESIGN_PROCESS.md)

## Deliverables
- Read [Designer/SPECIFICATION_TEMPLATE.md](roles/designer/SPECIFICATION_TEMPLATE.md)
- Read [Designer/DOCUMENTATION.md](roles/designer/DOCUMENTATION.md)

## Success Criteria
- [ ] Complete specification
- [ ] Clear test cases
- [ ] Design documented
- [ ] Ready for Coder
```

---

### Template for Coder Job

```markdown
# Coder Job: Implement [Task]

## Your Task
[What needs implementing]

## Specification
[Link to Designer's spec]

## Requirements
- Read [Coder Role](roles/coder/README.md)
- Read [Coder/ENVIRONMENT_SETUP.md](roles/coder/ENVIRONMENT_SETUP.md)
- Read [Coder/TDD_WORKFLOW.md](roles/coder/TDD_WORKFLOW.md)
- Read [Coder/CODE_STYLE.md](roles/coder/CODE_STYLE.md)
- Read [Coder/FILE_ORGANIZATION.md](roles/coder/FILE_ORGANIZATION.md)

## Deliverables
- See [Coder/TESTING_REQUIREMENTS.md](roles/coder/TESTING_REQUIREMENTS.md)
- See [Coder/DOCUMENTATION_REQUIREMENTS.md](roles/coder/DOCUMENTATION_REQUIREMENTS.md)

## Success Criteria
- [ ] All spec tests implemented
- [ ] All tests passing
- [ ] Coverage 80%+
- [ ] Code follows style
- [ ] Ready for Maintainer
```

---

### Template for Maintainer Job

```markdown
# Maintainer Job: Review [Task] Implementation

## Specification
[Link to Designer's spec]

## Implementation
[Link to Coder's code]

## Your Task
Verify implementation matches specification.

## Verification
- Read [Maintainer Role](roles/maintainer/README.md)
- Read [Maintainer/CONFORMANCE_CHECKLIST.md](roles/maintainer/CONFORMANCE_CHECKLIST.md)
- Read [Maintainer/CODE_REVIEW.md](roles/maintainer/CODE_REVIEW.md)
- Read [Maintainer/TEST_VERIFICATION.md](roles/maintainer/TEST_VERIFICATION.md)

## Result
APPROVE ✓ or REQUEST CHANGES with specific issues
```

---

## Current Status

### Roles Created ✅
- [x] Designer role and snippets structure
- [x] Coder role and snippets structure
- [x] Maintainer role and snippets structure

### Documentation Created ✅
- [x] Role overviews (README.md per role)
- [x] Snippet indices (INDEX.md per role)
- [x] Workflow documentation
- [x] Job instruction templates

### Snippets Planned 🔄
These snippets need to be created next:

**Designer Snippets** (5 total):
- [ ] SCOPE.md
- [ ] DESIGN_PROCESS.md
- [ ] SPECIFICATION_TEMPLATE.md
- [ ] DOCUMENTATION.md
- [ ] FILESYSTEM_RULES.md

**Coder Snippets** (7 total):
- [ ] SCOPE.md
- [ ] ENVIRONMENT_SETUP.md
- [ ] TDD_WORKFLOW.md
- [ ] CODE_STYLE.md
- [ ] FILE_ORGANIZATION.md
- [ ] TESTING_REQUIREMENTS.md
- [ ] DOCUMENTATION_REQUIREMENTS.md

**Maintainer Snippets** (6 total):
- [ ] SCOPE.md
- [ ] CONFORMANCE_CHECKLIST.md
- [ ] CODE_REVIEW.md
- [ ] TEST_VERIFICATION.md
- [ ] FILESYSTEM_CONFORMANCE.md
- [ ] DOCUMENTATION_REVIEW.md

---

## System Architecture

```
.github/copilot-instructions/
├── roles/                           (Role-based snippets)
│   ├── README.md                   (System overview)
│   ├── INDEX.md                    (This file - navigation)
│   │
│   ├── designer/                   (Designer role)
│   │   ├── README.md              (Role overview)
│   │   ├── INDEX.md               (Snippet index)
│   │   ├── SCOPE.md               (Not yet created)
│   │   ├── DESIGN_PROCESS.md      (Not yet created)
│   │   ├── SPECIFICATION_TEMPLATE.md (Not yet created)
│   │   ├── DOCUMENTATION.md       (Not yet created)
│   │   └── FILESYSTEM_RULES.md    (Not yet created)
│   │
│   ├── coder/                      (Coder role)
│   │   ├── README.md              (Role overview)
│   │   ├── INDEX.md               (Snippet index)
│   │   ├── SCOPE.md               (Not yet created)
│   │   ├── ENVIRONMENT_SETUP.md   (Not yet created)
│   │   ├── TDD_WORKFLOW.md        (Not yet created)
│   │   ├── CODE_STYLE.md          (Not yet created)
│   │   ├── FILE_ORGANIZATION.md   (Not yet created)
│   │   ├── TESTING_REQUIREMENTS.md (Not yet created)
│   │   └── DOCUMENTATION_REQUIREMENTS.md (Not yet created)
│   │
│   └── maintainer/                 (Maintainer role)
│       ├── README.md              (Role overview)
│       ├── INDEX.md               (Snippet index)
│       ├── SCOPE.md               (Not yet created)
│       ├── CONFORMANCE_CHECKLIST.md (Not yet created)
│       ├── CODE_REVIEW.md         (Not yet created)
│       ├── TEST_VERIFICATION.md   (Not yet created)
│       ├── FILESYSTEM_CONFORMANCE.md (Not yet created)
│       └── DOCUMENTATION_REVIEW.md (Not yet created)
│
├── (Other existing instruction folders)
└── (Other existing instruction files)
```

---

## Key Principle

**Build job instructions from reusable snippets.**

Instead of creating monolithic instruction files for each job, combine focused snippets that can be reused across many jobs. Each snippet covers one topic for one role, making it:
- Reusable across jobs
- Easy to maintain
- Quick to update
- Consistent across roles

---

**System**: Role-Based Instruction Snippets  
**Status**: Framework created, snippets in progress  
**Next**: Create individual snippets for each role
