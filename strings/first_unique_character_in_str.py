"""First Unique Character In A String.

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Example: `"ilovecoding"` -> index of `"l"`
"""


def first_unique_character_in_str(val: str) -> int:
    """Count character frequencies, then return the index of the first character with a count of one."""
    chars = {}

    for char in val:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    for index, char in enumerate(val):
        if chars[char] == 1:
            return index

    return -1
