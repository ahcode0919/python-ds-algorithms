class DoublyLinkedListNode[T]:
    """Doubly Linked List Node.

    (https://en.wikipedia.org/wiki/Doubly_linked_list): In a 'doubly linked list', each node contains,
    besides the next-node link, a second link field pointing to the 'previous' node in the sequence.
    """

    def __init__(
        self,
        data: T | None = None,
        previous_node: "DoublyLinkedListNode[T] | None" = None,
        next_node: "DoublyLinkedListNode[T] | None" = None,
    ):
        self.data: T | None = data
        self.previous: "DoublyLinkedListNode[T] | None" = previous_node
        self.next: "DoublyLinkedListNode[T] | None" = next_node
