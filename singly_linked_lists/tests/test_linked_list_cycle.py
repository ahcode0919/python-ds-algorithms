from singly_linked_lists.linked_list_cycle import has_cycle, has_cycle_with_set
from data_structures.singly_linked_list_node import SinglyLinkedListNode


def test_has_cycle():
    assert not has_cycle(None)
    assert not has_cycle(SinglyLinkedListNode(1))

    head = SinglyLinkedListNode(1)
    head.next = SinglyLinkedListNode(2)
    head.next.next = SinglyLinkedListNode(3)
    head.next.next.next = SinglyLinkedListNode(4)
    head.next.next.next.next = head.next
    assert has_cycle(head)

    head2 = SinglyLinkedListNode(1)
    head2.next = SinglyLinkedListNode(2)
    head2.next.next = SinglyLinkedListNode(3)
    assert not has_cycle(head2)


def test_has_cycle_with_set():
    assert not has_cycle_with_set(None)
    assert not has_cycle_with_set(SinglyLinkedListNode(1))

    head = SinglyLinkedListNode(1)
    head.next = SinglyLinkedListNode(2)
    head.next.next = SinglyLinkedListNode(3)
    head.next.next.next = SinglyLinkedListNode(4)
    head.next.next.next.next = head.next
    assert has_cycle_with_set(head)

    head2 = SinglyLinkedListNode(1)
    head2.next = SinglyLinkedListNode(2)
    head2.next.next = SinglyLinkedListNode(3)
    assert not has_cycle_with_set(head2)
