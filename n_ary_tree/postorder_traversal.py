"""Postorder Traversal.

Given the root of an n-ary tree, return the postorder traversal of its nodes' values — a node's
children are all visited before the node itself.
"""

from typing import List, Optional

from n_ary_tree.nary_tree_node import NaryTreeNode


def postorder_traversal(root: Optional[NaryTreeNode]) -> List:
    """Recursively visit each child before appending the current node's value."""
    values = []

    if not root:
        return values

    if root.children:
        for child in root.children:
            values.extend(postorder_traversal(child))
    values.append(root.value)

    return values
