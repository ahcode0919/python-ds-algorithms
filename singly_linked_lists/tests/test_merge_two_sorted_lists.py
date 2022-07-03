from singly_linked_lists.merge_two_sorted_lists import merge_two_lists
from data_structures.singly_linked_list_node import SinglyLinkedListNode
from test_helpers.test_helpers import get_list_values


def test_merge_two_lists():

    list1 = SinglyLinkedListNode(1)
    assert get_list_values(merge_two_lists(list1, None)) == [1]

    list2 = SinglyLinkedListNode(1)
    assert get_list_values(merge_two_lists(list1, list2)) == [1, 1]

    list1.next = SinglyLinkedListNode(2)
    list1.next.next = SinglyLinkedListNode(4)
    list2.next = SinglyLinkedListNode(3)
    list2.next.next = SinglyLinkedListNode(4)
    assert get_list_values(merge_two_lists(list1, list2)) == [1, 1, 2, 3, 4, 4]
