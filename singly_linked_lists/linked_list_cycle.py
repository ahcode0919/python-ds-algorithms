from typing import Optional, Set, TypeVar
from data_structures.singly_linked_list_node import SinglyLinkedListNode

T = TypeVar('T')


# Time: O(N + K) -> O(N), Space: O(1)
def has_cycle(head: Optional[SinglyLinkedListNode]) -> bool:
    if not head or not head.next:
        return False

    slow: SinglyLinkedListNode = head
    fast: SinglyLinkedListNode = head.next.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


# Time: O(N), Space: O(N)
def has_cycle_with_set(head: Optional[SinglyLinkedListNode]) -> bool:
    if not head or not head.next:
        return False

    node_set: Set[SinglyLinkedListNode] = set()
    node: SinglyLinkedListNode = head

    while node:
        if not node or node in node_set:
            return True
        node_set.add(node)
        node = node.next
    return False
