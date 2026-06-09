from typing import List
from n_ary_tree.nary_tree_node import NaryTreeNode


def preorder_traversal_iterative(root: NaryTreeNode) -> List:
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
