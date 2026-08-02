r"""In-order Traversal.

In-order traversal is to traverse the left subtree first. Then visit the root. Finally, traverse the right
subtree.

Example:
```text
     1
    / \
   2   3
  / \
 4   5
```

Output: `[4, 2, 5, 1, 3]`

"""

from binary_tree.tree_node import TreeNode


def inorder_traversal(root: TreeNode) -> list[int]:
    """Recursively traverse left, visit the node, then traverse right."""
    values = []

    if not root:
        return values

    if root.left:
        values.extend(inorder_traversal(root.left))
    values.append(root.val)

    if root.right:
        values.extend(inorder_traversal(root.right))

    return values


def inorder_traversal_stack(root: TreeNode) -> list[int]:
    """Traverse iteratively using an explicit stack to walk down the left spine before visiting a node."""
    output = []
    stack = []
    current_node = root

    while current_node or len(stack) > 0:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left
        current_node = stack.pop()
        output.append(current_node.val)
        current_node = current_node.right

    return output
