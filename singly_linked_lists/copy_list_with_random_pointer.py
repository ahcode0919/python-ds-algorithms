"""Copy List with Random Pointer.

A linked list is given such that each node contains an additional random pointer which could point to any node in
the list or None.

Return a deep copy of the list.
"""

from typing import Dict, Optional


class Node:
    """A linked list node with an additional pointer that may reference any other node in the list."""

    def __init__(self, value: int, next_node: "Node" = None, random: "Node" = None):
        self.value = value
        self.next = next_node
        self.random = random


def copy_random_list(head: Node) -> Node:
    """Walk the list once, cloning each node and its `random` target via a visited-node lookup."""
    if not head:
        return None

    current = head
    nodes = {}
    new_node = Node(head.value, None, None)
    nodes[current] = new_node

    while current:
        new_node.random = get_cloned_node(current.random, nodes)
        new_node.next = get_cloned_node(current.next, nodes)
        current = current.next
        new_node = new_node.next

    return get_cloned_node(head, nodes)


def get_cloned_node(node: Node, visited: Dict) -> Optional[Node]:
    """Return the existing clone of node from visited, creating and caching one if it doesn't exist yet."""
    if node:
        if node in visited:
            return visited[node]
        visited[node] = Node(node.value, None, None)
        return visited[node]
    return None
