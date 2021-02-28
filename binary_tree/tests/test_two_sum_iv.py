from binary_tree.two_sum_iv import two_sum_iv
from test_helpers.test_helpers import get_binary_tree, TreeNode


def test_two_sum_iv():
    tree = TreeNode(1)
    assert not two_sum_iv(tree, 2)

    tree = get_binary_tree()
    assert two_sum_iv(tree, 5)
    assert not two_sum_iv(tree, 1)
    assert not two_sum_iv(tree, 10)
