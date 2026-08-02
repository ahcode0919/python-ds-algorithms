from typing import List


def count_elements(arr: List[int]) -> int:
    """Count Elements.

    Given an integer array arr, count how many elements x there are such that x + 1 is also in arr. If there are
    duplicates in arr, count them separately.

    Build a set of values, then count elements whose successor is also present.
    """
    elements = set()
    counter = 0

    for element in arr:
        elements.add(element)

    for element in arr:
        if element + 1 in elements:
            counter += 1

    return counter
