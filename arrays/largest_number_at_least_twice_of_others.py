"""Largest Number At Least Twice of Others.

In a given integer array nums, there is always exactly one largest element. Determine whether the largest
element is at least twice as large as every other number in the array. If it is, return the index of the largest
element; otherwise return -1.

Example: `[3, 6, 1, 0]` -> `1`
"""


def largest_number_at_least_twice_of_others(nums: list[int]) -> int:
    """Single pass tracking the largest and second-largest indices.

    :param nums: array of numbers
    :return: index of number, -1 if none exists
    """
    largest = None
    next_largest = None

    for idx, num in enumerate(nums):
        if largest is None:
            largest = idx
            continue
        if num > nums[largest]:
            next_largest = largest
            largest = idx
            continue
        if next_largest is None or num > nums[next_largest]:
            next_largest = idx

    if next_largest is None or (nums[next_largest] * 2) <= nums[largest]:
        return largest
    return -1


def largest_number_at_least_twice_of_others2(nums: list[int]) -> int:
    """Array-manipulation approach using built-in max()/index(); simpler but mutates the input via pop().

    :param nums: array of numbers
    :return: index of number, -1 if none exists
    """
    if len(nums) == 1:
        return 0

    max_index = nums.index(max(nums))
    max_val = nums.pop(max_index)
    next_max = max(nums)

    if next_max * 2 <= max_val:
        return max_index
    return -1
