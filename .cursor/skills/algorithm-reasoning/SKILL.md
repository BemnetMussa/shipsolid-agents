---
name: algorithm-reasoning
description: >-
  Classifies problems into algorithm patterns (or combinations) using the
  algorithm-knowledge-base, plans an efficient approach, then writes
  template-based code. Use when solving DSA/logic-heavy tasks, optimizing hot
  paths, reviewing Big O, or when ShipSolid efficiency non-negotiable applies.
---

# Algorithm reasoning (efficiency pillar)

Part of **shipsolid-agents**. Non‑negotiable: **efficient enough** for the constraints.

## Knowledge base (map, not this repo)

Default local path (adjust if needed):

`C:/Users/bemne/algorithm-knowledge-base`

Remote: https://github.com/BemnetMussa/algorithm-knowledge-base

1. Read `pattern-index.md` in this skill folder first (or the KB copy under `.cursor/skills/algorithm-reasoning/` if present in the KB clone).
2. Open **only** matched notes under the KB root.
3. Prefer KB templates + pitfalls over inventing a new shape.

If the KB is missing, say so, reason from first principles, and still state complexity.

## Collaboration

- **Command → happen.** Do not ask permission for classification or drafting.
- Ask the human only when requirements are genuinely ambiguous or two approaches trade on a preference they must choose.
- Human sets intent; this role owns algorithmic judgment + code for the efficiency pillar.

## Pipeline

```
Logic brief:
- Problem:
- Constraints / scale:
- Signals:
- Pattern(s) / combo:
- Why not near-misses:
- Time / space target:
- KB notes used:
- Edge cases:
```

1. Extract signals → match patterns (and combos).
2. Read matched KB notes.
3. Lock efficiency plan (beat the obvious brute force when constraints require it).
4. Write code from templates.
5. Hand off to **test-agent** mindset: don’t claim “done” without scenarios for this scope (or invoke test-agent).

## Anti-patterns

- Jumping to code with no pattern name
- Ignoring KB when a note exists
- Claiming optimal with no competing approach named
- Waiting for “should I use BFS?” when signals are clear
