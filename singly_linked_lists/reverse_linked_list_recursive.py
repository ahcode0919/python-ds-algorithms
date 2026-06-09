from typing import Optional
from data_structures.singly_linked_list_node import SinglyLinkedListNode


def reverse_linked_list_recursive(head: SinglyLinkedListNode) -> Optional[SinglyLinkedListNode]:
    if not head or not head.next:
        return head

    new_head = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
