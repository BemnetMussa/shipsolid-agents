# Why ShipSolid

You’re reading this if you want the case for the problem — and why **this** kind of fix, not something else.

## The problem is real

Agent code often **looks fine** and **works on the happy path**. That’s why it’s easy to trust it. The pain shows up later: wrong or lazy algorithm, missed edges, or complexity that dies when input grows. “It runs on my machine” is not the same as reliable.

You can feel this yourself. You can also see it in the wild:

- Developers use AI more, but trust it less. The top frustration is code that’s **almost right** — which is harder to debug than code that’s obviously wrong. ([Stack Overflow 2025](https://survey.stackoverflow.co/2025/ai/))
- Studies of LLM bugs call out **misinterpretation** and **missing corner cases** — the code matches the vibe of the task and still fails on edges. ([arXiv:2403.08937](https://arxiv.org/html/2403.08937))
- Passing unit tests doesn’t mean the code is solid overall (quality/security issues still show up). ([arXiv:2508.14727](https://arxiv.org/pdf/2508.14727))
- On harder problems, models often pick **suboptimal algorithms** and timeout; they can pass contests-style checks and still fail when you require real complexity bounds. ([arXiv:2407.06153](https://arxiv.org/html/2407.06153), [BigO(Bench)](https://arxiv.org/pdf/2503.15242))

So the gap isn’t “AI can’t write code.” It’s **unreliable judgment on the path from intent → right idea → code that still holds**.

**Reliable here means:** efficient enough for the constraints, and it doesn’t break on the scenarios that matter at this stage of the system.

## What doesn’t fix it (other options)

| Option | Why it’s not enough |
| --- | --- |
| Bigger model / better prompt only | Still jumps to code; same failure modes, prettier output |
| Another DSA wiki alone | Passive notes don’t run when you’re coding — you already have a KB for learning |
| Human approves every step | Slow and painful; people want command → happen |
| “Just write more unit tests” in chat | Easy to forget, easy to drop; no growing suite, no forced efficiency |
| Train a custom model first | Heavy, slow, and not required to enforce a reliability loop |

Those are faster horses. You want a car: **navigation + build + proof you arrived.**

## Why something like ShipSolid

You need machinery that makes the two non‑negotiables hard to skip:

1. **Efficient** — classify the pattern (or combo), plan complexity, use known templates (your knowledge base).  
2. **Doesn’t break** — tests for *this* scope, keep old tests as you grow, run them, fail loud.

ShipSolid does that as **agent roles** (orchestrator + algorithm judgment + test agent), not as a new model and not as a wiki you forget to open.

```text
intent → pick efficient approach → code → test current scope → green → done
```

You still command. You don’t babysit every decision. The agent doesn’t get to stop at “looks good.”

## When this is the wrong tool

- Pure UI/CRUD with no real logic or scale pressure — the pain may be small.  
- Security hardening as the main goal — related trust problem, different product.  
- Replacing human ownership of *what* to build — you still set intent.

## Bottom line

The problem exists: agent code can look right and still be wrong or too slow under real use.  
The answer isn’t more notes or more nagging — it’s a **forced reliability loop** (efficiency + growing tests) as agent skills. That’s what this repo is for.
