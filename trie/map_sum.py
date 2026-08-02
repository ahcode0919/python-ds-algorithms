from typing import Dict


class MapSum:
    """Map Sum.

    Trie-backed map where every node caches the summed value of its subtree's keys.

    Implement a MapSum class with insert, and sum methods.

    For the method insert, you'll be given a pair of (string, integer). The string represents the key and the
    integer represents the value. If the key already existed, then the original key-value pair will be overridden
    to the new one.

    For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the
    pairs' value whose key starts with the prefix.

    Example: `insert("apple", 3)` -> `None`, `sum("ap")` -> `3`, `insert("app", 2)` -> `None`, `sum("ap")` -> `5`
    """

    def __init__(self):
        self.value = 0
        self.head: MapSumNode = MapSumNode()

    def insert(self, key: str, val: int) -> None:
        """Insert key into the trie, one node per prefix, and set the leaf's value."""
        current_node = self.head
        for index in range(1, len(key) + 1):
            if key[:index] in current_node.nodes:
                current_node = current_node.nodes.get(key[:index])
            else:
                current_node.nodes.setdefault(key[:index], MapSumNode())
                current_node = current_node.nodes.get(key[:index])
        current_node.value = val

    def sum(self, prefix: str) -> int:
        """Walk to the node for prefix, then sum the values of every key in its subtree."""
        current_node = self.head
        # Find target node
        for index in range(1, len(prefix) + 1):
            if prefix[:index] in current_node.nodes:
                current_node = current_node.nodes.get(prefix[:index])
            else:
                return 0

        # sum child nodes
        return self.__recursive_sum(current_node)

    def __recursive_sum(self, parent_node) -> int:
        """Recursively add parent_node's own value to the sum of all its child nodes."""
        if len(parent_node.nodes) == 0:
            return parent_node.value

        total = parent_node.value

        for node in parent_node.nodes:
            total += self.__recursive_sum(parent_node.nodes.get(node))
        return total


class MapSumNode:
    """A single node in the MapSum trie, storing a value and its child prefix nodes."""

    def __init__(self, value: int = 0):
        self.value = value
        self.nodes: Dict[str:MapSumNode] = dict()
