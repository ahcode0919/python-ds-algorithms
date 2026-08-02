r"""Pre-order Traversal.

Pre-order traversal is to visit the root first. Then traverse the left subtree. Finally, traverse the right
subtree.

Example:
```text
     1
    / \
   2   3
  / \
 4   5
```

Output: `[1, 2, 4, 5, 3]`

"""

from typing import List

from binary_tree.tree_node import TreeNode


def preorder_traversal_iterative(root: TreeNode) -> List[int]:
    """Traverse iteratively with an explicit stack. Time: O(N), Space: O(N)."""
    output = []

    if root is None:
        return output

    stack = [root]
    while stack:
        root_node = stack.pop()
        if root_node is not None:
            output.append(root_node.val)
        if root_node.right is not None:
            stack.append(root_node.right)
        if root_node.left is not None:
            stack.append(root_node.left)
    return output


def preorder_traversal_morris(root: TreeNode) -> List[int]:
    """Traverse using threaded links through predecessors, avoiding a stack. Time: O(N), Space: O(1)."""
    node, output = root, []
    while node:
        if not node.left:
            output.append(node.val)
            node = node.right
        else:
            predecessor = node.left

            while predecessor.right and predecessor.right is not node:
                predecessor = predecessor.right

            if not predecessor.right:
                output.append(node.val)
                predecessor.right = node
                node = node.left
            else:
                predecessor.right = None
                node = node.right

    return output


def preorder_traversal_recursive(root: TreeNode) -> List[int]:
    """Recursively visit the node, then traverse left, then traverse right. Time: O(N), Space: O(N)."""
    values = []
    if not root:
        return values

    values.append(root.val)

    if root.left:
        values.extend(preorder_traversal_recursive(root.left))
    if root.right:
        values.extend(preorder_traversal_recursive(root.right))
    return values
