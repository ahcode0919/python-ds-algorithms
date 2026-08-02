"""Add Binary.

Given two binary strings, return their sum (also a binary string). The input strings are both non-empty and
contain only the characters 1 or 0.

Example: `"11", "1"` -> `"100"`
Example: `"1010", "1011"` -> `"10101"`
"""

from collections import deque


def add_binary(num1: str, num2: str) -> str:
    """Add the strings bit by bit from the right, tracking carry manually."""
    length_a = len(num1)
    length_b = len(num2)
    max_length = max(length_a, length_b)
    output = deque()
    carry = 0

    num1 = ("0" * (max_length - length_a)) + num1
    num2 = ("0" * (max_length - length_b)) + num2

    for index in range(max_length - 1, -1, -1):
        if num1[index] == "1":
            carry += 1
        if num2[index] == "1":
            carry += 1

        if carry % 2 == 1:
            output.appendleft("1")
        else:
            output.appendleft("0")

        carry //= 2

    if carry == 1:
        output.appendleft("1")

    return "".join(output)


def add_binary_with_builtins(num1: str, num2: str) -> str:
    """Convert both operands to int, add, then convert the result back to a binary string."""
    return str(bin(int(num1, 2) + int(num2, 2)))[2:]
