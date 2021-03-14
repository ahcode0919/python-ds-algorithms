from singly_linked_lists.find_middle_node import find_middle_node
from data_structures.singly_linked_list_node import SinglyLinkedListNode


def test_find_middle_node():
    head = SinglyLinkedListNode(1)
    assert find_middle_node(head) == head

    head.next = SinglyLinkedListNode(2)
    assert find_middle_node(head) == head

    # 1, 2, 3
    head.next.next = SinglyLinkedListNode(3)
    assert find_middle_node(head) == head.next

    head.next.next.next = SinglyLinkedListNode(4)
    assert find_middle_node(head) == head.next
