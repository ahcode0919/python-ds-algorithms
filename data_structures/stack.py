"""Stack.

A stack is a LIFO (last in first out) data structure. It can be backed by a list since append and pop are
O(1).
"""

from typing import Generic, TypeVar

T = TypeVar("T")


class StackList(Generic[T]):
    """Stack backed by a list. List append and pop are O(1)."""

    def __init__(self):
        self.__list = []

    def __len__(self):
        return len(self.__list)

    def push(self, data: T):
        """Add data to the top of the stack."""
        self.__list.append(data)

    def pop(self) -> T:
        """Remove and return the element at the top of the stack."""
        return self.__list.pop()
