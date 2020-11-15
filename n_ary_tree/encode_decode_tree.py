from collections import deque
from typing import Optional
from binary_tree.tree_node import TreeNode
from n_ary_tree.node import Node


def encode(root: Node) -> Optional[TreeNode]:
    if not root:
        return None

    root_node = TreeNode(root.value)
    queue = deque([(root_node, root)])

    while queue:
        parent, current = queue.popleft()
        previous = None
        head = None

        if current.children:
            for child in current.children:
                node = TreeNode(child.value)

                if previous:
                    previous.right = node
                else:
                    head = node
                previous = node
                queue.append((node, child))

        parent.left = head

    return root_node


def decode(data: TreeNode) -> Optional[Node]:
    if not data:
        return None

    root = Node(data.val, [])
    queue = deque([(root, data)])

    while queue:
        parent, current = queue.popleft()
        first_child = current.left
        sibling = first_child

        while sibling:
            node = Node(sibling.val, [])
            parent.children.append(node)
            queue.append((node, sibling))
            sibling = sibling.right

    return root
