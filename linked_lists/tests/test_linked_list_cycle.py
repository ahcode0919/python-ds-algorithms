from linked_lists.linked_list_cycle import ListNode, has_cycle


def test_linked_list_cycle():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next
    assert has_cycle(head)

    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    assert not has_cycle(head2)
