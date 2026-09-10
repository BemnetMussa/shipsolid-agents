---
name: shipsolid
description: >-
  ShipSolid orchestrator: runs the full reliability pipeline — efficient
  algorithm judgment then test scenarios — before calling work done. Use when
  the user wants ship-solid / reliable code, says shipsolid, asks to implement
  or optimize something that must not break, or wants command-to-done without
  babysitting each step.
---

# ShipSolid orchestrator

You are the **car**, not a faster horse. Destination: **reliable code** = efficient enough + doesn’t break.

Do **not** stop after “code that looks good.” Run the full pipeline. Command → happen. Ask only if intent/constraints are genuinely ambiguous.

## Non‑negotiables

1. **Efficient** — right complexity for constraints (algorithm judgment + KB).
2. **Doesn’t break** — tests for current scope; keep prior tests; run them; fail loud.

## Pipeline (mandatory order)

Copy and fill as you go:

```
ShipSolid status:
- [ ] 1. Intent locked (I/O, constraints, scale)
- [ ] 2. Efficiency plan (algorithm-reasoning)
- [ ] 3. Code written from plan/templates
- [ ] 4. Tests added/kept (test-agent) for THIS scope
- [ ] 5. Suite run — PASS
- [ ] DONE (only after 5)
```

### 1. Intent
Capture: what to build, inputs/outputs, constraints (n, time, memory), current scope (single function vs wired into system).

### 2. Efficiency — follow `algorithm-reasoning`
Read and apply:
`.cursor/skills/algorithm-reasoning/SKILL.md`
(and its `pattern-index.md`; open KB notes as that skill says).

Output a short logic brief: pattern(s)/combo, complexity target, edges. Then implement.

### 3. Code
Implement from the plan. No “I’ll test later.” Efficiency claim must match the approach.

### 4. Doesn’t-break — follow `test-agent`
Read and apply:
`.cursor/skills/test-agent/SKILL.md`

- Scope-matched tests (unit/edges now; integration when wired).
- **Keep** existing tests.
- Prefer tests in the **target project repo**.

### 5. Run
Execute the project’s test command. On failure: fix code (or correct a wrong test if it contradicts the locked intent), re-run until green or blocked on missing intent.

### DONE
Only after the suite passes for this scope. Summarize in a few lines: approach + complexity + what was tested. No essay.

## Role split (same session is fine)

| Phase | Skill |
| --- | --- |
| Pattern + efficiency + implement | `algorithm-reasoning` |
| Scenarios + keep suite + run | `test-agent` |
| Order + “not done until green” | **this skill (`shipsolid`)** |

You may play both roles in one chat, but you must **not skip** the test-agent phase after coding.

## Autonomy

- Do not ask “should I add tests?” — add them.
- Do not ask “should I use the KB?” — use it when algorithmic.
- Ask only when you cannot infer the contract or how to run tests.

## Anti-patterns

- Shipping after code-only with zero new/updated tests
- Dropping old tests
- Skipping complexity reasoning on logic-heavy work
- Happy-path-only tests
- Declaring DONE while tests are red or unrun
