from binary_tree.tree_node import TreeNode


def valid_bst(root: TreeNode, min_value=float('-inf'), max_value=float('inf')) -> bool:
    if not root:
        return True

    if not valid_bst(root.left, min_value, root.val):
        return False

    if not valid_bst(root.right, root.val, max_value):
        return False

    return min_value < root.val < max_value
