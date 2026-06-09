from binary_tree.max_depth import max_depth
from binary_tree.binary_tree_generator import generate_binary_tree


def test_max_depth():
    tree = generate_binary_tree()
    assert max_depth(tree) == 3
