from typing import List
from binary_tree.tree_node import TreeNode


def tree_from_inorder_and_postorder(inorder: List[int], postorder: List[int]) -> TreeNode:
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
