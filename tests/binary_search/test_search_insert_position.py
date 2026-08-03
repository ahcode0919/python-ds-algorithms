from src.binary_search.search_insert_position import search_insert


def test_search_insert():
    assert search_insert([1, 3, 5, 6], 5) == 2
    assert search_insert([1, 3, 5, 6], 1) == 0
    assert search_insert([], 1) == 0
