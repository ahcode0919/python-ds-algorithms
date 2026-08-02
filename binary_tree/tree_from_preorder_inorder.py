r"""Tree From Preorder and Inorder Traversal.

Given preorder and inorder traversal of a tree, construct the binary tree.

Note: You may assume that duplicates do not exist in the tree.

For example, given:

preorder = `[3, 9, 20, 15, 7]` - Top -> Bottom, Left -> Right
inorder = `[9, 3, 15, 20, 7]` - Left -> Node -> Right

Return the following binary tree:

```text
    3
   / \
  9  20
    /  \
   15   7
```
"""

from typing import List

from binary_tree.tree_node import TreeNode


def tree_from_preorder_inorder(preorder: List[int], inorder: List[int]) -> TreeNode:
    """Take the root from the front of preorder, then use inorder to split and recurse on left, then right."""
    if not preorder:
        return None

    def tree_builder(inorder_left_index, inorder_right_index):
        nonlocal preorder_index

        if inorder_left_index == inorder_right_index:
            return None

        root = TreeNode(preorder[preorder_index])
        inorder_index = index_map[root.val]
        preorder_index += 1

        root.left = tree_builder(inorder_left_index, inorder_index)
        root.right = tree_builder(inorder_index + 1, inorder_right_index)

        return root

    preorder_index = 0
    index_map = {value: index for index, value in enumerate(inorder)}

    return tree_builder(0, len(inorder))
