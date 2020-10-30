from binary_tree.max_depth import max_depth
from test_helpers.test_helpers import generate_binary_tree


def test_max_depth():
    tree = generate_binary_tree()
    assert max_depth(tree) == 3
