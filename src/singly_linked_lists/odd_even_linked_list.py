from src.data_structures.singly_linked_list_node import SinglyLinkedListNode


def odd_even_list(head: SinglyLinkedListNode | None) -> SinglyLinkedListNode | None:
    """Odd Even Linked List.

    Given a singly linked list, group all odd nodes together followed by the even nodes. Here we are talking
    about the node number (position), not the value in the nodes.

    Do it in place: the program should run in O(1) space complexity and O(nodes) time complexity.

    Example: `1->2->3->4->5->None` -> `1->3->5->2->4->None`

    Threads the odd-position and even-position nodes into two chains, then links the odd chain to the even chain.
    """
    if not head:
        return None

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head

    return head
