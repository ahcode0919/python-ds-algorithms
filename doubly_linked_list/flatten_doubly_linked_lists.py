"""Flatten a Multilevel Doubly Linked List.

You are given a doubly linked list which in addition to the next and previous pointers, could have a
child pointer, which may or may not point to a separate doubly linked list. These child lists may have
one or more children of their own, and so on, to produce a multilevel data structure.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the
head of the first level of the list.

Example: `1 = 2 = 3 =|= 6 = 7` with `3` having a child list `4 = 5` -> `1 = 2 = 3 = 4 = 5 = 6 = 7`

Both solutions run in O(N) time. The recursive solution uses O(N) space for the call stack, while the
iterative solution uses O(N) space for the explicit stack.
"""

from typing import Optional


class Node:
    """A doubly linked list node that may additionally point to a child sub-list."""

    def __init__(
        self,
        val: int,
        previous_node: Optional["Node"],
        next_node: Optional["Node"],
        child_node: Optional["Node"],
    ):
        self.data: int = val
        self.previous: Optional["Node"] = previous_node
        self.next: Optional["Node"] = next_node
        self.child: Optional["Node"] = child_node


def flatten(head: Node) -> Node:
    """Recursively flatten each child list in place as it is encountered, then splice it back in."""
    if not head:
        return head

    current = head

    while current:
        if current.child:
            next_node = current.next
            new_list = flatten(current.child)
            current.child = None
            current.next = new_list
            new_list.previous = current

            new_list_end_node = new_list
            while new_list_end_node.next:
                new_list_end_node = new_list_end_node.next
            new_list_end_node.next = next_node
            if next_node:
                next_node.previous = new_list_end_node
            current = next_node
        else:
            current = current.next

    return head


def flatten_iterative(head: Node) -> Node:
    """Use an explicit stack of nodes to flatten the list without recursion."""
    if not head:
        return head

    dummy = Node(0, None, head, None)
    previous = dummy

    stack = list()
    stack.append(head)

    while stack:
        current = stack.pop()
        previous.next = current
        current.previous = previous

        if current.next:
            stack.append(current.next)

        if current.child:
            stack.append(current.child)
            current.child = None

        previous = current
    dummy.next.previous = None
    return dummy.next
