from binary_tree.find_mode import find_mode
from test_helpers.test_helpers import get_binary_tree, TreeNode


def test_find_mode():
    tree = get_binary_tree()
    assert sorted(find_mode(tree)) == [1, 2, 3, 4, 5]

    tree.left.right.left = TreeNode(5)
    assert find_mode(tree) == [5]
