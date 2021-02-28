from binary_tree.tree_node import TreeNode


def two_sum_iv(root: TreeNode, target: int) -> bool:
    if not root:
        return False

    values = set()
    queue = [root]

    while queue:
        node = queue.pop()

        if node:
            if target - node.val in values:
                return True
            values.add(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return False
