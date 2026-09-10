# shipsolid-agents

**Cursor agent kit for reliable code:** efficient enough + doesn’t break.

If you’re reading this months later (or you’re a contributor): this is **not** a DSA wiki and **not** a model we train. It’s a set of **agent skills + rules** so that when someone says “build this,” the agent doesn’t stop at code that *looks* good — it picks a solid approach, writes it, tests the current scope, and only then calls it done.

---

## The idea in one breath

| | |
| --- | --- |
| **Problem** | Agents write code that often works on the happy path but can use the wrong algorithm, miss edges, or hide bad complexity. |
| **Destination (A → B)** | **Reliable code** — doesn’t break on the scenarios for this stage of the system, and is efficient enough for the constraints. |
| **How** | Two non‑negotiables, enforced by agent roles (not by babysitting every decision). |
| **Not the goal** | Prettier style, human approving every step, or rewriting the learning notes repo. |

**Non‑negotiables**

1. **Efficient** — right complexity / pattern for the constraints.  
2. **Doesn’t break** — tests for *current* scope; suite grows as the system grows; **old tests stay**.

Logic matters more than language or stack. Language is not a barrier.

---

## Two repos (don’t mix them up)

| Repo | What it is |
| --- | --- |
| [algorithm-knowledge-base](https://github.com/BemnetMussa/algorithm-knowledge-base) | **Learning map** — human-friendly algorithm notes, templates, pitfalls. Leave it for learning. |
| **shipsolid-agents** (this repo) | **The car** — agent skills/rules that *use* that map to ship reliable code. |

Your real app stays in whatever project you’re building. Open or reference this kit so Cursor can load the skills.

---

## What’s in the box

| Path | Role |
| --- | --- |
| `.cursor/skills/shipsolid` | **Orchestrator** — full pipeline before “done” |
| `.cursor/skills/algorithm-reasoning` | Efficiency pillar — classify pattern(s), plan Big O, code from KB templates |
| `.cursor/skills/test-agent` | Doesn’t-break pillar — add/keep tests, run them, fail loud |
| `.cursor/rules/shipsolid.mdc` | Always-on reminder of the non‑negotiables |
| `examples/hello-reliable` | Tiny demo: efficient Two Sum + edge unit tests |

**Pipeline (what “shipsolid” means):**

```text
intent → algorithm-reasoning → code → test-agent → suite green → DONE
```

Tests grow with the build: one function → unit/edges; wired into other pieces → integration; **never throw away prior tests**.

---

## Quick start (Cursor)

1. Clone this repo (and ideally clone the [knowledge base](https://github.com/BemnetMussa/algorithm-knowledge-base) locally — skills default to `C:/Users/bemne/algorithm-knowledge-base`; change paths in the skill files if yours differs).
2. Open this repo in Cursor (or open it alongside your app).
3. In chat say **`shipsolid`** or “make this ship-solid” so the orchestrator runs both pillars.
4. Or call **`algorithm-reasoning`** / **`test-agent`** alone when you only need one role.

### Demo

```bash
cd examples/hello-reliable
python -m unittest test_two_sum.py -v
```

That’s a **unit-scope** example on purpose: prove edges for one function. Integration comes later when you wire things together.

---

## For contributors

- **Change agent behavior** here (skills/rules) — not by pasting the whole KB into prompts.  
- **Change learning notes** in [algorithm-knowledge-base](https://github.com/BemnetMussa/algorithm-knowledge-base).  
- Keep skills thin: index → open only the matched notes (progressive disclosure).  
- Don’t expand the demo into a full product; it’s a teaching loop for the pipeline.

---

## Status

Scaffold live: orchestrator + efficiency skill + test-agent + hello-reliable demo. Next ideas (when we want them): CI on the demo, more examples — not required to understand the idea.
