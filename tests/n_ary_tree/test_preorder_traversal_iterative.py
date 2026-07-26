from n_ary_tree.preorder_traversal_iterative import preorder_traversal_iterative
from test_helpers.test_helpers import get_n_nary_tree


def test_preorder_traversal_iterative():
    root = get_n_nary_tree()
    assert preorder_traversal_iterative(root) == [1, 2, 5, 7, 6, 3, 8, 4, 9, 10, 11, 12]
