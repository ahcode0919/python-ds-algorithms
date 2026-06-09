from data_structures.singly_linked_list_node import SinglyLinkedListNode
from singly_linked_lists.rotate_list import rotate_list
from test_helpers.test_helpers import get_list_values


def test_rotate_list():
    head = None
    assert rotate_list(head, 1) is None

    head = SinglyLinkedListNode(1)
    assert get_list_values(rotate_list(head, 1)) == [1]
    assert get_list_values(rotate_list(head, 3)) == [1]

    head.next = SinglyLinkedListNode(2)
    assert get_list_values(rotate_list(head, 1)) == [2, 1]

    head = SinglyLinkedListNode(1)
    head.next = SinglyLinkedListNode(2)
    head.next.next = SinglyLinkedListNode(3)
    head.next.next.next = SinglyLinkedListNode(4)
    head.next.next.next.next = SinglyLinkedListNode(5)
    assert get_list_values(rotate_list(head, 2)) == [4, 5, 1, 2, 3]
