from typing import Generic, Optional, TypeVar

from data_structures.singly_linked_list_node import SinglyLinkedListNode

T = TypeVar('T')


class SinglyLinkedList(Generic[T]):

    def __init__(self):
        self.__head: SinglyLinkedListNode = SinglyLinkedListNode()

    def all_values(self) -> [T]:
        values = []
        node = self.__head.next

        while node:
            values.append(node.data)
            node = node.next

        return values

    # O(N)
    def append(self, data: T) -> None:
        node = SinglyLinkedListNode(data)
        last_node = self.__head

        while last_node:
            if not last_node.next:
                break
            last_node = last_node.next
        last_node.next = node

    # O(N)
    def get(self, index: int) -> Optional[T]:
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
            IndexError('Index out of bounds')

    def remove(self, index: int) -> None:
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
        count = 0
        current_node = self.__head.next

        while current_node:
            count += 1
            current_node = current_node.next
        return count
