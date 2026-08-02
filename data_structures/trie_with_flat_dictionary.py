"""Trie (Flat Dictionary-backed).

A Trie is a special form of an N-ary tree. Typically, a trie is used to store strings. Each Trie node
represents a string (a prefix). Each node might have several children nodes while the paths to different
children nodes represent different characters. And the strings the child nodes represent will be the
origin string represented by the node itself plus the character on the path. - Leetcode

Unlike the array-backed and dictionary-backed tries, this implementation does not build an explicit tree of
node objects at all. Instead, every prefix of every inserted word is stored directly as a key in a single
flat dictionary, mapped to a boolean indicating whether that prefix is itself a complete word. This trades
memory for simplicity: lookups are O(1) since accessing elements is a direct dictionary access, but space is
O(M * N) because multiple values of a key must be tracked (plus their associated True/False values), since
every prefix of every word is stored as its own entry rather than being shared through a tree structure.
"""

from typing import Dict


class TrieWithFlatDictionary:
    """O(1) for accessing elements.

    O(M * N) - Because multiple values of a key must be tracked (plus their associated True/False values)
    """

    def __init__(self):
        """Initialize your data structure here."""
        self.nodes: Dict[str:bool] = dict()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        for index in range(1, len(word)):
            if self.nodes.get(word[:index]) is None:
                self.nodes[word[:index]] = False
        self.nodes[word] = True

    def search(self, word: str) -> bool:
        """Returns if the word is in the trie."""
        return self.nodes.get(word) is True

    def starts_with(self, prefix: str) -> bool:
        """Return if word in the trie that starts with the given prefix."""
        return self.nodes.get(prefix) is not None
