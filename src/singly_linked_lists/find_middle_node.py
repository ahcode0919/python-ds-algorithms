from src.data_structures.singly_linked_list_node import SinglyLinkedListNode


def find_middle_node(head: SinglyLinkedListNode) -> SinglyLinkedListNode:
    """Find Middle Node.

    Find the node that comes before the middle node of a singly linked list.

    Example: `[1] -> 1`, `[1, 2] -> 1`, `[1, 2, 3] -> 2`, `[1, 2, 3, 4] -> 2`

    Advances a slow and a fast pointer (2x speed) until the fast pointer runs out of room.
    """
    slow = head
    fast = head

    while slow and slow.next and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow
