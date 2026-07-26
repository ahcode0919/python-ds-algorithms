from data_structures.doubly_linked_list_node import DoublyLinkedListNode


def test_doubly_linked_list_node():
    node = DoublyLinkedListNode()
    assert node.data is None
    assert node.next is None
    assert node.previous is None

    node = DoublyLinkedListNode(1)
    assert node.data == 1
    assert node.previous is None
    assert node.next is None

    node = DoublyLinkedListNode(2, DoublyLinkedListNode(1), DoublyLinkedListNode(3))
    assert node.data == 2
    assert node.previous.data == 1
    assert node.next.data == 3
