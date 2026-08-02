class NaryTreeNode[T]:
    """NaryTreeNode.

    The node class used by all n-ary tree implementations. Each node holds a value and an
    optional list of child nodes.
    """

    def __init__(self, value: T, children: list["NaryTreeNode[T]"] | None = None):
        self.value: T = value
        self.children: list["NaryTreeNode[T]"] | None = children
