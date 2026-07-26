from binary_tree.tree_from_inorder_postorder import tree_from_inorder_and_postorder
from binary_tree.tree_node import TreeNode
from test_helpers.test_helpers import get_binary_tree_values


def test_tree_from_inorder_postorder():
    inorder = []
    postorder = []
    assert not tree_from_inorder_and_postorder(inorder, postorder)

    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    tree = tree_from_inorder_and_postorder(inorder, postorder)
    tree_values = get_binary_tree_values(tree)
    expected_values = get_binary_tree_values(root)

    assert tree_values == expected_values
