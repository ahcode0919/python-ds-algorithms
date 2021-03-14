from typing import Optional
from data_structures.singly_linked_list_node import SinglyLinkedListNode


def reverse_linked_list(head: SinglyLinkedListNode) -> Optional[SinglyLinkedListNode]:
    if not head:
        return None
    previous: Optional[SinglyLinkedListNode] = None
    current: Optional[SinglyLinkedListNode] = head

    while current:
        temp = current.next
        current.next = previous
        previous = current
        current = temp

    return previous
