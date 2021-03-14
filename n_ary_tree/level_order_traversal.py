from typing import List
from n_ary_tree.nary_tree_node import NaryTreeNode


def level_order_traversal(root: NaryTreeNode) -> List[List[int]]:
    levels = []

    if not root:
        return levels

    current_level = [root]

    while current_level:
        next_level = []
        values = []

        for node in current_level:
            if node.children:
                next_level.extend(node.children)
            values.append(node.value)

        levels.append(values)
        current_level = next_level

    return levels
