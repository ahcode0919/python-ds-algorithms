from src.binary_tree.valid_binary_search_tree import valid_bst
from tests.test_helpers.test_helpers import get_binary_search_tree


def test_valid_bst():
    assert valid_bst(get_binary_search_tree())
