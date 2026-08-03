class Node[T]:
    """A linked list node with an additional pointer that may reference any other node in the list."""

    def __init__(self, value: int, next_node: "Node | None" = None, random: "Node | None" = None):
        self.value: int = value
        self.next: Node[T] | None = next_node
        self.random: Node[T] | None = random


def copy_random_list[T](head: Node[T]) -> Node[T] | None:
    """Copy List with Random Pointer.

    A linked list is given such that each node contains an additional random pointer which could point to any
    node in the list or None.

    Return a deep copy of the list.

    Walks the list once, cloning each node and its `random` target via a visited-node lookup.
    """
    current: Node[T] | None = head
    nodes: dict[Node[T], Node[T]] = {}
    new_node: Node[T] | None = Node[T](head.value, None, None)
    nodes[current] = new_node

    while current and new_node:
        new_node.random = get_cloned_node(current.random, nodes)
        new_node.next = get_cloned_node(current.next, nodes)
        current = current.next
        new_node = new_node.next

    return get_cloned_node(head, nodes)


def get_cloned_node[T](node: Node[T] | None, visited: dict[Node[T], Node[T]]) -> Node[T] | None:
    """Return the existing clone of node from visited, creating and caching one if it doesn't exist yet."""
    if node:
        if node in visited:
            return visited[node]
        visited[node] = Node(node.value, None, None)
        return visited[node]
    return None
