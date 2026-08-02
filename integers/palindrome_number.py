"""Palindrome Number.

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same
backward as forward.

Example 1: `121` -> `true`

Example 2: `-121` -> `false`

Explanation: From left to right, it reads `-121`. From right to left, it becomes `121-`. Therefore it
is not a palindrome.
"""


def is_palindrome(a_string: int) -> bool:
    """Convert to a string and compare it against its reverse."""
    num = str(a_string)
    return num == num[::-1]
