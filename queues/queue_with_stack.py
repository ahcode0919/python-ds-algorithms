from collections import deque


class Queue:
    """Implement Queue With Stack.

    A FIFO queue backed by a double-ended queue used as a stack-like container.

    Implement the following operations of a queue using stacks: `push(x)` -- push element x to
    the back of queue; `pop()` -- removes the element from in front of queue; `peek()` -- get the
    front element; `empty()` -- return whether the queue is empty.

    Example:
    ```
    queue = MyQueue()

    queue.push(1)
    queue.push(2)
    queue.peek()  # returns 1
    queue.pop()  # returns 1
    queue.empty()  # returns false
    ```

    """

    def __init__(self):
        """Initialize an empty queue."""
        self.queue: deque[object] = deque()

    def push(self, item: object) -> None:
        """Push element item to the back of the queue."""
        self.queue.append(item)

    def pop(self) -> object:
        """Remove and return the element from the front of the queue."""
        return self.queue.popleft()

    def peek(self) -> object:
        """Return the element at the front of the queue without removing it."""
        return self.queue[0]

    def empty(self) -> bool:
        """Return whether the queue is empty."""
        return len(self.queue) == 0
