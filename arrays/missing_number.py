"""Missing Number.

Given an array nums containing n distinct numbers in the range `[0, n]`, return the only number in the range that
is missing from the array.
"""

from typing import List


def missing_number(nums: List[int]) -> int:
    """Sort the array and return the first index that doesn't match its value."""
    nums.sort()
    length = len(nums)

    for index in range(length):
        if nums[index] != index:
            return index
    return length


def missing_number_ii(nums: List[int]) -> int:
    """Compare the expected sum of `[0, n]` against the actual sum of nums."""
    length = len(nums)
    expected = (length * (length + 1)) // 2
    total = sum(nums)

    return expected - total
