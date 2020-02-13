from collections import deque
from typing import Deque


def decode_string(value: str) -> str:
    group = 0
    output: Deque = deque()
    stack: Deque = deque()

    for char in reversed(value):
        if char in ']':
            group += 1
            continue

        if char in '[':
            continue

        if char.isdigit():
            multiplier = int(char)
            chars = []
            group -= 1

            for _ in range(len(stack)):
                chars.append(stack.pop())

            if group == 0:
                output.extendleft(reversed(chars * multiplier))
            else:
                stack.extend(chars * multiplier)
        else:
            if group == 0:
                output.appendleft(char)
            else:
                stack.append(char)
    return ''.join(list(output))
