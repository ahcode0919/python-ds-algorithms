"""Multiply Strings.

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also
represented as a string.

Constraints:
- The length of both num1 and num2 is less than 110.
- Both num1 and num2 contain only digits 0-9.
- Neither num1 nor num2 contains a leading zero, except the number 0 itself.
- Built-in BigInteger libraries and directly converting the inputs to integers are not allowed.

Example: `num1 = "123"`, `num2 = "456"` -> `"56088"`
"""


def multiply_strings(num1: str, num2: str) -> str:
    """Convert each operand to an int via manual digit parsing, multiply, then stringify the result."""

    def string_to_int(string: str) -> int:
        """Parse a digit string into an int by summing each character's place value."""
        length = len(string)
        zero = ord("0")
        value = 0

        for index in range(length):
            temp = ord(string[index]) - zero
            value += temp * (10 ** (length - index - 1))
        return value

    return str(string_to_int(num1) * string_to_int(num2))
