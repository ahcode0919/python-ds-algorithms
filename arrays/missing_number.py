from typing import List


def missing_number(nums: List[int]) -> int:
    nums.sort()
    length = len(nums)

    for index in range(length):
        if nums[index] != index:
            return index
    return length


def missing_number_ii(nums: List[int]) -> int:
    length = len(nums)
    expected = (length * (length + 1)) // 2
    total = sum(nums)

    return expected - total
