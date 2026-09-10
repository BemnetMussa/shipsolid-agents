"""Unit + edge scenarios for two_sum — grow this suite; don't drop it."""

from __future__ import annotations

import unittest

from two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    def test_basic_pair(self) -> None:
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_pair_later_in_array(self) -> None:
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])

    def test_duplicates_same_value(self) -> None:
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

    def test_negatives(self) -> None:
        self.assertEqual(two_sum([-1, -2, -3, -4, -5], -8), [2, 4])

    def test_empty_raises(self) -> None:
        with self.assertRaises(ValueError):
            two_sum([], 0)

    def test_single_element_raises(self) -> None:
        with self.assertRaises(ValueError):
            two_sum([1], 1)

    def test_no_pair_raises(self) -> None:
        with self.assertRaises(ValueError):
            two_sum([1, 2, 3], 100)

    def test_zeros(self) -> None:
        self.assertEqual(two_sum([0, 4, 3, 0], 0), [0, 3])


if __name__ == "__main__":
    unittest.main()
