from typing import TypeVar
from data_structures.list_node import ListNode
from binary_tree.tree_node import TreeNode

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


def generate_binary_tree() -> TreeNode:
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    return head


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
