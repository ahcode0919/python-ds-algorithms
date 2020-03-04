from typing import Generic, Optional, TypeVar

T = TypeVar('T')


def has_cycle(head: 'ListNode') -> bool:
    if not head and head.next:
        return False

    slow = head
    fast = head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


class ListNode(Generic[T]):
    def __init__(self, val: T):
        self.val: T = val
        self.next: Optional[ListNode] = None
