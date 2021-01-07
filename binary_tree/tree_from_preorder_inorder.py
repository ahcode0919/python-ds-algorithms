from typing import List
from binary_tree.tree_node import TreeNode


def tree_from_preorder_inorder(preorder: List[int], inorder: List[int]) -> TreeNode:
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
