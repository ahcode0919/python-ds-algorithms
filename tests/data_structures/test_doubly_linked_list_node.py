from src.data_structures.doubly_linked_list_node import DoublyLinkedListNode


def test_doubly_linked_list_node():
    node = DoublyLinkedListNode(1)
    assert node.data == 1
    assert node.previous is None
    assert node.next is None

    node = DoublyLinkedListNode(2, DoublyLinkedListNode(1), DoublyLinkedListNode(3))
    assert node.data == 2
    assert node.previous and node.previous.data == 1
    assert node.next and node.next.data == 3
