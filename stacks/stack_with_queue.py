"""Implement Stack with Queue.

Implement the following operations of a stack using queues: `push(x)` pushes element x onto the stack, `pop()`
removes the element on top of the stack, `top()` gets the top element, and `empty()` returns whether the stack is
empty.

Example: `stack.push(1)`, `stack.push(2)`, then `stack.top()` returns `2`, `stack.pop()` returns `2`, and
`stack.empty()` returns `False`.
"""

from collections import deque
from typing import Deque, Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """LIFO stack implemented on top of a deque used as the underlying queue-like structure."""

    def __init__(self):
        self.stack: Deque[T] = deque()

    def push(self, item: T) -> None:
        """Push item onto the top of the stack."""
        self.stack.append(item)

    def pop(self) -> T:
        """Remove and return the item on top of the stack."""
        return self.stack.pop()

    def top(self) -> T:
        """Return the item on top of the stack without removing it."""
        return self.stack[-1]

    def empty(self) -> bool:
        """Return whether the stack has no items."""
        return len(self.stack) == 0
