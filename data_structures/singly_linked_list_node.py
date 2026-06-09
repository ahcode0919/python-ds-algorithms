from typing import Generic, Optional, TypeVar


T = TypeVar('T')


class SinglyLinkedListNode(Generic[T]):
    def __init__(self, data: T = None, next_node: Optional['SinglyLinkedListNode'] = None):
        self.data = data
        self.next = next_node
