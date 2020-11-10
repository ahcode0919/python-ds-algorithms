from n_ary_tree.postorder_traversal import postorder_traversal
from test_helpers.test_helpers import get_n_nary_tree


def test_postorder_traversal():
    assert postorder_traversal(get_n_nary_tree()) == [7, 5, 6, 2, 8, 3, 9, 10, 12, 11, 4, 1]
    assert postorder_traversal(None) == []

