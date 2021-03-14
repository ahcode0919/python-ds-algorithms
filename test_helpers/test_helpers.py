from collections import deque
from typing import List, TypeVar
from data_structures.singly_linked_list_node import SinglyLinkedListNode
from binary_tree.tree_node import TreeNode
from n_ary_tree.nary_tree_node import NaryTreeNode

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


def get_list_values(head):
    node = head
    values = []
    while node:
        values.append(node.data)
        node = node.next
    return values


def get_cyclic_list_values(head: SinglyLinkedListNode):
    if not head:
        return []

    values = [head.data]
    node = head.next

    while node is not head:
        values.append(node.data)
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
    root = NaryTreeNode(1)
    b = NaryTreeNode(2)
    c = NaryTreeNode(3)
    d = NaryTreeNode(4)
    root.children = [b, c, d]
    e = NaryTreeNode(5)
    f = NaryTreeNode(6)
    b.children = [e, f]
    e.children = [NaryTreeNode(7)]
    g = NaryTreeNode(8)
    c.children = [g]
    h = NaryTreeNode(9)
    i = NaryTreeNode(10)
    j = NaryTreeNode(11)
    d.children = [h, i, j]
    j.children = [NaryTreeNode(12)]
    return root


def get_n_ary_tree_values(root: NaryTreeNode) -> List:
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


def get_singly_linked_list(values: List[T]) -> SinglyLinkedListNode[T]:
    dummy = SinglyLinkedListNode()
    current = dummy

    for value in values:
        current.next = SinglyLinkedListNode(value)
        current = current.next

    return dummy.next
