r"""Binary Tree Path.

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:
Input:

```text
   1
 /   \
2     3
 \
  5
```

Output: `["1->2->5", "1->3"]`

Explanation: All root-to-leaf paths are: `1->2->5`, `1->3`

"""


class TreeNode:
    """Minimal binary tree node used by this module's examples."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def binary_tree_paths(root_node: TreeNode) -> [str]:
    """Collect every root-to-leaf path into a list of `"parent->child"` strings."""
    paths = []
    if not root_node:
        return paths
    return get_path(root_node, "", paths)


def get_path(node: TreeNode, path: str, paths: [str]) -> [str]:
    """Recurse left and right, appending a completed path string whenever a leaf is reached."""
    new_paths = list(paths)

    if not node.left and not node.right:
        new_paths.append(path + str(node.val))
        return new_paths
    if node.left:
        new_paths += get_path(node.left, path + str(node.val) + "->", paths)
    if node.right:
        new_paths += get_path(node.right, path + str(node.val) + "->", paths)
    return new_paths
