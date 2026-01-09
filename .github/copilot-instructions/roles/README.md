# Role-Based Instruction System

**Modular instruction snippets combined to create job-specific instructions for each role.**

---

## Overview

Instead of monolithic instruction files, this system uses **reusable snippets** that are combined to create instructions for specific roles:

- **Designer** - Designs architecture, structure, documents plans (no code)
- **Coder** - Implements code from specifications (writes code)
- **Maintainer** - Reviews code and files to ensure conformance (verification)

---

## The Three Roles

### 1. Designer 🎨
**You** - Creates design, architecture, plans, and documentation.

- Works in this repo (`JarvisCluster_Development`)
- No code allowed
- Markdown documentation only
- Creates step specs, design docs, planning
- Hands off to Coders

**Folders**: [designer/](designer/)

---

### 2. Coder 💻
**Production developer** - Implements from specifications.

- Works in production repo (`Jarvis`)
- Writes code, tests, documentation
- Follows Designer's specification exactly
- Uses TDD (tests first)
- Hands off to Maintainer

**Folders**: [coder/](coder/)

---

### 3. Maintainer ✓
**Code reviewer** - Verifies conformance to requirements.

- Reviews Designer's specification
- Reviews Coder's implementation
- Scans codebase for conformance
- Checks tests, coverage, style
- Approves or rejects work

**Folders**: [maintainer/](maintainer/)

---

## How It Works

### Step 1: Designer Creates Specification
```
Designer reads: design/ snippets
Designer writes: Step_X specification
Designer outputs: 
  - Spec document (what to build)
  - Test cases (how to verify)
  - File structure (where to put it)
Hands to: Coder
```

### Step 2: Coder Implements
```
Coder reads: coder/ snippets + Designer's spec
Coder writes: Code + Tests
Coder outputs: 
  - Implementation code
  - Test cases
  - Documentation
Hands to: Maintainer
```

### Step 3: Maintainer Verifies
```
Maintainer reads: maintainer/ snippets + Designer's spec + Coder's code
Maintainer scans: 
  - Does code match spec?
  - Do tests pass?
  - Is code quality good?
  - Are files organized correctly?
Maintainer outputs: 
  - Approval or rejection
  - Issues to fix
```

---

## Folder Structure

```
.github/copilot-instructions/roles/
├── README.md                        (this file)
├── INDEX.md                         (navigation)
│
├── designer/                        (Designer role snippets)
│   ├── README.md                   (Designer overview)
│   ├── SCOPE.md                    (What designer does)
│   ├── DESIGN_PROCESS.md           (How to design)
│   ├── SPECIFICATION_TEMPLATE.md   (How to write specs)
│   ├── DOCUMENTATION.md            (What to document)
│   └── ... more snippets
│
├── coder/                           (Coder role snippets)
│   ├── README.md                   (Coder overview)
│   ├── SCOPE.md                    (What coder does)
│   ├── ENVIRONMENT_SETUP.md        (Python env setup)
│   ├── TDD_WORKFLOW.md             (Test first approach)
│   ├── CODE_STYLE.md               (Style guidelines)
│   ├── FILE_ORGANIZATION.md        (Where to put files)
│   └── ... more snippets
│
└── maintainer/                      (Maintainer role snippets)
    ├── README.md                   (Maintainer overview)
    ├── SCOPE.md                    (What maintainer does)
    ├── CONFORMANCE_CHECKLIST.md    (What to check)
    ├── CODE_REVIEW.md              (How to review code)
    ├── TEST_VERIFICATION.md        (How to verify tests)
    └── ... more snippets
```

---

## Snippet Types

Each role has similar categories of snippets that match their responsibilities:

### Designer Snippets
- `SCOPE.md` - What you do
- `DESIGN_PROCESS.md` - How to design
- `SPECIFICATION_TEMPLATE.md` - How to write specs
- `DOCUMENTATION.md` - What docs to write
- `FILESYSTEM_RULES.md` - How this repo is organized

### Coder Snippets
- `SCOPE.md` - What you do
- `ENVIRONMENT_SETUP.md` - Python environment
- `TDD_WORKFLOW.md` - Test-first approach
- `CODE_STYLE.md` - Style guide
- `FILE_ORGANIZATION.md` - Where to put code
- `TESTING_REQUIREMENTS.md` - Test standards
- `DOCUMENTATION_REQUIREMENTS.md` - Doc standards

