"""Has Path Sum.

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values
along the path equals the given sum.
"""

from binary_tree.tree_node import TreeNode


def has_path_sum(root: TreeNode, target: int) -> bool:
    """Recursively subtract each node's value from the target and check for a zero remainder at a leaf."""
    if not root:
        return False

    target -= root.val

    if root.left or root.right:
        left = has_path_sum(root.left, target)
        right = has_path_sum(root.right, target)
        return left or right
    return target == 0
