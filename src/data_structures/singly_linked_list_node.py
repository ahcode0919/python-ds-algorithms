class SinglyLinkedListNode[T]:
    """Singly Linked List Node.

    A node in a singly linked list. It has a data field as well as a 'next' field, which points to the
    next node in the list.
    """

    def __init__(self, data: T | None = None, next_node: "SinglyLinkedListNode[T] | None" = None):
        self.data: T | None = data
        self.next: SinglyLinkedListNode[T] | None = next_node
