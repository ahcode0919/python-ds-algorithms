
def find_pivot_index(nums: [int]) -> int:
    total = sum(nums)
    left_sum = 0

    for i in range(0, len(nums)):
        if left_sum == total - left_sum - nums[i]:
            return i
        left_sum += nums[i]
    return -1
