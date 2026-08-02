class TreeNode[T]:
    """Shared binary tree node type used by the problems in this package.

    A single binary tree node holding a value and optional left/right children.
    """

    def __init__(
        self, val: T, left: "TreeNode[T] | None" = None, right: "TreeNode[T] | None" = None
    ):
        self.val = val
        self.left: TreeNode[T] | None = left
        self.right: TreeNode[T] | None = right
