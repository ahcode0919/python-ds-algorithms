"""Single Number.

Given a non-empty array of integers, every element appears twice except for one. Find that single one. Your
algorithm should have linear runtime complexity.

Example: `[2, 2, 1]` -> `1`
"""

from typing import List


def single_number(nums: List[int]) -> int:
    """Hash-table approach: count occurrences, then return the value seen once. Time: O(N), Space: O(N)."""
    if not nums:
        return 0

    nums_dict = dict()

    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1

    for num in nums_dict:
        if nums_dict[num] == 1:
            return num

    return 0


def single_number_bitwise(nums: List[int]) -> int:
    """Bitwise approach: XOR all values together, since duplicates cancel out. Time: O(N), Space: O(1)."""
    if not nums:
        return 0
    current = nums[0]

    for index in range(1, len(nums)):
        current ^= nums[index]

    return current
