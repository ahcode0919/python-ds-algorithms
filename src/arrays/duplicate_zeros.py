def duplicate_zeros(arr: list[int]) -> list[int]:
    """Duplicate Zeros.

    Duplicate the zeros in the supplied array. Excess values should be discarded so that the array remains the same
    size.

    Example: `[1, 0, 2, 3, 0, 4, 5, 6]` -> `[1, 0, 0, 2, 3, 0, 0, 4]`

    Time: O(N), Space: O(N)

    Build a shifted stack of values with zeros duplicated, then write it back in place.
    """
    stack = []
    index = 0
    length = len(arr)

    while len(stack) < length:
        stack.append(arr[index])

        if len(stack) < length and arr[index] == 0:
            stack.append(0)
        index += 1

    for i in range(length - 1, -1, -1):
        arr[i] = stack.pop()

    return arr
