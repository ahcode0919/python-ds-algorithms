def str_str(haystack: str, needle: str) -> int:
    """Implement strStr.

    Implement `strStr()`. Return the index of the first occurrence of needle in haystack, or -1 if needle is not
    part of haystack. If needle is empty, return 0.

    Slide a window the length of needle across haystack, returning the first index where it matches.
    """
    if not needle:
        return 0

    length_haystack = len(haystack)
    length_needle = len(needle)

    for index in range(length_haystack):
        if haystack[index : index + length_needle] == needle:
            return index
    return -1
