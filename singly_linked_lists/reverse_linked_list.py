"""Reverse Linked List.

Reverse a singly linked list.

This solution reverses the list iteratively by re-pointing each node's `next` to the previous node as it walks
along. Time: O(N), Space: O(1).
"""

from typing import Optional

from data_structures.singly_linked_list_node import SinglyLinkedListNode


def reverse_linked_list(head: SinglyLinkedListNode) -> Optional[SinglyLinkedListNode]:
    """Walk the list once, re-pointing each node's next to the previous node."""
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
