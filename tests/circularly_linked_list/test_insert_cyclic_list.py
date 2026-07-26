from circularly_linked_list.insert_cyclic_list import insert
from data_structures.singly_linked_list_node import SinglyLinkedListNode
from test_helpers.test_helpers import get_cyclic_list_values


def test_insert():
    head = None
    assert get_cyclic_list_values(insert(head, 1)) == [1]

    head = SinglyLinkedListNode(1)
    head.next = head
    assert get_cyclic_list_values(insert(head, 2)) == [1, 2]

    head = SinglyLinkedListNode(3)
    head.next = SinglyLinkedListNode(4)
    head.next.next = SinglyLinkedListNode(1)
    head.next.next.next = head
    assert get_cyclic_list_values(insert(head, 2)) == [3, 4, 1, 2]
