# Hello Reliable

Tiny ShipSolid demo: **efficient enough** + **doesn’t break** (tests for this scope).

## What it shows

| Pillar | Here |
| --- | --- |
| Efficiency | `two_sum` via hash map — O(n) time, O(n) space (not nested O(n²)) |
| Doesn’t break | Unit + edge tests in `test_two_sum.py` — suite you **keep** as you grow |

## Run

```bash
cd examples/hello-reliable
python -m unittest test_two_sum.py -v
```

## Try ShipSolid on it

In Cursor (with this repo open):

> shipsolid — add a function `two_sum_all` that returns all index pairs, keep old tests, add new ones, don’t break efficiency

Watch the orchestrator: intent → algorithm-reasoning → code → test-agent → green.
