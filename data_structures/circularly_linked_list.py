from typing import Optional
from data_structures.singly_linked_list_node import SinglyLinkedListNode


class CircularlyLinkedList:
    def __init__(self, node: Optional[SinglyLinkedListNode] = None):
        self.__head: SinglyLinkedListNode = node
        if node:
            node.next = self.__head

    @property
    def head(self) -> SinglyLinkedListNode:
        return self.__head

    @head.setter
    def head(self, node: SinglyLinkedListNode):
        self.__head = node
        if node:
            node.next = self.__head

    def all_values(self) -> []:
        values = []
        node = self.head

        while node:
            values.append(node.data)
            node = node.next
            if node == self.head:
                break
        return values

    def append(self, node: SinglyLinkedListNode):
        previous_node = self.head

        if not previous_node:
            self.head = node
            node.next = self.head
            return

        while previous_node.next != self.head:
            previous_node = previous_node.next

        next_node = previous_node.next
        previous_node.next = node
        node.next = next_node

    def remove(self, index: int):
        previous_node = self.head

        if not previous_node:
            raise IndexError("List is empty")

        if previous_node.next == self.head:
            self.head = None
            return

        if index == 0:
            previous_node.next = self.head.next
            self.head = previous_node.next
            return

        list_index = 1
        while previous_node.next is not self.head and list_index < index:
            previous_node = previous_node.next
            list_index += 1

        if list_index == index:
            next_node = previous_node.next
            previous_node.next = next_node.next
        else:
            raise IndexError

    def size(self) -> int:
        count = 0
        if not self.head:
            return count

        count += 1
        node = self.head.next

        while node and node != self.head:
            count += 1
            node = node.next
        return count
