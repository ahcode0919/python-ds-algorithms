from binary_tree.preorder_traversal import preorder_traversal_iterative, preorder_traversal_morris,\
    preorder_traversal_recursive
from test_helpers.test_helpers import get_binary_tree


def test_preorder_traversal_iterative():
    tree = get_binary_tree()
    assert preorder_traversal_iterative(tree) == [1, 2, 4, 5, 3]


def test_preorder_traversal_morris():
    tree = get_binary_tree()
    assert preorder_traversal_morris(tree) == [1, 2, 4, 5, 3]


def test_preorder_traversal_recursive():
    tree = get_binary_tree()
    assert preorder_traversal_recursive(tree) == [1, 2, 4, 5, 3]
