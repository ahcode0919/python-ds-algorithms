from src.data_structures.binary_tree_node import BinaryTreeNode


def test_init():
    root = BinaryTreeNode(1)
    left = BinaryTreeNode(2)
    right = BinaryTreeNode(3)

    assert root.data == 1
    assert not root.left
    assert not root.right

    root = BinaryTreeNode(1, left, right)
    assert root.left and root.left.data == 2
    assert root.right and root.right.data == 3


def test_left_node():
    left = BinaryTreeNode(2)
    root = BinaryTreeNode(1)
    root.left = left
    assert root.left and root.left.data == 2


def test_right_node():
    right = BinaryTreeNode(2)
    root = BinaryTreeNode(1)
    root.right = right
    assert root.right.data == 2
