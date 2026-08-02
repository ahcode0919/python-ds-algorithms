from typing import List


def two_sum(array: List[int], target: int) -> List[int]:
    """Two Sum.

    Given an array of integers, return indices of the two numbers that add up to a specific target. You may assume
    each input has exactly one solution, and you may not use the same element twice.

    Example: `nums = [2, 7, 11, 15], target = 9` -> `[0, 1]` (since `nums[0] + nums[1] = 2 + 7 = 9`)

    Single pass using a value->index hash map of complements. Time: O(N).
    """
    complements = dict()

    for index, number in enumerate(array):
        complement = target - number
        if complement in complements:
            return [complements[complement], index]
        complements[number] = index

    return [-1, -1]
