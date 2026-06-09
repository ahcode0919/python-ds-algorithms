from binary_tree.min_depth import min_depth, min_depth_bfs
from test_helpers.test_helpers import get_binary_tree


def test_min_depth():
    tree = get_binary_tree()
    assert min_depth(tree) == 2


def test_min_depth_bfs():
    tree = get_binary_tree()
    assert min_depth_bfs(tree) == 2
