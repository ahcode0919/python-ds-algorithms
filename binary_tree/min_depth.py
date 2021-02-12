from collections import deque
from binary_tree.tree_node import TreeNode


def min_depth(root: TreeNode) -> int:
    if not root:
        return 0

    if not root.left:
        return min_depth(root.right) + 1
    if not root.right:
        return min_depth(root.left) + 1

    return min(min_depth(root.left), min_depth(root.right)) + 1


def min_depth_bfs(root: TreeNode) -> int:
    if not root:
        return 0

    level = deque([root])
    depth = 1

    while level:
        for _ in range(len(level)):
            node = level.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        depth += 1
    return depth
