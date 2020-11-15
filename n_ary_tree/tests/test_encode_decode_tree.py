from n_ary_tree.encode_decode_tree import decode, encode
from test_helpers.test_helpers import get_n_nary_tree, get_n_ary_tree_values


def test_encode_decode():
    tree = get_n_nary_tree()
    values = get_n_ary_tree_values(tree)
    assert get_n_ary_tree_values(decode(encode(tree))) == values
