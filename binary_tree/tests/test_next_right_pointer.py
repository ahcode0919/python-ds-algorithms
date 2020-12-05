from binary_tree.next_right_pointer import next_right_pointer, Node


def test_next_right_pointer():
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)

    processed_tree = next_right_pointer(tree)
    assert not processed_tree.next
    assert processed_tree.left.next == processed_tree.right
    assert not processed_tree.right.next
