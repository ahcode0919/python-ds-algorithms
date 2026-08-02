from data_structures.singly_linked_list_node import SinglyLinkedListNode


def reverse_linked_list_recursive(head: SinglyLinkedListNode) -> SinglyLinkedListNode | None:
    """Reverse Linked List (recursive).

    Reverse a singly linked list.

    This solution reverses the list recursively: it recurses to the tail first, then, unwinding back up the call
    stack, points each node's successor back at it. Time: O(N), Space: O(N).
    """
    if not head or not head.next:
        return head

    new_head = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
