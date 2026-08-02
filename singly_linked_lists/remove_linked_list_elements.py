from typing import Optional

from data_structures.singly_linked_list_node import SinglyLinkedListNode


def remove_elements(
    head: Optional[SinglyLinkedListNode], data: int
) -> Optional[SinglyLinkedListNode]:
    """Remove Linked List Elements.

    Remove all elements from a linked list of integers that have a given value.

    Example: `1->2->6->3->4->5->6, val = 6` -> `1->2->3->4->5`

    Walks the list with a dummy head, relinking around any node whose value matches data.
    """
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
