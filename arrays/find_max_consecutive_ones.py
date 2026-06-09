from typing import List


def find_max_consecutive_ones(nums: List[int]) -> int:
    max_ones = 0

    if not nums:
        return max_ones

    ones_count = 0

    for num in nums:
        if num == 1:
            ones_count += 1
        else:
            ones_count = 0

        max_ones = max(max_ones, ones_count)

    return max_ones
