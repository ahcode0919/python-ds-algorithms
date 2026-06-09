from data_structures.singly_linked_list_node import SinglyLinkedListNode
from singly_linked_lists.palindrome_linked_list import is_palindrome


def test_is_palindrome():
    head = SinglyLinkedListNode(1)
    assert is_palindrome(head)

    head.next = SinglyLinkedListNode(2)
    assert not is_palindrome(head)

    head.next.next = SinglyLinkedListNode(1)
    assert is_palindrome(head)
