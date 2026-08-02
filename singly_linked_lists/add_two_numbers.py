"""Add Two Numbers.

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
order and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example: `(2 -> 4 -> 3) + (5 -> 6 -> 4)` -> `7 -> 0 -> 8` (`342 + 465 = 807`)
"""

from typing import Optional

from data_structures.singly_linked_list_node import SinglyLinkedListNode


def add_two_numbers(
    head1: Optional[SinglyLinkedListNode], head2: Optional[SinglyLinkedListNode]
) -> Optional[SinglyLinkedListNode]:
    """Sum the two numbers digit-by-digit from the least significant node, carrying into the next node."""
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
