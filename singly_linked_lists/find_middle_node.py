from typing import Optional
from data_structures.singly_linked_list_node import SinglyLinkedListNode


def find_middle_node(head: Optional[SinglyLinkedListNode]) -> Optional[SinglyLinkedListNode]:
    if not head:
        return None
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow
