from typing import List


def peaks(numbers: List[int]) -> List[int]:
    """Peaks.

    Given an array of integers, return the values that are between two smaller values.

    Example: `[1, 3, 2]` -> `[3]`

    Single pass comparing each interior element against its neighbors.
    """
    length = len(numbers)
    peak_nums = []

    if length < 3:
        return peak_nums

    for index in range(1, length - 1):
        if numbers[index - 1] < numbers[index] and numbers[index] > numbers[index + 1]:
            peak_nums.append(numbers[index])

    return peak_nums
