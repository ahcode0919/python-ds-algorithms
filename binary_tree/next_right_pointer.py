"""Next Right Pointer.

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer
should be set to `None`.
"""

from collections import deque


class Node:
    """Binary tree node with an extra `next` pointer to its right neighbor at the same level."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None


def next_right_pointer(root: Node) -> Node:
    """Breadth-first traverse level by level, linking each node's `next` pointer to its right sibling."""
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
