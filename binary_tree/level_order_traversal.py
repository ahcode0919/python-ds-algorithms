from collections import deque
from typing import List

from binary_tree.tree_node import TreeNode


def level_order_traversal(root: TreeNode) -> List[List[int]]:
    r"""Level-order Traversal.

    Given a binary tree, return the level order traversal of its nodes' values (i.e., from left to
    right, level by level).

    Breadth-first traverses the tree with a queue, grouping node values by depth level.

    Example:
    ```text
        1
       / \
      2   3
        /   \
       4     5
    ```

    Output: `[[1], [2, 3], [4, 5]]`

    """
    values = []

    if not root:
        return values

    queue = deque([root])

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        values.append(level)

    return values
