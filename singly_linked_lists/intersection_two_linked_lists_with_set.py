"""Intersection of Two Linked Lists (set-based).

Find the node at which two singly linked lists intersect.

Example: lists `a1 -> a2 -> a3` and `b1 -> b2` both feed into a shared tail `c1 -> c2 -> c3`. The answer is `c1`.

This is a less optimal solution than the two-pointer approach: it records every visited node from both lists in a
set and returns the first node already seen. Time: O(N), Space: O(N).
"""

from typing import Optional, Set

from data_structures.singly_linked_list_node import SinglyLinkedListNode


def get_intersection_node_with_set(
    head_a: SinglyLinkedListNode, head_b: SinglyLinkedListNode
) -> Optional[SinglyLinkedListNode]:
    """Advance through both lists together, recording visited nodes and returning the first repeat."""
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
