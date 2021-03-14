from typing import Optional, Set
from data_structures.singly_linked_list_node import SinglyLinkedListNode


def get_intersection_node_with_set(head_a: SinglyLinkedListNode,
                                   head_b: SinglyLinkedListNode) -> Optional[SinglyLinkedListNode]:
    nodes: Set[SinglyLinkedListNode] = set()
    node_a: SinglyLinkedListNode = head_a
    node_b: SinglyLinkedListNode = head_b

    while node_a or node_b:
        if node_a:
            if node_a in nodes:
                return node_a
            nodes.add(node_a)
            node_a = node_a.next

        if node_b:
            if node_b in nodes:
                return node_b
            nodes.add(node_b)
            node_b = node_b.next

    return None
