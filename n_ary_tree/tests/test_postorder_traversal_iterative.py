from test_helpers.test_helpers import get_n_nary_tree
from n_ary_tree.postorder_traversal_iterative import postorder_traversal_iterative


def test_postorder_traversal_iterative():
    assert postorder_traversal_iterative(get_n_nary_tree()) == [7, 5, 6, 2, 8, 3, 9, 10, 12, 11, 4, 1]
    assert postorder_traversal_iterative(None) == []
