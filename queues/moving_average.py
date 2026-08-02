"""Moving Average from Data Stream (Leetcode).

Given a stream of integers and a window size, calculate the moving average of all integers in the
sliding window.

Example:
`m = MovingAverage(3)`
`m.next(1) -> 1`
`m.next(10) -> (1 + 10) / 2`
`m.next(3) -> (1 + 10 + 3) / 3`
`m.next(5) -> (10 + 3 + 5) / 3`

"""

from collections import deque


class MovingAverage:
    """Maintain a fixed-size sliding window of numbers and report their running average."""

    def __init__(self, max_size: int):
        """Initialize the window with the given maximum size."""
        self.max_size = max_size
        self.queue = deque()

    def next(self, number: int) -> float:
        """Add number to the window, evict the oldest value if over capacity, and return the average."""
        self.queue.append(number)

        if len(self.queue) > self.max_size:
            self.queue.popleft()

        return sum(self.queue) / float(len(self.queue))
