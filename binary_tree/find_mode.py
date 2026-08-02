"""Find Mode.

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in
the given BST.
"""

from collections import Counter
from typing import List

from binary_tree.tree_node import TreeNode


def find_mode(root: TreeNode) -> List:
    """Count occurrences of every value with a full traversal and return the value(s) with the highest count."""
    counter = Counter()
    values = []

    def traverse(cnt, node):
        if not node:
            return
        cnt[node.val] += 1
        traverse(cnt, node.left)
        traverse(cnt, node.right)

    traverse(counter, root)
    largest = counter.most_common(1)

    if not largest:
        return values

    for element in counter:
        if counter[element] == largest[0][1]:
            values.append(element)

    return values
