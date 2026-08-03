def find_smallest_positive_integer(arr: list[int]) -> int:
    """Find Smallest Positive Integer.

    Find the smallest positive integer in an array. Return zero if there are no positive integers.

    Example: `[1, -2, 3]` -> `1`

    Single pass tracking the smallest positive value seen so far.
    """
    smallest = -1

    for i in range(len(arr)):
        if arr[i] > 0:
            if smallest == -1:
                smallest = arr[i]
            elif arr[i] < smallest:
                smallest = arr[i]

    if smallest == -1:
        return 0
    return smallest
