r"""Min Depth.

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf
node.

Note: A leaf is a node with no children.

Example:
Input:

```text
   3
  / \
 9  20
   /  \
 15    7
```

Output: `2` (Node - 9)

"""

from collections import deque

from src.binary_tree.tree_node import TreeNode


def min_depth(root: TreeNode) -> int:
    """Recursively descend, at each node skipping to whichever child subtree exists when only one does."""
    if not root:
        return 0

    if not root.left:
        return min_depth(root.right) + 1
    if not root.right:
        return min_depth(root.left) + 1

    return min(min_depth(root.left), min_depth(root.right)) + 1


def min_depth_bfs(root: TreeNode) -> int:
    """Breadth-first traverse level by level, returning as soon as the first leaf node is reached."""
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
