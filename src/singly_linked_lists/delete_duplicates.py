from src.data_structures.singly_linked_list_node import SinglyLinkedListNode


def delete_duplicates(head: SinglyLinkedListNode | None) -> SinglyLinkedListNode | None:
    """Delete Duplicates.

    Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
    Return the linked list sorted as well.

    Walks the sorted list, skipping over any node whose value repeats the next node's value.
    """
    node = head

    while node:
        if node.next and node.data == node.next.data:
            node.next = node.next.next
        else:
            node = node.next

    return head
