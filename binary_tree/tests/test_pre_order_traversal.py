from binary_tree.pre_order_traversal import preorder_traversal_iterative, preorder_traversal_morris
from binary_tree.binary_tree_generator import generate_binary_tree


def test_preorder_traversal_iterative():
    tree = generate_binary_tree()
    assert preorder_traversal_iterative(tree) == [1, 2, 3, 4, 5]


def test_preorder_traversal_morris():
    tree = generate_binary_tree()
    assert preorder_traversal_morris(tree) == [1, 2, 3, 4, 5]