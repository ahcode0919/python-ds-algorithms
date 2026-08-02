from data_structures.binary_tree_node import BinaryTreeNode


class BinaryTree:
    r"""Binary Tree.

    A Binary tree is a non-linear tree data structure with one "root" node. Each node has only two child
    nodes. These are denoted "left" and "right".

    ::

             Root
              / \\
             L   R
            / \\
           L   R

    Further Reading - https://en.wikipedia.org/wiki/Binary_tree
    """

    def __init__(self, root: BinaryTreeNode = None):
        self.__root = root

    @property
    def root(self) -> BinaryTreeNode:
        return self.__root

    @root.setter
    def root(self, root: BinaryTreeNode):
        self.__root = root
