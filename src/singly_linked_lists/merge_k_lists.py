from src.data_structures.singly_linked_list_node import SinglyLinkedListNode


def merge_k_lists[T](lists) -> SinglyLinkedListNode | None:
    """Merge K Sorted Lists.

    You are given an array of k linked lists, each linked list sorted in ascending order.

    Merge all the linked lists into one sorted linked list and return it.

    Repeatedly scans the current head of every list, appending the smallest one found each round.
    """
    dummy = SinglyLinkedListNode()
    current: SinglyLinkedListNode = dummy

    if not lists:
        return None

    filtered_lists: list[SinglyLinkedListNode] = [val for val in lists if val]

    while filtered_lists:
        min_node = 0
        smallest = float("inf")

        for index, head in enumerate(filtered_lists):
            if head.data and head.data <= smallest:
                smallest = head.data
                min_node = index

        node = filtered_lists[min_node]
        current.next = node

        if node.next:
            filtered_lists[min_node] = node.next
        else:
            filtered_lists.pop(min_node)
        current = current.next

    return dummy.next
