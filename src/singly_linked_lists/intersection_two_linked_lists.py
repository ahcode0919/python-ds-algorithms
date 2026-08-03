from src.data_structures.singly_linked_list_node import SinglyLinkedListNode


def get_intersection_node(
    head_a: SinglyLinkedListNode, head_b: SinglyLinkedListNode
) -> SinglyLinkedListNode | None:
    """Intersection of Two Linked Lists.

    Find the node at which two singly linked lists intersect.

    Example: lists `a1 -> a2 -> a3` and `b1 -> b2` both feed into a shared tail `c1 -> c2 -> c3`. The answer is
    `c1`.

    This solution uses two pointers that each walk one list then switch to the head of the other list, so they
    cover equal total distance and meet at the intersection (or both reach None if there is none). Time: O(N),
    Space: O(1).
    """
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
