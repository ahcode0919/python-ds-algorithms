class TrieWithDictionary:
    r"""Trie (Dictionary-backed).

    A Trie is a special form of an N-ary tree. Typically, a trie is used to store strings. Each Trie node
    represents a string (a prefix). Each node might have several children nodes while the paths to
    different children nodes represent different characters. And the strings the child nodes represent
    will be the origin string represented by the node itself plus the character on the path. - Leetcode

    ::

         head
         /  \\
        a    b
       /    /  \\
     am    ba  be
          /
        bad

    This implementation backs each node's children with a dictionary (hash table) keyed by the prefix
    string represented so far, rather than a fixed-size array. This avoids reserving space for unused
    characters and is not limited to a fixed alphabet, at the cost of hashing overhead per lookup.
    """

    def __init__(self):
        """Initialize your data structure here."""
        self.head: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        current_trie = self.head
        for index in range(1, len(word) + 1):
            if word[:index] in current_trie.child_nodes:
                current_trie = current_trie.child_nodes.get(word[:index])
            else:
                child_node = TrieNode()
                current_trie.child_nodes.setdefault(word[:index], child_node)
                current_trie = child_node

    def search(self, word: str) -> bool:
        """Returns if the word is in the trie."""
        current_trie = self.head
        for index in range(1, len(word) + 1):
            if word[:index] in current_trie.child_nodes:
                current_trie = current_trie.child_nodes.get(word[:index])
            else:
                return False
        return len(current_trie.child_nodes) == 0

    def starts_with(self, prefix: str) -> bool:
        """Returns if there is any word in the trie that starts with the given prefix."""
        current_trie = self.head
        for index in range(1, len(prefix) + 1):
            if prefix[:index] in current_trie.child_nodes:
                current_trie = current_trie.child_nodes.get(prefix[:index])
            else:
                return False
        return True


class TrieNode:
    def __init__(self):
        self.child_nodes: dict[str:TrieNode] = dict()
