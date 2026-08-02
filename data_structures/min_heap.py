"""Min Heap.

A Min Heap is a complete binary tree where every parent node is smaller than or equal to its children. The
smallest element is always at the root. It is commonly backed by an array where for a node at index `i`,
its parent is at `(i - 1) // 2` and its children are at `2i + 1` and `2i + 2`.

New values are inserted at the end of the array and then "sifted up" - repeatedly swapped with their parent
until the heap property is restored.
"""


class MinHeap:
    def __init__(self):
        self.list = []

    def insert(self, val):
        """Add val to the end of the array, then sift it up until the heap property is restored."""
        self.list.append(val)
        self._sift_up(len(self.list) - 1)

    def is_empty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)

    def values(self):
        values = []
        for value in self.list:
            values.append(value)
        return values

    def _get_parent(self, idx):
        return (idx - 1) // 2

    def _sift_up(self, idx):
        """Repeatedly swap the value at idx with its parent until it is no longer smaller than its parent."""
        current_index = idx

        while current_index > 0:
            parent = self._get_parent(current_index)

            if self.list[current_index] < self.list[parent]:
                self.list[current_index], self.list[parent] = (
                    self.list[parent],
                    self.list[current_index],
                )
                current_index = parent
            else:
                break
