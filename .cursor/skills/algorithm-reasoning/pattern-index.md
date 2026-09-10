# Pattern index (signals → KB notes)

Paths are relative to the **algorithm-knowledge-base** repo root.

| If you see… | Reach for | Note |
|---|---|---|
| Sorted / monotonic predicate / min feasible value | Binary search (incl. on answer) | `searching/binary-search.md` |
| Contiguous subarray/substring + window condition | Sliding window | `sliding-window/sliding-window.md` |
| Two ends / pair from sorted | Two pointers | `array/two-pointers.md` |
| Range / subarray sums after prep | Prefix sum | `prefix-sum/prefix-sum.md` |
| Next greater/smaller, spans | Monotonic stack | `stack/monotonic-stack.md` |
| Fast membership / frequencies | Hash map / set | `hash-map/hash-map.md` |
| Top-k / priority | Heap | `heap/heap.md` |
| Prefix strings | Trie | `trie/trie.md` |
| Connectivity / merge sets | Union-Find | `union-find/union-find.md` |
| Explore / flood | DFS | `graph/dfs.md` |
| Unweighted shortest / levels | BFS | `graph/bfs.md` |
| Weighted shortest (non-neg) | Dijkstra | `graph/dijkstra.md` |
| Prerequisites / DAG order | Topological sort | `graph/topological-sort.md` |
| Overlapping subproblems | DP | `dynamic-programming/dynamic-programming.md` |
| Generate / prune configs | Backtracking | `backtracking/backtracking.md` |
| Bits / masks | Bitwise | `Bitwise/bitwise.md` |

## Common combos

- Binary search + greedy check → “min/max X such that…”
- Sliding window + hash map → substring with counts
- Prefix sum + hash map → subarray sum equals k
- Sort + two pointers → pair/triplet sums
- Kruskal + union-find → MST
- Kahn BFS + indegree → topo
- Trie + DFS → word search style

Open **both** notes; say outer vs inner structure.
