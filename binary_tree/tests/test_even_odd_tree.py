from binary_tree.even_odd_tree import even_odd_tree
from binary_tree.tree_node import TreeNode


def test_even_odd_tree():
    root = TreeNode(1)
    assert even_odd_tree(root)
    assert not even_odd_tree(TreeNode(2))

    root.left = TreeNode(10)
    root.right = TreeNode(4)
    assert even_odd_tree(root)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(11)
    assert even_odd_tree(root)

    root.right.right = TreeNode(12)
    assert not even_odd_tree(root)
