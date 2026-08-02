from data_structures.singly_linked_list_node import SinglyLinkedListNode


def find_middle_node(head: SinglyLinkedListNode | None) -> SinglyLinkedListNode | None:
    """Find Middle Node.

    Find the node that comes before the middle node of a singly linked list.

    Example: `[1] -> 1`, `[1, 2] -> 1`, `[1, 2, 3] -> 2`, `[1, 2, 3, 4] -> 2`

    Advances a slow and a fast pointer (2x speed) until the fast pointer runs out of room.
    """
    if not head:
        return None
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow
