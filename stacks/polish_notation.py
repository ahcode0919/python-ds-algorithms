"""Evaluate Reverse Polish Notation.

Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /; each
operand may be an integer or another expression. Division between two integers should truncate toward zero. The
given RPN expression is always valid, so it will always evaluate to a result and there won't be any divide by
zero operation.

Example: `["2", "1", "+", "3", "*"]` -> `9`, since `((2 + 1) * 3) = 9`
Example: `["4", "13", "5", "/", "+"]` -> `6`, since `(4 + (13 / 5)) = 6`
"""

from math import trunc
from queue import LifoQueue
from typing import List


def evaluate_rpn(tokens: List[str]) -> int:
    """Evaluate RPN tokens using a stack, applying each operator to the two most recent operands."""
    stack = LifoQueue()

    for token in tokens:
        if token.lstrip("-").isdigit():
            stack.put(token)
        else:
            right = int(stack.get())
            left = int(stack.get())
            stack.put(compute(left, right, token))

    return stack.get()


def compute(left: int, right: int, operator: str) -> int:
    """Apply the given operator to the left and right operands."""
    if operator == "-":
        return left - right
    if operator == "+":
        return left + right
    if operator == "/":
        return trunc(float(left) / right)
    return left * right
