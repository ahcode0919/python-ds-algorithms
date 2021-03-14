from data_structures.singly_linked_list_node import SinglyLinkedListNode
from singly_linked_lists.delete_duplicates import delete_duplicates
from test_helpers.test_helpers import get_list_values


def test_delete_duplicates():
    head = None
    assert delete_duplicates(head) is None

    head = SinglyLinkedListNode(1)
    assert get_list_values(delete_duplicates(head)) == [1]

    head.next = SinglyLinkedListNode(2)
    head.next.next = SinglyLinkedListNode(2)
    head.next.next.next = SinglyLinkedListNode(3)
    head.next.next.next.next = SinglyLinkedListNode(4)
    head.next.next.next.next.next = SinglyLinkedListNode(4)
    assert get_list_values(delete_duplicates(head)) == [1, 2, 3, 4]
