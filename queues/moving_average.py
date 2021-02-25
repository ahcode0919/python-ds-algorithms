from collections import deque


class MovingAverage:

    def __init__(self, max_size: int):
        self.max_size = max_size
        self.queue = deque()

    def next(self, number: int) -> float:
        self.queue.append(number)

        if len(self.queue) > self.max_size:
            self.queue.popleft()

        return sum(self.queue) / float(len(self.queue))
