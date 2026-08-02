"""Reverse String.

Reverse a string. Several approaches are shown, from slicing to an in-place two-pointer swap.
"""

from typing import List, Optional


def reverse_string(string: str) -> str:
    """Reverse the string using slice notation."""
    return string[::-1]


def reverse_string_in_place(string: [str]):
    """Swap characters from both ends inward, mutating the input list of characters in place."""
    index = 0
    length = len(string)
    middle = length / 2
    while index < middle:
        string[index], string[length - 1 - index] = string[length - 1 - index], string[index]
        index += 1


def reverse_string_with_list_comprehension(string: str) -> str:
    """Build the reversed string with a list comprehension iterating indices backwards."""
    return "".join([string[i] for i in range(len(string) - 1, -1, -1)])


def reverse_string_with_loop(string: str) -> str:
    """Build the reversed string by writing each character into its mirrored index of a new list."""
    reversed_str: List[Optional[str]] = [None] * len(string)
    for index in range(len(string) - 1, -1, -1):
        reversed_str[len(string) - 1 - index] = string[index]
    return "".join(reversed_str)
