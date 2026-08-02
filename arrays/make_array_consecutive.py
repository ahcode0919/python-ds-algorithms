"""Make Array Consecutive.

Find the number of elements that would need to be added so that each array value is separated by exactly one.

Example: `[1, 2, 3, 5]` -> `1` (a `4` needs to be added to the array)
"""


def make_array_consecutive(values: [int]) -> int:
    """Sort the array, then sum the gaps between consecutive sorted values."""
    length = len(values)
    numbers_needed = 0

    if length <= 1:
        return numbers_needed

    sorted_numbers = sorted(values)

    for i in range(1, length):
        numbers_needed += (sorted_numbers[i] - sorted_numbers[i - 1]) - 1

    return numbers_needed
