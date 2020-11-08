from typing import List, TypeVar

T = TypeVar('T')


class Node:
    def __init__(self, value: T, children: List['Node'] = None):
        self.value = value
        self.children: List[Node] = children
