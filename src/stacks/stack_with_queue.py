from collections import deque


class Stack:
    """Implement Stack with Queue.

    Implement the following operations of a stack using queues: `push(x)` pushes element x onto the stack, `pop()`
    removes the element on top of the stack, `top()` gets the top element, and `empty()` returns whether the stack
    is empty.

    LIFO stack implemented on top of a deque used as the underlying queue-like structure.

    Example: `stack.push(1)`, `stack.push(2)`, then `stack.top()` returns `2`, `stack.pop()` returns `2`, and
    `stack.empty()` returns `False`.
    """

    def __init__(self):
        self.stack: deque[object] = deque()

    def push(self, item: object) -> None:
        """Push item onto the top of the stack."""
        self.stack.append(item)

    def pop(self) -> object:
        """Remove and return the item on top of the stack."""
        return self.stack.pop()

    def top(self) -> object:
        """Return the item on top of the stack without removing it."""
        return self.stack[-1]

    def empty(self) -> bool:
        """Return whether the stack has no items."""
        return len(self.stack) == 0
