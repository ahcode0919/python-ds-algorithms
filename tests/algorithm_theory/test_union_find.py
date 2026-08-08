from src.algorithm_theory.union_find import UnionFind


def test_initializer():
    union_find = UnionFind()
    assert union_find.size() == 0
    assert union_find.components() == 0


def test_components():
    union_find = UnionFind()
    union_find.add_edges(7, [(0, 2), (1, 0), (4, 3), (2, 5), (3, 6)])

    assert union_find.components() == 2
