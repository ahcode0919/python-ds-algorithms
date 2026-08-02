"""Singly Linked List.

(https://en.wikipedia.org/wiki/Linked_list): Singly linked lists contain nodes which have a data field as
well as 'next' field, which points to the next node in line of nodes. Operations that can be performed on
singly linked lists include insertion, deletion and traversal.

Benefits:

* Dynamic data structure that can expand or shrink as needed
* Requires no extra space (memory efficient)
* Does not require a continuous block of memory like arrays

Drawbacks:

* Operations take O(N) time (Ex: Search)
* Tracking of pointers takes up additional memory
"""

from typing import Generic, Optional, TypeVar

from data_structures.singly_linked_list_node import SinglyLinkedListNode

T = TypeVar("T")


class SinglyLinkedList(Generic[T]):
    def __init__(self):
        self.__head: SinglyLinkedListNode = SinglyLinkedListNode()

    def all_values(self) -> [T]:
        """Return a list of every value in the list, in order from head to tail."""
        values = []
        node = self.__head.next

        while node:
            values.append(node.data)
            node = node.next

        return values

    # O(N)
    def append(self, data: T) -> None:
        """Add a new node containing data to the end of the list."""
        node = SinglyLinkedListNode(data)
        last_node = self.__head

        while last_node:
            if not last_node.next:
                break
            last_node = last_node.next
        last_node.next = node

    # O(N)
    def get(self, index: int) -> Optional[T]:
        """Return the data stored at index, or None if the index is out of bounds."""
        current_node = self.__head.next
        count = 0

        while current_node:
            if count == index:
                break
            current_node = current_node.next
            count += 1
        if current_node is None or count != index:
            return None
        return current_node.data

    def insert(self, data: T, index: int) -> None:
        """Insert a new node containing data before the node currently at index."""
        node = SinglyLinkedListNode(data)
        current_node = self.__head
        count = 0
        while current_node:
            if count == index:
                next_node = current_node.next
                node.next = next_node
                current_node.next = node
                return
            current_node = current_node.next
            count += 1
        if count < index:
            IndexError("Index out of bounds")

    def remove(self, index: int) -> None:
        """Remove the node at index by linking its predecessor directly to its successor."""
        count = 0
        current_node = self.__head

        while current_node:
            if count == index:
                remove_node = current_node.next
                if remove_node and remove_node.next:
                    current_node.next = remove_node.next
                    return
                current_node.next = None
            current_node = current_node.next
            count += 1

    # O(N)
    def size(self) -> int:
        """Return the number of nodes in the list."""
        count = 0
        current_node = self.__head.next

        while current_node:
            count += 1
            current_node = current_node.next
        return count
