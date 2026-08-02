"""Preorder Traversal (Iterative).

Given the root of an n-ary tree, return the preorder traversal of its nodes' values — a node's
value is visited before its children.
"""

from typing import List

from n_ary_tree.nary_tree_node import NaryTreeNode


def preorder_traversal_iterative(root: NaryTreeNode) -> List:
    """Push nodes onto a stack, children in reverse order, to visit them in preorder."""
    if not root:
        return []

    stack = [root]
    values = []

    while stack:
        node = stack.pop()
        values.append(node.value)

        if node.children:
            for child in reversed(node.children):
                stack.append(child)

    return values
