from typing import List


def replace_elements_with_greatest(arr: List[int]) -> List[int]:
    """Replace Elements with Greatest Element on Right Side.

    Given an array arr, replace every element in that array with the greatest element among the elements to its
    right, and replace the last element with -1.

    Example: `[17, 18, 5, 4, 6, 1]` -> `[18, 6, 6, 6, 1, -1]`

    Constraints: `1 <= arr.length <= 10^4`, `1 <= arr[i] <= 10^5`

    Right-to-left pass tracking the max seen so far, writing before updating.
    """
    length = len(arr)
    max_number = -1

    for index in range(length - 1, -1, -1):
        temp = arr[index]
        arr[index] = max_number
        max_number = max(temp, max_number)

    return arr
