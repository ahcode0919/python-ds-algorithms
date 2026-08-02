from src.data_structures.singly_linked_list_node import SinglyLinkedListNode


def reverse_linked_list(head: SinglyLinkedListNode) -> SinglyLinkedListNode | None:
    """Reverse Linked List.

    Reverse a singly linked list.

    This solution reverses the list iteratively by re-pointing each node's `next` to the previous node as it
    walks along. Time: O(N), Space: O(1).
    """
    if not head:
        return None
    previous: SinglyLinkedListNode | None = None
    current: SinglyLinkedListNode | None = head

    while current:
        temp = current.next
        current.next = previous
        previous = current
        current = temp

    return previous
