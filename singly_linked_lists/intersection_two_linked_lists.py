from typing import Optional
from data_structures.singly_linked_list_node import SinglyLinkedListNode


def get_intersection_node(head_a: SinglyLinkedListNode, head_b: SinglyLinkedListNode) -> Optional[SinglyLinkedListNode]:
    if not head_a or not head_b:
        return None

    node_a: SinglyLinkedListNode = head_a
    node_b: SinglyLinkedListNode = head_b

    while node_a != node_b:
        node_a = node_a.next
        node_b = node_b.next

        if node_a is None and node_b is None:
            return None

        if node_a is None:
            node_a = head_b

        if node_b is None:
            node_b = head_a

    return node_a
