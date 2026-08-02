"""Linked List Cycle.

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in
the linked list where the tail connects to. If pos is -1, then there is no cycle in the linked list.
"""

from src.data_structures.singly_linked_list_node import SinglyLinkedListNode


# Time: O(N + K) -> O(N), Space: O(1)
def has_cycle(head: SinglyLinkedListNode | None) -> bool:
    """Detect a cycle with slow/fast pointers, returning True once they meet."""
    if not head or not head.next:
        return False

    slow: SinglyLinkedListNode | None = head
    fast: SinglyLinkedListNode | None = head.next.next

    while slow and slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


# Time: O(N), Space: O(N)
def has_cycle_with_set(head: SinglyLinkedListNode | None) -> bool:
    """Detect a cycle by tracking visited nodes in a set, returning True on the first repeat."""
    if not head or not head.next:
        return False

    node_set: set[SinglyLinkedListNode] = set()
    node: SinglyLinkedListNode | None = head

    while node:
        if not node or node in node_set:
            return True
        node_set.add(node)
        node = node.next
    return False
