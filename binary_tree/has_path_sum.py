from binary_tree.tree_node import TreeNode


def has_path_sum(root: TreeNode, target: int) -> bool:
    if not root:
        return False

    target -= root.val

    if root.left or root.right:
        left = has_path_sum(root.left, target)
        right = has_path_sum(root.right, target)
        return left or right
    return target == 0
