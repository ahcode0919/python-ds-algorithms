from singly_linked_lists.intersection_two_linked_lists import get_intersection_node
from data_structures.singly_linked_list_node import SinglyLinkedListNode


def test_get_intersection_node():
    head1 = SinglyLinkedListNode(1)
    head1.next = SinglyLinkedListNode(2)

    head2 = SinglyLinkedListNode(1)
    head2.next = SinglyLinkedListNode(2)
    head2.next.next = SinglyLinkedListNode(3)
    assert get_intersection_node(head1, head2) is None

    head1 = SinglyLinkedListNode(1)
    head2 = head1
    assert get_intersection_node(head1, head2) is head1

    head1 = SinglyLinkedListNode(1)
    head1.next = SinglyLinkedListNode(2)
    head1.next.next = SinglyLinkedListNode(3)
    head1.next.next.next = SinglyLinkedListNode(4)
    head2 = SinglyLinkedListNode(1)
    head2.next = head1.next.next
    assert get_intersection_node(head1, head2) is head1.next.next
