"""Sorted Squares.

Given a sorted array of numbers, return the squares of each number in ascending order.

Example: `[-2, -1, 0, 1, 3]` -> `[0, 1, 1, 4, 9]`
"""

from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    """Two-pointer merge from the point where values turn non-negative, comparing magnitudes outward."""
    length = len(nums)
    first_positive = None

    for index in range(length):
        if nums[index] >= 0:
            first_positive = index
            break

    # All Negative
    if first_positive is None:
        result = []
        for index in range(length - 1, -1, -1):
            result.append(nums[index] * nums[index])
        return result

    # All Positive
    if first_positive == 0:
        return [x * x for x in nums]

    left = first_positive - 1
    right = first_positive
    squares = []

    while left >= 0 and right < length:
        if abs(nums[left]) < nums[right]:
            squares.append(nums[left] * nums[left])
            left -= 1
        else:
            squares.append(nums[right] * nums[right])
            right += 1

    while right < length:
        squares.append(nums[right] * nums[right])
        right += 1

    while left >= 0:
        squares.append(nums[left] * nums[left])
        left -= 1

    return squares
