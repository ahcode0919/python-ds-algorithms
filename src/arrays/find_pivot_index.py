def find_pivot_index(nums: list[int]) -> int:
    """First Pivot Index.

    Given an array of integers nums, return the "pivot" index of this array. The pivot index is the index where the
    sum of the numbers to the left of the index equals the sum of the numbers to the right of the index. If no such
    index exists, return -1. If there are multiple pivot indexes, return the left-most one.

    Example: `[1, 7, 3, 6, 5, 6]` -> `3`

    Single pass tracking the running left-hand sum against the remaining total.
    """
    total = sum(nums)
    left_sum = 0

    for index, value in enumerate(nums):
        if left_sum == total - left_sum - value:
            return index
        left_sum += value
    return -1
