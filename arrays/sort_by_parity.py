"""Sort By Parity.

Given an array of non-negative integers, return an array consisting of all the even elements, followed by all
the odd elements.

Example: `[3, 1, 2, 4]` -> `[2, 4, 3, 1]` (can be any order)
"""

from typing import List


def sort_by_parity(nums: List[int]) -> List[int]:
    """Two-pointer partition swapping odd values found on the left with even values found on the right."""
    length = len(nums)
    left_index = 0
    right_index = length - 1

    while left_index < right_index:
        if nums[left_index] % 2 == 0:
            left_index += 1
        elif nums[right_index] % 2 != 0:
            right_index -= 1
        else:
            nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
            left_index += 1
            right_index -= 1
    return nums
