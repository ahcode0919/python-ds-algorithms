def reverse_number(number: int) -> int:
    """Reverse the digits of a 32-bit signed integer.

    Given a 32-bit signed integer, reverses the digits of its absolute value, then reapplies the
    sign, returning 0 if the reversed value overflows a 32-bit signed integer.

    Example 1: `123` -> `321`
    """
    reversed_number = int(str(abs(number))[::-1])

    if reversed_number > 2**31 - 1:  # Check for integer overflow (per question)
        return 0

    if number < 0:
        return -reversed_number
    return reversed_number
