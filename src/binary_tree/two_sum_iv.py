from src.binary_tree.tree_node import TreeNode


def two_sum_iv(root: TreeNode, target: int) -> bool:
    """Two Sum IV.

    Given the root of a Binary Tree and a target number, return `True` if there exist two elements in
    the BST such that their sum is equal to the given target.

    Traverses the tree while tracking seen values, returning True as soon as a complementary value is
    found.
    """
    if not root:
        return False

    values = set()
    queue = [root]

    while queue:
        node = queue.pop()

        if node:
            if target - node.val in values:
                return True
            values.add(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return False
