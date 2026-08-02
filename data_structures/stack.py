from typing import Generic, TypeVar

T = TypeVar("T")


class StackList(Generic[T]):
    """Stack.

    A stack is a LIFO (last in first out) data structure. It is backed here by a list, since list append
    and pop are both O(1).
    """

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
