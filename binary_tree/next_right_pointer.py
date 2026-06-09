from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None


def next_right_pointer(root: Node) -> Node:
    if not root:
        return root

    level = deque([root])

    while level:
        right = None

        for _ in range(len(level)):
            left = level.pop()
            left.next = right
            right = left
            if left.right:
                level.appendleft(left.right)
            if left.left:
                level.appendleft(left.left)

    return root
