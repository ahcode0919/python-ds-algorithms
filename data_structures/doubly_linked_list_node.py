"""Doubly Linked List Node.

(https://en.wikipedia.org/wiki/Doubly_linked_list): In a 'doubly linked list', each node contains, besides
the next-node link, a second link field pointing to the 'previous' node in the sequence.
"""

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class DoublyLinkedListNode(Generic[T]):
    def __init__(
        self,
        data: T = None,
        previous_node: Optional["DoublyLinkedListNode"] = None,
        next_node: Optional["DoublyLinkedListNode"] = None,
    ):
        self.data: T = data
        self.previous: Optional[DoublyLinkedListNode] = previous_node
        self.next: Optional[DoublyLinkedListNode] = next_node
