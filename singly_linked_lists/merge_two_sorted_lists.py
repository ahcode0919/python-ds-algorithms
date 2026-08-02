from data_structures.singly_linked_list_node import SinglyLinkedListNode


def merge_two_lists(
    head1: SinglyLinkedListNode | None, head2: SinglyLinkedListNode | None
) -> SinglyLinkedListNode | None:
    """Merge Two Sorted Lists.

    Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together
    the nodes of the first two lists.

    Example: `1->2->4`, `1->3->4` -> `1->1->2->3->4->4`

    Splices the two sorted lists together node by node, always taking the smaller current head.
    """
    if not head1 and not head2:
        return None

    node1 = head1
    node2 = head2
    dummy_node = SinglyLinkedListNode(0)
    current_node = dummy_node

    while node1 and node2:
        if node1.data <= node2.data:
            current_node.next = node1
            node1 = node1.next
        else:
            current_node.next = node2
            node2 = node2.next
        current_node = current_node.next

    if node1:
        current_node.next = node1
    if node2:
        current_node.next = node2

    return dummy_node.next
