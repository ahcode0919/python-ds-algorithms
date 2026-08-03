from src.data_structures.singly_linked_list_node import SinglyLinkedListNode
from src.singly_linked_lists.odd_even_linked_list import odd_even_list
from tests.test_helpers.test_helpers import get_list_values


def test_odd_even_linked_list():
    head = None
    assert odd_even_list(head) is None

    head = SinglyLinkedListNode(1)
    assert odd_even_list(head) == head

    head.next = SinglyLinkedListNode(2)
    head.next.next = SinglyLinkedListNode(3)
    head.next.next.next = SinglyLinkedListNode(4)
    head.next.next.next.next = SinglyLinkedListNode(5)
    assert get_list_values(odd_even_list(head)) == [1, 3, 5, 2, 4]
