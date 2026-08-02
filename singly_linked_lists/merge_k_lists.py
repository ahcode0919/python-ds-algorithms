from data_structures.singly_linked_list_node import SinglyLinkedListNode


def merge_k_lists(lists: list[SinglyLinkedListNode[int]]) -> SinglyLinkedListNode[int] | None:
    """Merge K Sorted Lists.

    You are given an array of k linked lists, each linked list sorted in ascending order.

    Merge all the linked lists into one sorted linked list and return it.

    Repeatedly scans the current head of every list, appending the smallest one found each round.
    """
    dummy = SinglyLinkedListNode()
    current: SinglyLinkedListNode | None = dummy

    if not lists:
        return None

    lists = [val for val in lists if val]

    while lists:
        min_node = None
        smallest = float("inf")

        for index, head in enumerate(lists):
            if head.data and smallest and head.data <= smallest:
                smallest = head.data
                min_node = index

        if min_node and current:
            current.next = lists[min_node]

            if not lists[min_node].next:
                lists.pop(min_node)
            else:
                next_node = lists[min_node].next
                if next_node:
                    lists[min_node] = next_node
        if current:
            current = current.next

    return dummy.next
