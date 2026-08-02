"""Merge K Sorted Lists.

You are given an array of k linked lists, each linked list sorted in ascending order.

Merge all the linked lists into one sorted linked list and return it.
"""

from typing import List, Optional

from data_structures.singly_linked_list_node import SinglyLinkedListNode


def merge_k_lists(lists: Optional[List[SinglyLinkedListNode]]) -> Optional[SinglyLinkedListNode]:
    """Repeatedly scan the current head of every list, appending the smallest one found each round."""
    dummy = SinglyLinkedListNode()
    current = dummy

    lists = [val for val in lists if val]

    while lists:
        min_node = None
        smallest = float("inf")

        for index, head in enumerate(lists):
            if head and head.data <= smallest:
                smallest = head.data
                min_node = index

        current.next = lists[min_node]

        if not lists[min_node].next:
            lists.pop(min_node)
        else:
            lists[min_node] = lists[min_node].next
        current = current.next

    return dummy.next
