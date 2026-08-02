from binary_tree.tree_node import TreeNode


def tree_from_inorder_and_postorder(inorder: list[int], postorder: list[int]) -> TreeNode:
    r"""Tree from Inorder and Postorder Traversal.

    Given inorder and postorder traversal of a tree, construct the binary tree.

    Note: You may assume that duplicates do not exist in the tree.

    For example, given:

    inorder = `[9, 3, 15, 20, 7]` - Left -> Node -> Right
    postorder = `[9, 15, 7, 20, 3]` - Left -> Right -> Node

    Return the following binary tree:

    ```text
        3
       / \
      9  20
        /  \
       15   7
    ```

    Pops the root from the end of postorder, then uses inorder to split and recurse on right, then left.
    """

    def helper(in_left, in_right):
        if in_left > in_right:
            return None

        # last element is root
        value = postorder.pop()
        root = TreeNode(value)

        middle = index_map[value]

        root.right = helper(middle + 1, in_right)
        root.left = helper(in_left, middle - 1)

        return root

    index_map = {value: index for index, value in enumerate(inorder)}

    return helper(0, len(inorder) - 1)
