# shipsolid-agents

Agent roles that make **code ship-solid**: efficient + doesn’t break.

Not another notes wiki. This repo is the **car** — agent skills/rules that turn intent into reliable code. Algorithm learning notes live in the knowledge base; this pack **uses** them.

## Non‑negotiables

1. **Efficient** — right complexity for the constraints (from the KB + algorithm judgment).
2. **Doesn’t break** — tested for the current scope; suite grows as the system grows; old tests stay.

## How it fits

| Piece | Role |
| --- | --- |
| [algorithm-knowledge-base](https://github.com/BemnetMussa/algorithm-knowledge-base) | Learning map (patterns, templates, pitfalls) |
| **shipsolid-agents** (this repo) | Agent kit: efficiency judgment + test agent |
| Your app repo | Where code actually ships |

## Agent skills

| Skill | Job |
| --- | --- |
| `algorithm-reasoning` | Classify pattern(s), plan efficiency, write from KB templates |
| `test-agent` | Add/keep tests for current scope, run them, fail loud on regressions |

## Quick start (Cursor)

1. Clone this repo (or add it as a submodule / open alongside your project).
2. Point the algorithm skill at your local KB clone (see skill files).
3. In chat: use **algorithm-reasoning** when writing/optimizing logic; use **test-agent** when proving code doesn’t break.
4. Prefer two roles over one mega-agent — writers shouldn’t only grade their own homework.

## Philosophy

- **Destination:** reliable code (doesn’t break + efficient enough).
- **Not the destination:** prettier prose, human approving every micro-decision, or dumping the whole KB into every prompt.
- Tests level up with the build: unit/edges first → integration when wired → keep prior tests.
- Language/stack is not the religion. **Logic is.**

## Status

Initial scaffold. Skills and project rules are under `.cursor/`.
