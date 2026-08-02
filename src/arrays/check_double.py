def check_double(arr: list[int]) -> bool:
    """Check Double.

    Given an array arr of integers, check if there exist two integers N and M such that N is the double of M (i.e.
    N = 2 * M). More formally, check if there exist two indices i and j such that i != j and arr[i] == 2 * arr[j].

    Example: `arr = [10, 2, 5, 3]` -> `True` (`N = 10` is the double of `M = 5`, since `10 = 2 * 5`)

    Track seen values in a set and check for a value's double or half on each pass.
    """
    elements = set()

    for num in arr:
        if num * 2 in elements:
            return True
        if num % 2 == 0 and num / 2 in elements:
            return True
        elements.add(num)

    return False
