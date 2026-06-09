from binary_tree.tree_node import TreeNode


def max_depth(root: TreeNode) -> int:
    max_level = 0

    if not root:
        return max_level

    level = [root]

    while level:
        max_level += 1
        next_level = []

        while len(level) > 0:
            node = level.pop()
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level

    return max_level
