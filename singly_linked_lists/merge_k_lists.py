from typing import List, Optional
from data_structures.singly_linked_list_node import SinglyLinkedListNode


def merge_k_lists(lists: Optional[List[SinglyLinkedListNode]]) -> Optional[SinglyLinkedListNode]:
    dummy = SinglyLinkedListNode()
    current = dummy

    lists = [val for val in lists if val]

    while lists:
        min_node = None
        smallest = float('inf')

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
