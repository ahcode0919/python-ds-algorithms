"""String to Integer II.

Convert a number string to an integer. The number may be prefixed with `-` or `+`.

Example: `"-34"` -> `-34`
Example: `"100"` -> `100`
"""


def string_to_integer_ii(string: str) -> int:
    """Detect an optional sign prefix, then accumulate the integer value digit by digit via place value."""
    zero = ord("0")
    positive = True
    length = len(string)
    start = 0
    number = 0

    if length < 1:
        return 0

    # Determine Positive / Negative
    if string[0] == "-":
        start = 1
        positive = False
    elif string[0] == "+":
        start = 1

    # Iterate over remaining characters
    for index in range(start, length):
        temp = ord(string[index]) - zero
        number += temp * (10 ** (length - index - 1))

    return number if positive else number * -1
