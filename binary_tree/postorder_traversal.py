r"""Post-order Traversal.

Algorithm Postorder(tree):

1. Traverse the left subtree.
2. Traverse the right subtree.
3. Visit the root.

Example:
```text
     1
    / \
   2   3
  / \
 4   5
```

Output: `[4, 5, 2, 3, 1]`

"""

from binary_tree.tree_node import TreeNode


def postorder_traversal_recursive(root: TreeNode) -> list[int]:
    """Recursively traverse left, traverse right, then visit the node."""
    values = []
    if not root:
        return values

    if root.left:
        values.extend(postorder_traversal_recursive(root.left))
    if root.right:
        values.extend(postorder_traversal_recursive(root.right))

    values.append(root.val)

    return values


def postorder_traversal_iterative(root: TreeNode) -> list[int]:
    """Traverse iteratively with an explicit stack, visiting a node only after both children are handled."""
    values = []
    stack = []

    while root or stack:
        while root:
            if root.right:
                stack.append(root.right)
            stack.append(root)
            root = root.left

        root = stack.pop()

        if stack and root.right == stack[-1]:
            stack[-1] = root
            root = root.right
        else:
            values.append(root.val)
            root = None

    return values
