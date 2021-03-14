from typing import Optional, Set
from data_structures.singly_linked_list_node import SinglyLinkedListNode


def detect_cycle(head: SinglyLinkedListNode) -> Optional[SinglyLinkedListNode]:
    # detect cycle
    if not head or not head.next:
        return None
    slow: SinglyLinkedListNode = head
    fast: SinglyLinkedListNode = head
    intersection: Optional[SinglyLinkedListNode] = None

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            intersection = slow
            break

    if not intersection:
        return intersection

    # detect intersection
    node = head
    while node != intersection:
        node = node.next
        intersection = intersection.next

    return intersection


def detect_cycle_with_set(head: SinglyLinkedListNode) -> Optional[SinglyLinkedListNode]:
    visited_nodes: Set[SinglyLinkedListNode] = set()

    node = head

    while node:
        if node and node in visited_nodes:
            return node
        visited_nodes.add(node)
        node = node.next
    return None