### Maintainer Snippets
- `SCOPE.md` - What you do
- `CONFORMANCE_CHECKLIST.md` - What to verify
- `CODE_REVIEW.md` - How to review
- `TEST_VERIFICATION.md` - How to verify tests
- `FILESYSTEM_CONFORMANCE.md` - Check file organization
- `DOCUMENTATION_REVIEW.md` - Check docs

---

## Using Snippets to Create Job Instructions

When you need to give a job to an agent (Designer, Coder, or Maintainer):

### For Designer Job
Combine snippets:
```
- designer/SCOPE.md
- designer/DESIGN_PROCESS.md
- designer/SPECIFICATION_TEMPLATE.md
- designer/DOCUMENTATION.md
+ specific task (Step_1, design review, etc.)
= Complete designer job instruction
```

### For Coder Job
Combine snippets:
```
- coder/SCOPE.md
- coder/ENVIRONMENT_SETUP.md
- coder/TDD_WORKFLOW.md
- coder/CODE_STYLE.md
- coder/FILE_ORGANIZATION.md
+ specific specification (from Designer)
= Complete coder job instruction
```

### For Maintainer Job
Combine snippets:
```
- maintainer/SCOPE.md
- maintainer/CONFORMANCE_CHECKLIST.md
- maintainer/CODE_REVIEW.md
- maintainer/TEST_VERIFICATION.md
+ Designer's spec + Coder's implementation
= Complete maintainer job instruction
```

---

## Benefits

### For You (Designer)
- ✅ Clear focus: Design only, no code concerns
- ✅ Reusable patterns: Design process documented once
- ✅ Easy specification: Template-based specs
- ✅ Clear handoff: Specification is precise

### For Coders
- ✅ Clear requirements: Spec tells exactly what to build
- ✅ Test cases provided: Know exactly what "done" means
- ✅ Reusable guidance: Common snippets for all jobs
- ✅ Clear standards: Code style, tests, docs all specified

### For Maintainer
- ✅ Clear checklist: Know exactly what to verify
- ✅ Reusable process: Same verification steps every time
- ✅ Easy approval: Clear pass/fail criteria
- ✅ Consistent quality: All work meets same standards

---

## Current Status

### Roles Created ✅
- [x] Designer role folder created
- [x] Coder role folder created
- [x] Maintainer role folder created
- [x] Overview documentation created

### Designer Snippets 🔄
- [ ] SCOPE.md
- [ ] DESIGN_PROCESS.md
- [ ] SPECIFICATION_TEMPLATE.md
- [ ] DOCUMENTATION.md
- [ ] ... (more as needed)

### Coder Snippets 🔄
- [ ] SCOPE.md
- [ ] ENVIRONMENT_SETUP.md
- [ ] TDD_WORKFLOW.md
- [ ] CODE_STYLE.md
- [ ] FILE_ORGANIZATION.md
- [ ] TESTING_REQUIREMENTS.md
- [ ] DOCUMENTATION_REQUIREMENTS.md
- [ ] ... (more as needed)

### Maintainer Snippets 🔄
- [ ] SCOPE.md
- [ ] CONFORMANCE_CHECKLIST.md
- [ ] CODE_REVIEW.md
- [ ] TEST_VERIFICATION.md
- [ ] FILESYSTEM_CONFORMANCE.md
- [ ] DOCUMENTATION_REVIEW.md
- [ ] ... (more as needed)

### Navigation 🔄
- [ ] INDEX.md for roles system
- [ ] Role-specific READMEs

---

## Navigation

### By Role
- [Designer Role](designer/) - Design and planning
- [Coder Role](coder/) - Implementation
- [Maintainer Role](maintainer/) - Verification

### By Task
- See [INDEX.md](INDEX.md) for snippet index by type

---

## Key Principle

**One snippet, one purpose. Combine snippets to create complete job instructions.**

Each snippet is focused, reusable, and can be combined with others to create specific instructions for specific jobs.

---

**System**: Role-Based Instruction Snippets  
**Status**: Framework created, snippets in progress  
**Next**: Create designer snippets
