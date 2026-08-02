"""Detect Cycle.

Given a linked list, return the node where the cycle begins. If there is no cycle, return None.
"""

from typing import Optional, Set

from data_structures.singly_linked_list_node import SinglyLinkedListNode


def detect_cycle(head: SinglyLinkedListNode) -> Optional[SinglyLinkedListNode]:
    """Find the cycle start with slow/fast pointers, then a second pass from head. Time: O(N), Space: O(1)."""
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
    """Find the cycle start by tracking visited nodes in a set. Time: O(N), Space: O(N)."""
    visited_nodes: Set[SinglyLinkedListNode] = set()

    node = head

    while node:
        if node and node in visited_nodes:
            return node
        visited_nodes.add(node)
        node = node.next
    return None
