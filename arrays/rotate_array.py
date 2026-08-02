"""Rotate Array.

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example: `k = 3, [1, 2, 3, 4, 5, 6]` -> `[4, 5, 6, 1, 2, 3]`
"""

from typing import List


def rotate_array_with_array(nums: List[int], k: int) -> List[int]:
    """Build a new array by copying each element to its rotated index. Time: O(N), Space: O(N)."""
    length = len(nums)
    copy = [0] * length

    for index in range(length):
        copy[(index + k) % length] = nums[index]

    return copy


def rotate_array_in_place(nums: List[int], k: int) -> List[int]:
    """Reverse the whole array, then reverse each of the two rotated segments in place."""
    length = len(nums)
    k = k % length

    reverse(nums, 0, length - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, length - 1)
    return nums


def reverse(arr: List, start, end):
    """Reverse arr[start:end + 1] in place using a two-pointer swap."""
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
