"""Valid Palindrome.

A string that is the same forwards and backwards. The naive solution simply reverses and compares; the second
solution accounts for punctuation and case by skipping non-alphanumeric characters and lowercasing before
comparing.
"""


def valid_palindrome_naive(string: str) -> bool:
    """Reverse the string and compare it to the original, with no handling of punctuation or case."""
    return string == string[::-1]


def valid_palindrome(string: str) -> bool:
    """Walk inward from both ends, skipping non-alphanumeric characters, comparing lowercased characters."""
    start = 0
    end = len(string) - 1

    normalized_string = string.lower()

    while start < end:
        if not normalized_string[start].isalnum():
            start += 1
            continue

        if not normalized_string[end].isalnum():
            end -= 1
            continue

        if normalized_string[start] is not normalized_string[end]:
            return False

        start += 1
        end -= 1

    return True
