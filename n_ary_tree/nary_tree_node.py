from typing import List, Optional, TypeVar

T = TypeVar('T')


class NaryTreeNode:
    def __init__(self, value: T, children: Optional[List['NaryTreeNode']] = None):
        self.value: T = value
        self.children: Optional[List[NaryTreeNode]] = children
