from binary_tree.postorder_traversal import postorder_traversal_iterative, postorder_traversal_recursive
from test_helpers.test_helpers import get_binary_tree


def test_postorder_traversal_iterative():
    tree = get_binary_tree()
    assert postorder_traversal_recursive(tree) == [4, 5, 2, 3, 1]


def test_postorder_traversal_recursive():
    tree = get_binary_tree()
    assert postorder_traversal_iterative(tree) == [4, 5, 2, 3, 1]
