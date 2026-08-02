from n_ary_tree import nary_tree_node


def preorder_traversal(root: nary_tree_node) -> list:
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
