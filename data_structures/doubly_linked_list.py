from typing import Generic, Optional, TypeVar
from data_structures.doubly_linked_list_node import DoublyLinkedListNode

T = TypeVar('T')


class DoublyLinkedList(Generic[T]):

    def __init__(self):
        self.__head: DoublyLinkedListNode = DoublyLinkedListNode()
        self.__tail: DoublyLinkedListNode = DoublyLinkedListNode()

        self.__head.next = self.__tail
        self.__tail.previous = self.__head

    # O(N)
    def all_values(self) -> [T]:
        values = []
        node = self.__head.next

        while node is not self.__tail:
            values.append(node.data)
            node = node.next

        return values

    # O(1)
    def append(self, data: T):
        # Last <-> Tail --> Last <-> New <-> Tail
        node = DoublyLinkedListNode(data)
        last_node = self.__tail.previous

        last_node.next = node
        node.previous = last_node

        node.next = self.__tail
        self.__tail.previous = node

    # O(N)
    def get_node(self, index: int) -> Optional[DoublyLinkedListNode]:
        current_node = self.__head.next
        count = 0

        while current_node is not self.__tail:
            if count == index:
                return current_node
            current_node = current_node.next
            count += 1
        return None

    # O(N)
    def get(self, index: int) -> Optional[T]:
        node = self.get_node(index)
        if node:
            return node.data
        return None

    # O(N)
    def insert(self, data: T, index: int):
        node = DoublyLinkedListNode(data)
        current_node: DoublyLinkedListNode = self.get_node(index)

        if not current_node and index == 0:
            self.__head.next = node
            node.previous = self.__head
            node.next = self.__tail
            self.__tail.previous = node
            return

        if not current_node:
            raise IndexError("Index out of bounds")

        # Previous <-> Original --> Previous <-> New <-> Original
        current_node.previous.next = node
        node.previous = current_node.previous
        node.next = current_node
        current_node.previous = node

    # O(N)
    def remove(self, index: int) -> Optional[T]:
        node = self.get_node(index)
        if not node:
            return None

        # Previous <-> Node <-> Next --> Previous <-> Next
        node.previous.next = node.next
        node.next.previous = node.previous

        return node.data

    # O(N)
    def size(self) -> int:
        count = 0
        node = self.__head.next

        while node != self.__tail:
            count += 1
            node = node.next
        return count
