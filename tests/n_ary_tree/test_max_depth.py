from n_ary_tree.max_depth import max_depth_bottom_up, max_depth_top_down
from test_helpers.test_helpers import get_n_nary_tree


def test_max_depth_bottom_up():
    assert max_depth_bottom_up(get_n_nary_tree()) == 4


def test_max_depth_top_down():
    assert max_depth_top_down(get_n_nary_tree()) == 4
