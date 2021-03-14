from typing import List, Optional
from n_ary_tree.nary_tree_node import NaryTreeNode


def postorder_traversal(root: Optional[NaryTreeNode]) -> List:
    values = []

    if not root:
        return values

    if root.children:
        for child in root.children:
            values.extend(postorder_traversal(child))
    values.append(root.value)

    return values
