from src.n_ary_tree.nary_tree_node import NaryTreeNode


def preorder_traversal(root: NaryTreeNode | None) -> list:
    """Preorder Traversal.

    Given the root of an n-ary tree, return the preorder traversal of its nodes' values — a
    node's value is visited before its children. Recursively visit the current node's value,
    then each child in order.
    """
    if not root:
        return []

    values = [root.value]

    if not root.children:
        return values

    for child in root.children:
        values.extend(preorder_traversal(child))

    return values
