from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class SinglyLinkedListNode(Generic[T]):
    """Singly Linked List Node.

    A node in a singly linked list. It has a data field as well as a 'next' field, which points to the
    next node in the list.
    """

    def __init__(self, data: T = None, next_node: Optional["SinglyLinkedListNode"] = None):
        self.data = data
        self.next = next_node
