"""Replace Words.

In English, we have a concept called root, which can be followed by some other words to form another longer word -
let's call this word successor. For example, the root "an", followed by "other", can form another word "another".

Now, given a dictionary consisting of many roots and a sentence, replace all the successors in the sentence with the
root forming it. If a successor has many roots that can form it, replace it with the root with the shortest length.
Output the sentence after the replacement.

Example: `dictionary = ["cat", "bat", "rat"]`, `sentence = "the cattle was rattled by the battery"` ->
`"the cat was rat by the bat"`
"""

from typing import Dict, List


def replace_words(dictionary: List[str], sentence: str) -> str:
    """Build a prefix trie from dictionary roots, then replace each sentence word with its shortest matching root."""
    words = sentence.split(" ")
    updated_sentence: [str] = []
    prefix_trie = TrieNode()

    for word in dictionary:
        prefix_trie.insert(word)

    for word in words:
        updated_sentence.append(prefix_trie.replace_word(word))

    return " ".join(updated_sentence)


class TrieNode:
    """A prefix trie node used to store dictionary roots and match sentence words against them."""

    def __init__(self):
        self.nodes: Dict[str:TrieNode] = dict()

    def insert(self, word: str) -> None:
        """Insert word into the trie, stopping early if a shorter existing root already covers it."""
        current_node = self
        for index in range(1, len(word) + 1):
            if word[:index] in current_node.nodes:
                next_node = current_node.nodes.get(word[:index])
                if len(next_node.nodes) == 0:
                    return
                if index == len(word):
                    current_node.nodes[word[:index]] = TrieNode()
                    return
                current_node = next_node
            else:
                current_node.nodes.setdefault(word[:index], TrieNode())
                current_node = current_node.nodes.get(word[:index])

    def replace_word(self, word: str) -> str:
        """Walk the trie along word's prefixes and return the shortest matching root, or word unchanged."""
        current_node = self
        for index in range(1, len(word) + 1):
            if word[:index] in current_node.nodes:
                current_node = current_node.nodes.get(word[:index])
                if len(current_node.nodes) == 0:
                    return word[:index]
            else:
                return word
        return word
