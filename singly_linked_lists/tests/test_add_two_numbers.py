from singly_linked_lists.add_two_numbers import add_two_numbers
from data_structures.singly_linked_list_node import SinglyLinkedListNode
from test_helpers.test_helpers import get_list_values


def test_add_two_numbers():
    head1 = SinglyLinkedListNode(1)
    head1.next = SinglyLinkedListNode(2)
    head1.next.next = SinglyLinkedListNode(3)

    head2 = None

    assert get_list_values(add_two_numbers(head1, head2)) == [1, 2, 3]

    head1 = SinglyLinkedListNode(5)
    head2 = SinglyLinkedListNode(5)
    assert get_list_values(add_two_numbers(head1, head2)) == [0, 1]

    head1.next = SinglyLinkedListNode(2)
    head2.next = SinglyLinkedListNode(3)
    head2.next.next = SinglyLinkedListNode(4)
    assert get_list_values(add_two_numbers(head1, head2)) == [0, 6, 4]
