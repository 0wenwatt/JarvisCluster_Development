# Coder - SCOPE

**What you do and don't do.**

---

## Your Responsibilities

### ✅ You Do This

**Implement**:
- Write code from specification
- Follow file structure specified
- Implement all required features
- Handle edge cases specified
- Handle error conditions specified

**Test First**:
- Read test cases from spec
- Write tests from test cases (before code)
- Make tests pass with implementation
- Verify coverage is 80%+
- Ensure no skipped tests

**Document**:
- Add docstrings to functions/classes
- Comment complex logic
- Explain non-obvious code
- Update README if needed
- Document assumptions

**Quality**:
- Follow code style guide
- Keep code clean
- No debug prints or temp code
- No commented-out code
- No temporary variables

**Collaborate**:
- Ask Designer to clarify ambiguities
- Tell Maintainer what to check
- Respond to feedback
- Make requested changes
- Work toward approval

---

### ❌ You Don't Do This

- **Change specification** - Accept it as-is
- **Make design decisions** - Designer made them
- **Skip test cases** - Implement all of them
- **Write tests after code** - Tests FIRST
- **Approve your own work** - Maintainer does that
- **Decide code structure** - Designer specified it
- **Leave debug code** - Clean it all up
- **Low test coverage** - Must be 80%+
- **Poor documentation** - Must document thoroughly

---

## Your Authority

### When You Decide

- Implementation techniques
- Library choices (within guidelines)
- Code optimization
- Refactoring for clarity
- Testing strategy (within TDD framework)

### When Designer Decides

- What to build
- How to architecture it
- What file structure to use
- What features to include
- What edge cases to handle

### When Maintainer Decides

- Whether code meets spec
- Whether quality is acceptable
- Whether tests are sufficient
- Whether to approve work
- Whether changes are needed

---

## Interaction Points

### With Designers

**You Receive**:
- Specification document
- Test cases (as requirements)
- File structure plan
- Architecture rationale

**You Ask**:
- Clarifications on ambiguities
- Confirmation of test interpretation
- Edge case handling details
- Feature priorities

**You Follow**:
- Specification exactly
- Test cases as requirements
- File structure as planned
- Success criteria defined

**You Never**:
- Deviate from spec
- Skip test cases
- Change architecture
- Make design decisions

### With Maintainers

**You Provide**:
- Implementation code
- Test suite (all passing)
- Code documentation
- Clean workspace
- Work ready for review

**Maintainer Provides**:
- Code review
- Quality assessment
- Approval or feedback
- Specific improvement requests

**If Changes Requested**:
- Fix specific issues
- Re-test
- Re-submit
- Repeat until approved

---

## Boundary Cases

### Ambiguous Specification

**If spec is unclear**:
- Ask Designer for clarification BEFORE implementing
- Get confirmation on interpretation
- Update spec if needed (Designer approves)
- Don't assume or guess

**Before handing off**:
- No ambiguities in your understanding
- All test cases understood
- All edge cases handled

### Test Case Interpretation

**If test case is unclear**:
- Ask Designer what behavior is required
- Confirm test case implementation
- Ask for examples if needed
- Don't guess at intent

### Implementation Challenges

**If implementation is harder than expected**:
- Tell Designer about the challenge
- Ask if approach is different than intended
- Confirm behavior is still correct
- Never skip test cases
- Never lower coverage below 80%

### Code Quality vs. Schedule

**If running out of time**:
- Tests must pass (non-negotiable)
- Coverage must be 80%+ (non-negotiable)
- Code must be documented (non-negotiable)
- Quality is not negotiable
- All work before handoff

---

## Quality Gates

Your work is ready to hand off when:

- [ ] **All tests implemented**
  - From Designer's test cases
  - Every case covered
  - No skipped tests

- [ ] **All tests passing**
  - Run: `pytest tests/ -v`
  - 100% pass rate
  - No failures or errors

- [ ] **Coverage sufficient**
  - Run: `pytest --cov`
  - Coverage >= 80%
  - All critical code covered

- [ ] **Code quality good**
  - Follows style guide
  - No debug code
  - No temp files
  - Well-organized

- [ ] **Documentation complete**
  - Docstrings present
  - Complex logic explained
  - Assumptions documented
  - Type hints added

- [ ] **Files organized**
  - Follow Designer's structure
  - Clear module organization
  - Appropriate grouping
  - No clutter

- [ ] **Workspace clean**
  - No temporary files
  - No debug code
  - No IDE files
  - Ready to review

---

## Common Mistakes to Avoid

### ❌ Don't

- Guess at test case meaning (ask Designer)
- Skip test cases (implement all)
- Test after code ("I'll test later" = never)
- Have low coverage (must be 80%+)
- Leave debug code in ("I'll clean it up" = you won't)
- Make design decisions (that's Designer's job)
- Deviate from spec (implement what Designer said)
- Assume ambiguities (ask Designer)

### ✅ Do

- Ask for clarifications upfront
- Implement all test cases
- Test first, then code
- Aim for 85%+ coverage
- Clean code before handoff
- Follow Designer's architecture
- Implement spec exactly
- Confirm understanding before starting

---

## Success Indicators

You're doing well when:

✅ Tests define all requirements  
✅ Code passes all tests  
✅ Coverage is 85%+  
✅ Code is clean and documented  
✅ Maintainer gives approval  
✅ No major feedback needed  
✅ Code used directly in production  
✅ Designer is satisfied  

---

**Role**: Coder - Scope  
**Authority**: Implementation technique, code optimization, testing strategy  
**Responsibility**: Meeting spec, writing tests first, code quality, documentation
