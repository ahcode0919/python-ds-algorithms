"""Shared binary tree node type used by the problems in this package."""

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class TreeNode(Generic[T]):
    """A single binary tree node holding a value and optional left/right children."""

    def __init__(
        self, val: T, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None
    ):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right
