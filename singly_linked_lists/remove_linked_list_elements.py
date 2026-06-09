from typing import Optional
from data_structures.singly_linked_list_node import SinglyLinkedListNode


def remove_elements(head: Optional[SinglyLinkedListNode], data: int) -> Optional[SinglyLinkedListNode]:
    dummy_node: SinglyLinkedListNode = SinglyLinkedListNode(0)
    dummy_node.next = head

    previous: SinglyLinkedListNode = dummy_node
    current: Optional[SinglyLinkedListNode] = head

    while current:
        if current.data == data:
            previous.next = current.next
            current = current.next
        else:
            previous = current
            current = current.next

    return dummy_node.next
