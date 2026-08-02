from typing import List, Optional, TypeVar

T = TypeVar("T")


class NaryTreeNode:
    """NaryTreeNode.

    The node class used by all n-ary tree implementations. Each node holds a value and an
    optional list of child nodes.
    """

    def __init__(self, value: T, children: Optional[List["NaryTreeNode"]] = None):
        self.value: T = value
        self.children: Optional[List[NaryTreeNode]] = children
