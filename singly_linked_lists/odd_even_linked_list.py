from typing import Optional
from data_structures.singly_linked_list_node import SinglyLinkedListNode


def odd_even_list(head: Optional[SinglyLinkedListNode]) -> Optional[SinglyLinkedListNode]:
    if not head:
        return None

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head

    return head
