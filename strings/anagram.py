"""Valid Anagram.

Given two strings, write a function to determine if string A is an anagram of string B (i.e. contains the same
characters with the same frequency, just rearranged).

Example: `"star", "rats"` -> `True`
"""


def valid_anagram(val1: str, val2: str) -> bool:
    """Count characters in val1, then decrement per character in val2 and check every count nets to zero."""
    if len(val1) != len(val2):
        return False

    char_counter = {}

    for char in val1:
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1

    for char in val2:
        if char in char_counter:
            char_counter[char] -= 1
        else:
            return False

    for result in char_counter.values():
        if result != 0:
            return False
    return True
