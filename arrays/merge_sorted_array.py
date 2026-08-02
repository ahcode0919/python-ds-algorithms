"""Merge Sorted Array.

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array. The number of
elements initialized in nums1 and nums2 are m and n respectively. Assume nums1 has enough space (size m + n) to
hold the additional elements from nums2.

Example: `nums1 = [1, 2, 3, 0, 0, 0], m = 3`, `nums2 = [2, 5, 6], n = 3` -> `[1, 2, 2, 3, 5, 6]`
"""

from typing import List


def merge_sorted_array(
    nums1: List[int], nums1_length: int, nums2: List[int], nums2_length: int
) -> List[int]:
    """Fill nums1 from the back, comparing the largest remaining elements of each array."""
    index_nums1 = nums1_length - 1
    index_nums2 = nums2_length - 1
    current_index = nums1_length + nums2_length - 1

    while index_nums2 >= 0:
        if index_nums1 < 0 <= index_nums2:
            nums1[current_index] = nums2[index_nums2]
            index_nums2 -= 1
        elif nums1[index_nums1] > nums2[index_nums2]:
            nums1[current_index] = nums1[index_nums1]
            index_nums1 -= 1
        else:
            nums1[current_index] = nums2[index_nums2]
            index_nums2 -= 1

        current_index -= 1

    return nums1
