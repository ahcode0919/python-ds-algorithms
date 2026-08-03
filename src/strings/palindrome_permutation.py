from collections import Counter


def palindrome_permutation(palindrome: str) -> bool:
    """Palindrome Permutation.

    Given a string, determine if a permutation of the string could form a palindrome.

    Example: `"code"` -> `False`
    Example: `"aab"` -> `True`
    Example: `"carerac"` -> `True`

    Count character frequencies and check that at most one character has an odd count.
    """
    length = len(palindrome)
    counter = Counter(list(palindrome))

    if length % 2 == 0:
        for key in counter:
            if counter[key] % 2 != 0:
                return False
    else:
        ones_count = Counter(counter.values()).get(1)
        if ones_count and ones_count > 1:
            return False

    return True
