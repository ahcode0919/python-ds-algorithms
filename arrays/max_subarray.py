"""Max Subarray.

Given an integer array nums, find the contiguous subarray (containing at least one number) that has the largest
sum, and return its sum.
"""

from typing import List


def max_subarray(nums: List[int]) -> int:
    """Kadane's algorithm: track the best sum ending at the current index."""
    length = len(nums)
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, length):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum
