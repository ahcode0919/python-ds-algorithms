from collections import deque
from typing import List, TypeVar
from data_structures.list_node import ListNode
from binary_tree.tree_node import TreeNode
from n_ary_tree.node import Node

T = TypeVar('T')


def get_binary_search_tree():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(18)
    return root


def get_binary_tree() -> TreeNode:
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    return head


def get_binary_tree_values(root: TreeNode) -> List:
    values = []
    queue = deque([root])

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            values.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return values


def get_list_values(head: T):
    node = head
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values


def get_cyclic_list_values(head: ListNode):
    if not head:
        return []

    values = [head.val]
    node = head.next

    while node is not head:
        values.append(node.val)
        node = node.next
    return values


def get_n_nary_tree():
    #         1
    #      /  |  \
    #     2   3   4
    #    / \  |  / | \
    #   5   6 8 9  10 11
    #  /                \
    # 7                  12
    root = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    root.children = [b, c, d]
    e = Node(5)
    f = Node(6)
    b.children = [e, f]
    e.children = [Node(7)]
    g = Node(8)
    c.children = [g]
    h = Node(9)
    i = Node(10)
    j = Node(11)
    d.children = [h, i, j]
    j.children = [Node(12)]
    return root


def get_n_ary_tree_values(root: Node) -> List:
    queue = deque([root])
    values = []

    while queue:
        node = queue.popleft()
        values.append(node.value)

        if not node.children:
            continue

        for child in node.children:
            queue.append(child)

    return values


def get_singly_linked_list(values: List[T]) -> ListNode[T]:
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next
