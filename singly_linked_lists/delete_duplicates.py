from typing import Optional
from data_structures.singly_linked_list_node import SinglyLinkedListNode


def delete_duplicates(head: Optional[SinglyLinkedListNode]) -> Optional[SinglyLinkedListNode]:
    node = head

    while node:
        if node.next and node.data == node.next.data:
            node.next = node.next.next
        else:
            node = node.next

    return head
