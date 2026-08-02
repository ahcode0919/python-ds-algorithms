def is_palindrome(a_string: int) -> bool:
    """Determine whether an integer is a palindrome.

    An integer is a palindrome when it reads the same backward as forward. Converts the number to
    a string and compares it against its reverse.

    Example 1: `121` -> `true`

    Example 2: `-121` -> `false`

    Explanation: From left to right, it reads `-121`. From right to left, it becomes `121-`.
    Therefore it is not a palindrome.
    """
    num = str(a_string)
    return num == num[::-1]
