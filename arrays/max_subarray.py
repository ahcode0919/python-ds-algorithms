from typing import List


def max_subarray(nums: List[int]) -> int:
    length = len(nums)
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, length):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum
