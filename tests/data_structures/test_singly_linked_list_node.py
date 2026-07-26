from data_structures.singly_linked_list_node import SinglyLinkedListNode


def test_singly_linked_list_node():
    node = SinglyLinkedListNode()
    assert node.next is None
    assert node.data is None

    node = SinglyLinkedListNode(1)
    assert node.data == 1
    assert not node.next

    node = SinglyLinkedListNode(1, SinglyLinkedListNode(2))
    assert node.data == 1
    assert node.next.data == 2
