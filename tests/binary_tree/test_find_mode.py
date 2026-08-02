from src.binary_tree.find_mode import find_mode
from tests.test_helpers.test_helpers import TreeNode, get_binary_tree


def test_find_mode():
    tree = get_binary_tree()
    assert sorted(find_mode(tree)) == [1, 2, 3, 4, 5]

    tree.left.right.left = TreeNode(5)
    assert find_mode(tree) == [5]
