from singly_linked_lists.merge_k_lists import merge_k_lists
from data_structures.list_node import ListNode
from test_helpers.test_helpers import get_list_values, get_singly_linked_list


def test_merge_k_lists():
    lists = [get_singly_linked_list([1, 2, 3]), get_singly_linked_list([1, 3, 4, 5]), get_singly_linked_list([3, 6])]
    assert get_list_values(merge_k_lists(lists)) == [1, 1, 2, 3, 3, 3, 4, 5, 6]

    lists = [None, None, get_singly_linked_list([1, 2, 3])]
    assert get_list_values(merge_k_lists(lists)) == [1, 2, 3]

    lists = []
    assert merge_k_lists(lists) is None

    lists = [None, None]
    assert merge_k_lists(lists) is None
