from binary_tree.next_right_pointer import Node, next_right_pointer


def test_next_right_pointer():
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)

    processed_tree = next_right_pointer(tree)
    assert not processed_tree.next
    assert processed_tree.left.next == processed_tree.right
    assert not processed_tree.right.next
