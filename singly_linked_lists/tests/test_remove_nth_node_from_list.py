from singly_linked_lists.remove_nth_node_from_list import remove_nth_from_end
from data_structures.singly_linked_list_node import SinglyLinkedListNode


def test_remove_nth_from_end():
    head = SinglyLinkedListNode(1)
    assert remove_nth_from_end(head, 1) is None

    head = SinglyLinkedListNode(1)
    head.next = SinglyLinkedListNode(2)
    assert remove_nth_from_end(head, 2).data == 2
    assert remove_nth_from_end(head, 1).data == 1

    head = SinglyLinkedListNode(1)
    head.next = SinglyLinkedListNode(2)
    head.next.next = SinglyLinkedListNode(3)
    head.next.next.next = SinglyLinkedListNode(4)
    assert remove_nth_from_end(head, 2).next.next.data == 4
