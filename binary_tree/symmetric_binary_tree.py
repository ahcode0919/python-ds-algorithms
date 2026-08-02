from typing import Optional

from binary_tree.tree_node import TreeNode


def symmetric_binary_tree(root: Optional[TreeNode]) -> bool:
    r"""Symmetric Binary Tree.

    Given a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

    For example, this binary tree `[1, 2, 2, 3, 4, 4, 3]` is symmetric:

    ```text
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    ```

    But the following `[1, 2, 2, null, 3, null, 3]` is not:

    ```text
        1
       / \
      2   2
       \   \
       3    3
    ```

    Compares each level from the outside in, mirroring left and right positions, to check for symmetry.
    """
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
