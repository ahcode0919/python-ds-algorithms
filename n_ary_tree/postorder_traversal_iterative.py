from collections import deque
from typing import List, Optional
from n_ary_tree.node import Node


def postorder_traversal_iterative(root: Optional[Node]) -> List:
    values = deque()
    stack = []
    if not root:
        return []

    stack.append(root)

    while stack:
        node = stack.pop()
        if node.children:
            for child in node.children:
                stack.append(child)
        values.appendleft(node.value)

    return list(values)
