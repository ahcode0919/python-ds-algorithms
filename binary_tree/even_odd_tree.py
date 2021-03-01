from collections import deque
from binary_tree.tree_node import TreeNode


def even_odd_tree(root: TreeNode):
    if not root:
        return False

    level = deque([root])
    even = True

    while level:
        last_value = None

        for _ in range(len(level)):
            node = level.popleft()

            if even:
                if node.val % 2 == 0:
                    return False
                if last_value and node.val <= last_value:
                    return False
            else:
                if node.val % 2 != 0:
                    return False
                if last_value and node.val >= last_value:
                    return False

            last_value = node.val

            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        even = not even

    return True
