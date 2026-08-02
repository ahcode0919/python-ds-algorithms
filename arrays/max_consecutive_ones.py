from typing import List


def max_consecutive_ones(nums: List[int]) -> int:
    """Max Consecutive Ones.

    Return the largest number of consecutive 1s from an array of binary integers.

    Example: `[1, 1, 0, 1, 1, 1, 0, 0, 1]` -> `3`

    Single pass tracking a running streak of 1s reset on each 0.
    """
    max_ones, count = 0, 0

    for num in nums:
        if num == 1:
            count += 1
        else:
            max_ones = max(max_ones, count)
            count = 0

    return max(max_ones, count)
