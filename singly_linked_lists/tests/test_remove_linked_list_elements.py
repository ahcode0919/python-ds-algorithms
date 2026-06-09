from singly_linked_lists.remove_linked_list_elements import remove_elements
from data_structures.singly_linked_list_node import SinglyLinkedListNode
from test_helpers.test_helpers import get_list_values


def test_remove_elements():
    assert remove_elements(None, 1) is None

    head = SinglyLinkedListNode(1)
    assert remove_elements(head, 1) is None
    assert remove_elements(head, 2) is head

    head = SinglyLinkedListNode(1)
    head.next = SinglyLinkedListNode(2)
    head.next.next = SinglyLinkedListNode(2)
    head.next.next.next = SinglyLinkedListNode(3)
    assert get_list_values(remove_elements(head, 2)) == [1, 3]
