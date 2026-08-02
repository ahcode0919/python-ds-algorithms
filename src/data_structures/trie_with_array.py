class TrieWithArray[T]:
    r"""Trie (Array-backed).

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

    This implementation backs each node's children with a fixed-size array of 26 slots (one per lowercase
    letter a-z), indexed by `ord(char) - ord("a")`. Lookups are O(1) per character since the child slot is
    computed directly, but every node reserves space for all 26 possible children whether or not they are
    used.
    """

    def __init__(self):
        self.head: TrieNode[T] = TrieNode[T]()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        current_trie = self.head

        for index in range(1, len(word) + 1):
            node_index = ord(word[:index][-1]) - ord("a")
            next_node = current_trie.child_nodes[node_index]
            if next_node is not None:
                current_trie = next_node
            else:
                new_node = TrieNode()
                current_trie.child_nodes[node_index] = new_node
                current_trie = new_node

    def search(self, word: str) -> bool:
        """Returns True if the word is in the trie."""
        current_trie = self.head

        for index in range(1, len(word) + 1):
            node_index = ord(word[:index][-1]) - ord("a")
            next_node = current_trie.child_nodes[node_index]
            if next_node is not None:
                current_trie = next_node
            else:
                return False
        return current_trie.child_nodes == [None] * 26

    def starts_with(self, prefix: str) -> bool:
        """Returns True if there is any word in the trie that starts with the given prefix."""
        current_trie = self.head

        for index in range(1, len(prefix) + 1):
            node_index = ord(prefix[:index][-1]) - ord("a")
            next_node = current_trie.child_nodes[node_index]
            if next_node is not None:
                current_trie = next_node
            else:
                return False
        return True


class TrieNode[T]:
    def __init__(self):
        self.child_nodes: list[TrieNode[T] | None] = [None] * 26
