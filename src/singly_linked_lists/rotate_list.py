from src.data_structures.singly_linked_list_node import SinglyLinkedListNode


def rotate_list(head: SinglyLinkedListNode | None, amount: int) -> SinglyLinkedListNode | None:
    """Rotate List.

    Given a linked list, rotate the list to the right by k places, where k is non-negative.

    Example: `1->2->3->4->5->None, k = 2` -> `4->5->1->2->3->None`

    Joins the list into a ring, then walks to the new tail and breaks the ring there.
    """
    if not head:
        return None

    if not head.next:
        return head

    current = head
    number = 1

    while current.next:
        number += 1
        current = current.next
    current.next = head
    current = head

    for _ in range((number - amount) % number - 1):
        current = current.next

    new_head = current.next
    current.next = None
    return new_head
