"""Bubble Sort

The simplest sorting algorithm, working by repeatedly swapping the adjacent elements if they are
in wrong order.

Example: `[2, 1, 3] -> [1, 2, 3]`
"""


def bubble_sort(array: [int]) -> []:
    """Repeatedly swap adjacent out-of-order elements, shrinking the unsorted upper bound each pass."""
    length = len(array)

    # Return if nothing to sort
    if length <= 1:
        return array

    # Reduce the upper limit with each iteration, since the correct value has 'bubbled' to the top
    for i in reversed(range(0, length)):
        swap = False
        # Compare value and switch up to the upper limit 'i'
        for j in range(0, i):
            next_val = j + 1
            if next_val < length and array[j] > array[next_val]:
                temp = array[j]
                array[j] = array[next_val]
                array[next_val] = temp
                swap = True

        # Return if no swaps take place
        if not swap:
            return array
    return array
