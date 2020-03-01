from typing import Generic, Optional, TypeVar

T = TypeVar('T')


class TreeNode(Generic[T]):
    def __init__(self, x: T):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
