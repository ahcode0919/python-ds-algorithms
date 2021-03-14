from typing import Optional
from data_structures.singly_linked_list_node import SinglyLinkedListNode


def remove_nth_from_end(head: SinglyLinkedListNode, nth: int) -> Optional[SinglyLinkedListNode]:
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
