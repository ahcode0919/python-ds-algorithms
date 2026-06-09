from singly_linked_lists.detect_cycle import detect_cycle, detect_cycle_with_set
from data_structures.singly_linked_list_node import SinglyLinkedListNode


def test_detect_cycle():
    assert detect_cycle(SinglyLinkedListNode(1)) is None

    head = SinglyLinkedListNode(1)
    head.next = SinglyLinkedListNode(2)
    head.next.next = SinglyLinkedListNode(3)
    assert detect_cycle(head) is None

    head = SinglyLinkedListNode(1)
    head.next = head
    assert detect_cycle(head) == head

    head = SinglyLinkedListNode(1)
    head.next = SinglyLinkedListNode(2)
    head.next.next = SinglyLinkedListNode(3)
    head.next.next.next = SinglyLinkedListNode(4)
    head.next.next.next.next = head.next
    assert detect_cycle(head) is head.next


def test_detect_cycle_with_set():
    assert detect_cycle_with_set(SinglyLinkedListNode(1)) is None

    head = SinglyLinkedListNode(1)
    head.next = head
    assert detect_cycle_with_set(head) == head

    head = SinglyLinkedListNode(1)
    head.next = SinglyLinkedListNode(2)
    head.next.next = SinglyLinkedListNode(3)
    head.next.next.next = SinglyLinkedListNode(4)
    head.next.next.next.next = head.next
    assert detect_cycle_with_set(head) == head.next
