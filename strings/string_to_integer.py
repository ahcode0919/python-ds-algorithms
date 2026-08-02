"""String to Integer.

Convert a string to an integer. The string may include spaces before and after the number, and may end in words,
which should be ignored.
"""


def string_to_integer(string: str) -> int:
    """Skip leading spaces and an optional minus sign, then parse and return the leading run of digits."""
    length = len(string)
    numbers = set(list("1234567890"))
    positive = True
    start_index = -1

    if length < 1:
        return 0

    for index in range(length):
        if string[index] in " ":
            continue

        if string[index] in "-":
            positive = False
            continue

        if string[index] not in numbers:
            return 0

        if string[index] in numbers:
            start_index = index
            break

    # Handle empty string (no numbers)
    if start_index == -1:
        return 0

    end_index = start_index

    for index in range(start_index, length):
        if string[index] in numbers:
            end_index += 1
        else:
            break

    return int(string[start_index:end_index]) if positive else -int(string[start_index:end_index])
