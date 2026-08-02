"""Third Max.

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return
the maximum number instead.

Example: `[3, 2, 1]` -> `1`
Example: `[1, 2]` -> `2` (the third maximum does not exist, so the maximum is returned instead)
"""

from typing import List


def third_max(nums: List[int]) -> int:
    """Deduplicate with a set, then remove the two largest values and return what remains as the max."""
    unique_nums = set(nums)

    if len(unique_nums) < 3:
        return max(unique_nums)

    unique_nums.remove(max(unique_nums))  # 1st
    unique_nums.remove(max(unique_nums))  # 2nd
    return max(unique_nums)  # 3rd
