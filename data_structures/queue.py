from typing import Generic


class QueueList:
    """
    Basic queue backed with a list. Not optimal since list has O(N) complexity for
    inserting and removing elements at the beginning
    """

    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def dequeue(self) -> Generic:
        return self.queue.pop(0)

    def enqueue(self, element: Generic):
        self.queue.append(element)
