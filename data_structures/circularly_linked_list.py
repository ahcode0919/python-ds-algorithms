from typing import Optional

from data_structures.singly_linked_list_node import SinglyLinkedListNode


class CircularlyLinkedList:
    """Circularly Linked List.

    In the last node of a list, the link field often contains a null reference, a special value used to
    indicate the lack of further nodes. A less common convention is to make it point to the first node of
    the list; in that case the list is said to be 'circular' or 'circularly linked'; otherwise it is said
    to be 'open' or 'linear'. It is a list where the last pointer points to the first node.

    This is more of an example. It can be optimized in a variety of ways depending on its intended usage.
    """

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
        """Return a list of every value in the list, starting from head and stopping once head is seen again."""
        values = []
        node = self.head

        while node:
            values.append(node.data)
            node = node.next
            if node == self.head:
                break
        return values

    def append(self, node: SinglyLinkedListNode):
        """Insert node just before head, so the list stays circular with head as the last-linked node."""
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
        """Remove the node at index, walking the ring until either it or head is reached again."""
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
        """Return the number of nodes in the ring."""
        count = 0
        if not self.head:
            return count

        count += 1
        node = self.head.next

        while node and node != self.head:
            count += 1
            node = node.next
        return count
