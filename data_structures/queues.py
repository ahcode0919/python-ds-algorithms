"""Queue.

A Queue is a FIFO (first in first out) data structure. The simplest analogy would be waiting in line.

::

    Front             Back
        [1, 2, 3, 4]
    Remove values from the front and add new values to the back
    Enqueue - Add new value to the back
    Dequeue - Remove value from the front

Three implementations are provided below, plus the built-in `collections.deque` which can also be used
directly as a queue (`queue.append(1)` to enqueue, `queue.popleft()` to dequeue).
"""

from typing import Generic, List, TypeVar

from data_structures.doubly_linked_list import DoublyLinkedList

T = TypeVar("T")


class QueueList(Generic[T]):
    """Basic queue backed with a list.

    Not optimal since list has O(N) complexity for inserting and removing elements at the beginning
    """

    def __init__(self):
        self.queue: List[T] = []

    def __len__(self):
        return len(self.queue)

    def dequeue(self) -> T:
        """Remove and return the element at the front of the queue."""
        return self.queue.pop(0)

    def enqueue(self, element: T):
        """Add element to the back of the queue."""
        self.queue.append(element)


class QueueLinkedList(Generic[T]):
    """Queue backed by a doubly linked list."""

    def __init__(self):
        self.linked_list = DoublyLinkedList()

    def __len__(self):
        return self.linked_list.size()

    # O(1)
    def dequeue(self) -> T:
        """Remove and return the element at the front of the queue."""
        return self.linked_list.remove(0)

    # O(1)
    def enqueue(self, element: T):
        """Add element to the back of the queue."""
        self.linked_list.append(element)


class CircularQueue(Generic[T]):
    """Queue backed by a fixed-size array, wrapping the head/tail indices to reuse freed slots.

    Similar to the linked-list queue in time complexity but uses an array to mimic the same functionality.
    """

    def __init__(self, k: int):
        self.queue = [0] * k
        self.count = 0
        self.size = k
        self.head = 0

    def enqueue(self, value: T) -> bool:
        """Add value to the back of the queue. Return False if the queue is full."""
        if self.isfull():
            return False
        tail = (self.head + self.count) % self.size
        self.queue[tail] = value
        self.count += 1
        return True

    def dequeue(self) -> bool:
        """Remove the element at the front of the queue. Return False if the queue is empty."""
        if self.isempty():
            return False
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return True

    def front(self) -> T:
        """Get the front item from the queue."""
        if self.isempty():
            return -1
        return self.queue[self.head]

    def rear(self) -> T:
        """Get the last item from the queue."""
        if self.isempty():
            return -1
        tail = (self.head + self.count - 1) % self.size
        return self.queue[tail]

    def isempty(self) -> bool:
        return self.count == 0

    def isfull(self) -> bool:
        return self.count == self.size
