from src.algorithm_theory.binary_search import binary_search_iterative, binary_search_recursive


def test_binary_search_iterative():
    arr = [2, 5, 36, 40, 58]
    assert binary_search_iterative(arr, 2) == 0
    assert binary_search_iterative(arr, 5) == 1
    assert binary_search_iterative(arr, 36) == 2
    assert binary_search_iterative(arr, 40) == 3
    assert binary_search_iterative(arr, 58) == 4
    assert binary_search_iterative(arr, 1) is None


def test_binary_search_recursive():
    arr = [2, 5, 36, 40, 58]
    assert binary_search_recursive(arr, 0, len(arr) - 1, 2) == 0
    assert binary_search_recursive(arr, 0, len(arr) - 1, 5) == 1
    assert binary_search_recursive(arr, 0, len(arr) - 1, 36) == 2
    assert binary_search_recursive(arr, 0, len(arr) - 1, 40) == 3
    assert binary_search_recursive(arr, 0, len(arr) - 1, 58) == 4
    assert binary_search_recursive(arr, 0, len(arr) - 1, 1) is None
