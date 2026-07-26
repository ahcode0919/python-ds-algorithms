from n_ary_tree.nary_tree_node import NaryTreeNode


def test_nary_tree_node():
    node = NaryTreeNode(1)
    assert node.value == 1
    assert node.children is None

    node = NaryTreeNode(1, [NaryTreeNode(2)])
    assert node.value == 1
    assert node.children[0].value == 2
