from typing import List

from collections import Counter
from binary_tree.tree_node import TreeNode


def find_mode(root: TreeNode) -> List:
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
