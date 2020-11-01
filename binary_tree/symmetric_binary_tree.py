from binary_tree.tree_node import TreeNode
from typing import Optional


def symmetric_binary_tree(root: Optional[TreeNode]) -> bool:
    level = [root]

    while level:
        next_level = []
        left = 0
        right = len(level) - 1

        while left <= right:
            left_val = level[left].val if level[left] else None
            right_val = level[right].val if level[right] else None

            if left_val != right_val:
                return False

            left += 1
            right -= 1

        for node in level:
            if node:
                next_level.append(node.left)
                next_level.append(node.right)

        level = next_level

    return True
