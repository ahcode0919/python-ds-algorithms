"""Find Disappeared Numbers.

Given an array of integers where `1 <= a[i] <= n` (n = size of array), some elements appear twice and others
appear once. Find all the elements of `[1, n]` inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra
space.

Example: `[4, 3, 2, 7, 8, 2, 3, 1]` -> `[5, 6]`
"""


def find_disappeared_numbers(nums: list[int]) -> list[int]:
    """O(N) time, O(N) space using a set of seen values."""
    unique_nums = set(nums)
    length = len(nums)
    disappeared_nums = []

    for num in range(1, length + 1):
        if num not in unique_nums:
            disappeared_nums.append(num)
    return disappeared_nums


def find_disappeared_numbers_ii(nums: list[int]) -> list[int]:
    """O(N) time, O(1) extra space by negating values at visited indices in place."""
    length = len(nums)

    for index in range(length):
        num_index = abs(nums[index]) - 1
        if nums[num_index] > 0:
            nums[num_index] *= -1

    disappeared_nums = []

    for index in range(length):
        if nums[index] > 0:
            disappeared_nums.append(index + 1)
    return disappeared_nums
