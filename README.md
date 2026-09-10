# shipsolid-agents

You use this so agent-written code is **reliable**: efficient enough, and it doesn’t break.

This is not a notes wiki. It’s a Cursor **agent kit** (skills + rules). When you say build something, the agent should pick a solid approach, write the code, test what exists at this stage, and only then call it done.

## What “reliable” means here

1. **Efficient** — right algorithm / complexity for the constraints  
2. **Doesn’t break** — tested for the current scope; as the system grows, tests grow too; old tests stay  

Not the goal: prettier code, or you approving every tiny decision.

## Two repos

- **[algorithm-knowledge-base](https://github.com/BemnetMussa/algorithm-knowledge-base)** — learning notes (patterns, templates). You keep that for learning.  
- **This repo** — agents that *use* those notes to ship reliable code  

Your real app stays in your project. You open or point Cursor at this kit so the skills load.

## How it runs

```text
intent → algorithm-reasoning → code → test-agent → tests pass → done
```

| Skill | What it does |
| --- | --- |
| `shipsolid` | Runs the full pipeline above |
| `algorithm-reasoning` | Picks the pattern, plans efficiency, writes from the KB |
| `test-agent` | Adds/keeps tests, runs them, fails loud |

Rules live in `.cursor/rules/shipsolid.mdc`.

## Use it

1. Clone this repo. Clone the knowledge base too if you can (skills look for it under `C:/Users/bemne/algorithm-knowledge-base` — change the path in the skill files if yours is different).  
2. Open this repo in Cursor (alone or next to your app).  
3. In chat say **shipsolid** or “make this ship-solid.”  

Or call `algorithm-reasoning` / `test-agent` on their own if you only need one.

## Demo

Small example: efficient Two Sum + edge tests.

```bash
cd examples/hello-reliable
python -m unittest test_two_sum.py -v
```

One function on purpose. When you wire more pieces later, you add integration tests and keep these.

## If you change this repo

Edit skills/rules here. Edit learning notes in the knowledge base. Keep skills thin — don’t dump the whole KB into every prompt.
