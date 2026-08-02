from binary_tree.tree_node import TreeNode


def valid_bst(root: TreeNode, min_value=float("-inf"), max_value=float("inf")) -> bool:
    """Valid Binary Search Tree.

    Given a binary tree, determine if it is a valid binary search tree (BST).

    Assume a BST is defined as follows:

    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.

    Recursively narrows an allowed (min, max) range for each subtree and checks every node falls
    within it.
    """
    if not root:
        return True

    if not valid_bst(root.left, min_value, root.val):
        return False

    if not valid_bst(root.right, root.val, max_value):
        return False

    return min_value < root.val < max_value
