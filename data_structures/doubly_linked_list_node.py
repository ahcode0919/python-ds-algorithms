from typing import Generic, Optional, TypeVar


T = TypeVar('T')


class DoublyLinkedListNode(Generic[T]):
    def __init__(self, data: T = None,
                 previous_node: Optional['DoublyLinkedListNode'] = None,
                 next_node: Optional['DoublyLinkedListNode'] = None):
        self.data: T = data
        self.previous: Optional[DoublyLinkedListNode] = previous_node
        self.next: Optional[DoublyLinkedListNode] = next_node
