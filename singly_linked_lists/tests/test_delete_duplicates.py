from data_structures.list_node import ListNode
from singly_linked_lists.delete_duplicates import delete_duplicates
from test_helpers.test_helpers import get_list_values


def test_delete_duplicates():
    head = None
    assert delete_duplicates(head) is None

    head = ListNode(1)
    assert get_list_values(delete_duplicates(head)) == [1]

    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(4)
    assert get_list_values(delete_duplicates(head)) == [1, 2, 3, 4]
