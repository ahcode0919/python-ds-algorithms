from binary_tree.symmetric_binary_tree import symmetric_binary_tree
from binary_tree.tree_node import TreeNode


def test_symmetric_binary_tree():
    assert symmetric_binary_tree(None)
    assert symmetric_binary_tree(TreeNode(1))

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(2)
    assert symmetric_binary_tree(tree)

    tree.left.left = TreeNode(3)
    assert not symmetric_binary_tree(tree)

    tree.right.right = TreeNode(3)
    assert symmetric_binary_tree(tree)

    tree.right.right = None
    tree.right.left = TreeNode(3)
    assert not symmetric_binary_tree(tree)
