from typing import List


def find_index_largest_number(numbers: List[int]) -> int:
    """Find Index of Largest Number.

    Find the index of the largest number in a list. Return -1 if the list is empty.

    Single pass tracking the index of the largest value seen so far.
    """
    if not numbers:
        return -1

    largest_index = numbers[0]

    for index in range(1, len(numbers)):
        if numbers[index] > numbers[largest_index]:
            largest_index = index
    return largest_index
