from singly_linked_lists.reverse_linked_list_recursive import reverse_linked_list_recursive
from data_structures.singly_linked_list_node import SinglyLinkedListNode
from test_helpers.test_helpers import get_list_values


def test_reverse_linked_list():
    head = SinglyLinkedListNode(1)
    head.next = SinglyLinkedListNode(2)
    head.next.next = SinglyLinkedListNode(3)
    assert get_list_values(reverse_linked_list_recursive(head)) == [3, 2, 1]

    head = SinglyLinkedListNode(1)
    head.next = SinglyLinkedListNode(2)
    assert get_list_values(reverse_linked_list_recursive(head)) == [2, 1]

    head = SinglyLinkedListNode(1)
    assert get_list_values(reverse_linked_list_recursive(head)) == [1]
