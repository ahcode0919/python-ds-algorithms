"""Move Zeros.

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of
the non-zero elements. You must do this in-place without making a copy of the array, and minimize the total
number of operations.

Example: `[0, 1, 0, 3, 12]` -> `[1, 3, 12, 0, 0]`
"""

from typing import List


def move_zeros(nums: List[int]) -> None:
    """Two-pointer in-place compaction: write non-zero values forward, then pad the remainder with zeros."""
    length = len(nums)

    read_index = 0
    write_index = 0

    while read_index < length:
        if nums[read_index] != 0:
            nums[write_index] = nums[read_index]
            write_index += 1
        read_index += 1

    while write_index < read_index:
        nums[write_index] = 0
        write_index += 1
