from binary_tree.has_path_sum import has_path_sum
from binary_tree.tree_node import TreeNode
from test_helpers.test_helpers import get_binary_tree


def test_has_path_sum():
    assert has_path_sum(get_binary_tree(), 4)
    assert has_path_sum(get_binary_tree(), 7)
    assert has_path_sum(get_binary_tree(), 8)
    assert has_path_sum(TreeNode(1), 1)
