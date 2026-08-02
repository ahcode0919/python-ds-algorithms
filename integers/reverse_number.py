"""Reverse Number.

Given a 32-bit signed integer, reverse digits of an integer.

Example 1: `123` -> `321`
"""


def reverse_number(number: int) -> int:
    """Reverse the digits of the absolute value, then reapply the sign, checking for 32-bit overflow."""
    reversed_number = int(str(abs(number))[::-1])

    if reversed_number > 2**31 - 1:  # Check for integer overflow (per question)
        return 0

    if number < 0:
        return -reversed_number
    return reversed_number
