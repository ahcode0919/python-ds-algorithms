from typing import List


def intersection_of_two_arrays(nums1: List[int], nums2: List[int]) -> List[int]:
    """Intersection of Two Arrays.

    Given two arrays, write a function that computes their intersection, including duplicate matches.

    Example: `nums1 = [1, 2, 2, 1], nums2 = [2, 2]` -> `[2, 2]`

    Count nums1 occurrences in a hash map, then consume matches while scanning nums2.
    """
    intersection = []
    nums1_map = {}

    for num in nums1:
        if num in nums1_map:
            nums1_map[num] += 1
        else:
            nums1_map[num] = 1

    for num in nums2:
        if num in nums1_map and nums1_map[num] > 0:
            intersection.append(num)
            nums1_map[num] -= 1

    return intersection
