from binary_tree.tree_from_preorder_inorder import tree_from_preorder_inorder
from binary_tree.tree_node import TreeNode
from test_helpers.test_helpers import get_binary_tree_values


def test_tree_from_preorder_inorder():
    preorder = []
    inorder = []
    assert not tree_from_preorder_inorder(preorder, inorder)

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    tree = tree_from_preorder_inorder(preorder, inorder)
    tree_values = get_binary_tree_values(tree)
    expected_values = get_binary_tree_values(root)

    assert tree_values == expected_values
