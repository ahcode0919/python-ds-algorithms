# Trie

* [Map Sum](#map-sum)

## Map Sum

Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer
represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs'
value whose key starts with the prefix.

Example 1:

```text
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
```

```python
class MapSum:
    def __init__(self):
        self.value = 0
        self.nodes: Dict[str: MapSumNode] = dict()

    def insert(self, key: str, val: int) -> None:
        current_node = self
        for index in range(1, len(key) + 1):
            if key[0:index] in current_node.nodes:
                current_node = current_node.nodes.get(key[0:index])
            else:
                current_node.nodes.setdefault(key[0:index], MapSumNode())
                current_node = current_node.nodes.get(key[0:index])
        current_node.value = val

    def sum(self, prefix: str) -> int:
        current_node = self
        # Find target node
        for index in range(1, len(prefix) + 1):
            if prefix[0:index] in current_node.nodes:
                current_node = current_node.nodes.get(prefix[0:index])
            else:
                return 0 # node does not exist
        # sum child nodes
        return self.__recursive_sum(current_node)

    def __recursive_sum(self, parent_node) -> int:
        if len(parent_node.nodes) == 0:
            return parent_node.value

        total = parent_node.value

        for node in parent_node.nodes:
            total += self.__recursive_sum(parent_node.nodes.get(node))
        return total


class MapSumNode:
    def __init__(self, value: int = 0):
        self.value = value
        self.nodes: Dict[str: MapSumNode] = dict()
```