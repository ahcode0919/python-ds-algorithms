"""Intersection of Three Sorted Arrays.

Given three integer arrays arr1, arr2, and arr3 sorted in strictly increasing order, return a sorted array of
only the integers that appear in all three arrays.

Example: `arr1 = [1, 2, 3, 4, 5], arr2 = [1, 2, 5, 7, 9], arr3 = [1, 3, 4, 5, 8]` -> `[1, 5]`
"""

from typing import List


def arrays_intersection(arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    """Set-intersection approach across all three arrays."""
    intersection = set(arr1)
    intersection = intersection.intersection(arr2)
    return list(intersection.intersection(arr3))


def arrays_intersection2(arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    """Three-pointer sweep exploiting the sorted order of each array."""
    index1 = 0
    index2 = 0
    index3 = 0
    result = []

    while index1 < len(arr1) and index2 < len(arr2) and index3 < len(arr3):
        if arr1[index1] == arr2[index2] == arr3[index3]:
            result.append(arr1[index1])
            index1 += 1
            index2 += 1
            index3 += 1
            continue

        current_max = max(arr1[index1], arr2[index2], arr3[index3])

        if arr1[index1] < current_max:
            index1 += 1
        if arr2[index2] < current_max:
            index2 += 1
        if arr3[index3] < current_max:
            index3 += 1

    return result
