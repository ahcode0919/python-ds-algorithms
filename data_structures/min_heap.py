class MinHeap:
    def __init__(self):
        self.list = []

    def insert(self, val):
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
