def plus_one(digits: list[int]) -> list[int]:
    """Plus One.

    Given a non-empty array of digits representing a non-negative integer, add one to the integer. The digits are
    stored such that the most significant digit is at the head of the list, and each element in the array contains a
    single digit. You may assume the integer does not contain any leading zero, except for the number 0 itself.

    Example: `[1, 2, 3]` -> `[1, 2, 4]`

    Add one from the least-significant digit, carrying and inserting a new leading digit as needed.

    :param digits: list of int numbers representing a non-negative number
    :return: incremented list
    """
    for i in reversed(range(len(digits))):
        digits[i] = (digits[i] + 1) % 10
        if digits[i] != 0:
            break
        if i == 0:
            digits.insert(0, 1)
            break
    return digits
