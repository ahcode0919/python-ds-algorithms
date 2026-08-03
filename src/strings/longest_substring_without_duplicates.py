def longest_substring_without_duplicates(string: str) -> int:
    """Longest Substring Without Duplicates.

    Find the length of the longest substring of a string that contains no repeated characters.

    Example: `"abcabedfg"` -> `7` (the length of `"cabedfg"`)

    Slide a window with two pointers, expanding right while characters are unique and shrinking left otherwise.
    """
    length = len(string)
    left_index = 0
    right_index = 0
    longest = 0

    unique = set()

    while right_index < length and left_index < length:
        if string[right_index] not in unique:
            unique.add(string[right_index])
            right_index += 1
            longest = max(longest, right_index - left_index)
        else:
            unique.remove(string[left_index])
            left_index += 1
    return longest
