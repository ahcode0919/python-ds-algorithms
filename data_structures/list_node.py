from typing import Generic, Optional, TypeVar

T = TypeVar('T')


class ListNode(Generic[T]):
    def __init__(self, val: Optional[T] = None, next_node: Optional['ListNode[T]'] = None):
        self.val: Optional[T] = val
        self.next: Optional[ListNode] = next_node
