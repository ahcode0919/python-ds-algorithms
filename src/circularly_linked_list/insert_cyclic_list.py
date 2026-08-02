from src.data_structures.singly_linked_list_node import SinglyLinkedListNode


def insert(head: SinglyLinkedListNode | None, value: int) -> SinglyLinkedListNode | None:
    """Insert into a Cyclic Sorted List.

    Given a node from a Circular Linked List which is sorted in ascending order, write a function to
    insert a value into the list such that it remains a sorted circular list. The given node can be a
    reference to any single node in the list, and may not be necessarily the smallest value in the list.

    If there are multiple suitable places for insertion, you may choose any place to insert the new
    value. After the insertion, the circular list should remain sorted.

    If the list is empty (i.e., given node is null), you should create a new single circular list and
    return the reference to that single node. Otherwise, you should return the original given node.
    """
    if not head:
        cyclic_list = SinglyLinkedListNode(value)
        cyclic_list.next = cyclic_list
        return cyclic_list

    previous = head
    node = head.next

    while node:
        if previous.data <= value <= node.data:
            new_node = SinglyLinkedListNode(value)
            previous.next = new_node
            new_node.next = node
            return head
        if previous.data > node.data:
            if value >= previous.data or value <= node.data:
                new_node = SinglyLinkedListNode(value)
                previous.next = new_node
                new_node.next = node
                return head

        previous = node
        node = node.next

        if previous == head:
            break

    new_node = SinglyLinkedListNode(value)
    previous.next = new_node
    new_node.next = node

    return head
