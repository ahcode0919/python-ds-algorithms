"""Valid Mountain Array.

Given an array of integers, return True if it is a valid mountain array. A valid mountain array has length >= 3,
and there exists some index i with `0 < i < A.length - 1` such that A is strictly increasing from A[0] to A[i]
and strictly decreasing from A[i] to the end.

Example: `[1, 2, 3, 2, 1]` is a valid mountain array.
"""

from typing import List


def valid_mountain_array(arr: List[int]) -> bool:
    """Walk up the increasing run, then confirm a strictly decreasing run finishes the array."""
    length = len(arr)
    if length <= 2:
        return False

    index = 1

    # Check increasing
    while index < length:
        if arr[index - 1] < arr[index]:
            index += 1
        else:
            break

    # Edge case: only increasing, only decreasing
    if index in [length, 1]:
        return False

    # Check decreasing
    while index < length:
        if arr[index - 1] > arr[index]:
            index += 1
        else:
            return False
    return True
