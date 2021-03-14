from typing import Optional
from data_structures.singly_linked_list_node import SinglyLinkedListNode


def insert(head: Optional[SinglyLinkedListNode], value: int) -> Optional[SinglyLinkedListNode]:
    if not head:
        cyclic_list = SinglyLinkedListNode(value)
        cyclic_list.next = cyclic_list
        return cyclic_list

    previous = head
    node = head.next

    while node:
        if previous.data <= value <= node.data:
            new_node = SinglyLinkedListNode(value)
            previous.next = new_node
            new_node.next = node
            return head
        if previous.data > node.data:
            if value >= previous.data or value <= node.data:
                new_node = SinglyLinkedListNode(value)
                previous.next = new_node
                new_node.next = node
                return head

        previous = node
        node = node.next

        if previous == head:
            break

    new_node = SinglyLinkedListNode(value)
    previous.next = new_node
    new_node.next = node

    return head
