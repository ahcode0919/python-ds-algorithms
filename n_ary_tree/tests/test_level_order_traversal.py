from n_ary_tree.level_order_traversal import level_order_traversal
from test_helpers.test_helpers import get_n_nary_tree


def test_level_order_traversal():
    assert level_order_traversal(get_n_nary_tree()) == [[1], [2, 3, 4], [5, 6, 8, 9, 10, 11], [7, 12]]
