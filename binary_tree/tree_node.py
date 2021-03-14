from typing import Generic, Optional, TypeVar

T = TypeVar('T')


class TreeNode(Generic[T]):
    def __init__(self, val: T, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right
