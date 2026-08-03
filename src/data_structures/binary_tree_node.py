class BinaryTreeNode[T]:
    """Binary Tree Node.

    A node in a binary tree, holding data plus references to its left and right child nodes.
    """

    def __init__(
        self, data: T, left: BinaryTreeNode[T] | None = None, right: BinaryTreeNode[T] | None = None
    ):
        self.data = data
        self.left = left
        self.right = right
