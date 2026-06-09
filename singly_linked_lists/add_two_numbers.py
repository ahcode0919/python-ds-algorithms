from typing import Optional
from data_structures.singly_linked_list_node import SinglyLinkedListNode


def add_two_numbers(head1: Optional[SinglyLinkedListNode],
                    head2: Optional[SinglyLinkedListNode]) -> Optional[SinglyLinkedListNode]:
    node1 = head1
    node2 = head2
    dummy_node = SinglyLinkedListNode(0)
    result = dummy_node
    carry = 0
    while node1 or node2:
        val1 = 0
        val2 = 0
        if node1:
            val1 = node1.data
            node1 = node1.next
        if node2:
            val2 = node2.data
            node2 = node2.next

        total = val1 + val2 + carry
        carry = int(total / 10)
        result.next = SinglyLinkedListNode(total % 10)
        result = result.next

    if carry > 0:
        result.next = SinglyLinkedListNode(carry)

    return dummy_node.next
