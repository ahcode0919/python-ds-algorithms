"""Two Sum II.

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to
a specific target number. Return the indices such that they add up to the target, where the first number must be
less than the second. The returned indices (index1 and index2) are not zero-based. You may assume each input has
exactly one solution, and you may not use the same element twice.

Example: `[2, 7, 11, 15], target = 9` -> `[1, 2]` (the sum of 2 and 7 is 9, so index1 = 1, index2 = 2)
"""

from typing import List


def two_sum_ii(numbers: List[int], target: int) -> List[int]:
    """Two-pointer sweep inward on the sorted array, exploiting monotonic sum changes."""
    index_left = 0
    index_right = len(numbers) - 1

    while index_left < index_right:
        total = numbers[index_left] + numbers[index_right]
        if total < target:
            index_left += 1
        elif total > target:
            index_right -= 1
        else:
            return [index_left + 1, index_right + 1]
