"""First Duplicate.

Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for
which the second occurrence has the minimal index. In other words, if there is more than one duplicated number,
return the number whose second occurrence has a smaller index than the second occurrence of the other number. If
there are no such elements, return -1.
"""


def first_duplicate(array: list[int]) -> int:
    """Count occurrences with a dict, then return the first value whose count exceeds one."""
    number_counter = dict()
    for value in array:
        if value in number_counter:
            number_counter[value] += 1
        else:
            number_counter[value] = 1

    for value in array:
        if number_counter[value] > 1:
            return value
    return -1


def first_duplicate_in_place(array: list[int]) -> int:
    """Repeatedly pop the front element and check membership in the remaining array."""
    while len(array) > 0:
        value = array.pop(0)
        if value in array:
            return value
    return -1
