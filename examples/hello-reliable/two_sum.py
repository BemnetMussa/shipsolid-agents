"""Two Sum — efficient lookup (ShipSolid hello-reliable demo).

Pattern: hash map complement (see algorithm-knowledge-base hash-map notes).
Time O(n), space O(n). Brute nested loops would be O(n^2).
"""

from __future__ import annotations


def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of two distinct elements that add to target.

    If multiple answers exist, returns one valid pair (first completion
    when scanning left to right). Raises ValueError if none.
    """
    seen: dict[int, int] = {}
    for i, value in enumerate(nums):
        need = target - value
        if need in seen:
            return [seen[need], i]
        seen[value] = i
    raise ValueError("no two sum pair")
