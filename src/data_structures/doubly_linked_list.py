from src.data_structures.doubly_linked_list_node import DoublyLinkedListNode


class DoublyLinkedList[T]:
    """Doubly Linked List.

    (https://en.wikipedia.org/wiki/Doubly_linked_list): In a 'doubly linked list', each node contains,
    besides the next-node link, a second link field pointing to the 'previous' node in the sequence. This
    implementation uses sentinel head and tail nodes so insertion and removal never need to special-case an
    empty list.
    """

    def __init__(self):
        self._head: DoublyLinkedListNode[T] = DoublyLinkedListNode[T](None)
        self._tail: DoublyLinkedListNode[T] = DoublyLinkedListNode[T](None)

        self._head.next = self._tail
        self._tail.previous = self._head

    # O(N)
    def all_values(self) -> list[T | None]:
        """Return a list of every value in the list, in order from head to tail."""
        values = []
        node = self._head.next

        while node and node is not self._tail:
            values.append(node.data)
            node = node.next

        return values

    # O(1)
    def append(self, data: T):
        """Add a new node containing data to the end of the list, just before the sentinel tail."""
        # Last <-> Tail --> Last <-> New <-> Tail
        node = DoublyLinkedListNode(data)
        last_node = self._tail.previous

        if last_node:
            last_node.next = node
            node.previous = last_node

            node.next = self._tail
            self._tail.previous = node

    # O(N)
    def get_node(self, index: int) -> DoublyLinkedListNode | None:
        """Return the node at index, or None if the index is out of bounds."""
        current_node = self._head.next
        count = 0

        while current_node and current_node is not self._tail:
            if count == index:
                return current_node
            current_node = current_node.next
            count += 1
        return None

    # O(N)
    def get(self, index: int) -> T | None:
        """Return the data stored at index, or None if the index is out of bounds."""
        node = self.get_node(index)
        if node:
            return node.data
        return None

    # O(N)
    def insert(self, data: T, index: int):
        """Insert a new node containing data before the node currently at index."""
        node = DoublyLinkedListNode[T](data)
        current_node: DoublyLinkedListNode[T] | None = self.get_node(index)

        if not current_node and index == 0:
            self._head.next = node
            node.previous = self._head
            node.next = self._tail
            self._tail.previous = node
            return

        if not current_node or not current_node.previous:
            raise IndexError("Index out of bounds")

        # Previous <-> Original --> Previous <-> New <-> Original
        current_node.previous.next = node
        node.previous = current_node.previous
        node.next = current_node
        current_node.previous = node

    # O(N)
    def remove(self, index: int) -> T | None:
        """Remove the node at index by linking its neighbors directly to each other and return its data."""
        node = self.get_node(index)
        if not node or not node.previous or not node.next:
            return None

        # Previous <-> Node <-> Next --> Previous <-> Next
        node.previous.next = node.next
        node.next.previous = node.previous

        return node.data

    # O(N)
    def size(self) -> int:
        """Return the number of nodes in the list."""
        count = 0
        node = self._head.next

        while node and node != self._tail:
            count += 1
            node = node.next
        return count
