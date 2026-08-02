def find_max_consecutive_ones(nums: list[int]) -> int:
    """Find Max Consecutive Ones.

    You are given a binary array nums; return the maximum number of consecutive 1's in the array.

    Example: `nums = [1, 1, 0, 1, 1, 1]` -> `3`
    Example: `nums = [1, 0, 1, 1, 0, 1]` -> `2`

    Single pass tracking a running streak of 1s and the best streak seen.
    """
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
