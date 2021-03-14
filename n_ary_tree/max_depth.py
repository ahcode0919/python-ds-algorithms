from n_ary_tree.nary_tree_node import NaryTreeNode


def max_depth_top_down(root: NaryTreeNode) -> int:
    def traverse(node, depth):
        if not node:
            return depth

        maximum_depth = depth

        if node.children:
            for child in node.children:
                maximum_depth = max(maximum_depth, traverse(child, depth + 1))
        return maximum_depth

    if not root:
        return 0

    return traverse(root, 1)


def max_depth_bottom_up(root: NaryTreeNode) -> int:
    if not root:
        return 0

    depth = 1

    if root.children:
        for child in root.children:
            depth = max(depth, max_depth_bottom_up(child) + 1)

    return depth
