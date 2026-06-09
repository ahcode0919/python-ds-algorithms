from typing import List
from n_ary_tree import nary_tree_node


def preorder_traversal(root: nary_tree_node) -> List:
    if not root:
        return []

    values = [root.value]

    if not root.children:
        return values

    for child in root.children:
        values.extend(preorder_traversal(child))

    return values
