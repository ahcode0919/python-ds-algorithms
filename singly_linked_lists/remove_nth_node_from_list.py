from typing import Optional

from data_structures.singly_linked_list_node import SinglyLinkedListNode


def remove_nth_from_end(head: SinglyLinkedListNode, nth: int) -> Optional[SinglyLinkedListNode]:
    """Remove Nth Node From End of List.

    Given a linked list, remove the n-th node from the end of the list and return its head.

    Advances a lead pointer nth+1 nodes ahead, then moves both pointers until lead runs out, deleting the target.
    """
    dummy: SinglyLinkedListNode = SinglyLinkedListNode(0)
    dummy.next = head
    previous: SinglyLinkedListNode = dummy
    lead: SinglyLinkedListNode = dummy

    # Move lead forward
    for _ in range(nth + 1):
        lead = lead.next

    # Move through list until lead is None
    while lead:
        previous = previous.next
        lead = lead.next

    # Delete Node by relinking nodes or reassigning head
    previous.next = previous.next.next
    return dummy.next
