from typing import Optional
from data_structures.list_node import ListNode


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    node = head

    while node:
        if node.next and node.val == node.next.val:
            node.next = node.next.next
        else:
            node = node.next

    return head
