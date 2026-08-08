class UnionFind:
    def __init__(self):
        self.roots = []

    def add_edges(self, n: int, edges: list[tuple[int, int]]):
        self.roots = [number for number in range(n)]
        for edge in edges:
            a, b = edge
            self.union(a, b)

    def components(self) -> int:
        count = 0

        for index in range(len(self.roots)):
            if self.roots[index] == index:
                count += 1

        return count

    def union(self, a: int, b: int):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a is not None and root_b is not None:
            self.roots[root_a] = root_b

    def find(self, node1: int) -> None | int:
        stack = [node1]

        while stack:
            current = stack.pop()
            if self.roots[current] == current:
                return current
            stack.append(self.roots[current])
        return None

    def size(self) -> int:
        return len(self.roots)
