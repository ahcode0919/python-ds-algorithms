from collections import deque

from n_ary_tree.nary_tree_node import NaryTreeNode


def postorder_traversal_iterative[T](root: NaryTreeNode[T] | None) -> list[T]:
    """Postorder Traversal (Iterative).

    Given the root of an n-ary tree, return the postorder traversal of its nodes' values — a
    node's children are all visited before the node itself. Push nodes onto a stack, prepending
    each visited value into a deque to build postorder.
    """
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
