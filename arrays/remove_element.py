from typing import List


def remove_element(nums: List[int], val: int) -> int:
    """Remove Element.

    Given an array nums and a value val, remove all instances of that value in-place and return the new length. Do
    not allocate extra space for another array; modify the input array in-place with O(1) extra memory. The order of
    elements can be changed, and it doesn't matter what is left beyond the new length.

    Example: `nums = [3, 2, 2, 3], val = 3` -> length `2`, with the array mutated to `[2, 2, ...]`

    Single pass shifting kept elements left by the count of removed matches seen so far.
    """
    index = 0
    count = 0
    length = len(nums)

    while index < length:
        if nums[index] == val:
            count += 1
        else:
            nums[index - count] = nums[index]
        index += 1
    return length - count
