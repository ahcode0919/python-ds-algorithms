"""Even Odd Tree.

A binary tree is named even-odd if it meets the following conditions:

For every even-indexed level (0, 2, 4, etc), all nodes at the level have odd integer values in strictly increasing
order (from left to right).

For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from
left to right).

Given the root of a binary tree, return `True` if the binary tree is even-odd, otherwise return `False`.
"""

from collections import deque
from typing import Optional

from binary_tree.tree_node import TreeNode


def even_odd_tree(root: Optional[TreeNode]):
    """Level-order traverse the tree, validating each level against the even/odd parity and ordering rules."""
    if not root:
        return False

    level = deque([root])
    even = True

    while level:
        last_value = None

        for _ in range(len(level)):
            node = level.popleft()

            if even:
                if not validate_even(node, last_value):
                    return False
            else:
                if not validate_odd(node, last_value):
                    return False

            last_value = node.val

            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        even = not even

    return True


def validate_even(node: TreeNode, last_value: Optional[int]) -> bool:
    """Check that a node's value is odd and, on an even level, strictly greater than the previous value."""
    if node.val % 2 == 0:
        return False
    if last_value and node.val <= last_value:
        return False
    return True


def validate_odd(node: TreeNode, last_value: Optional[int]) -> bool:
    """Check that a node's value is even and, on an odd level, strictly less than the previous value."""
    if node.val % 2 != 0:
        return False
    if last_value and node.val >= last_value:
        return False
    return True
