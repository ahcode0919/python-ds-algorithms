from arrays.find_max_consecutive_ones_with_flip import find_max_consecutive_ones_with_flip


def test_find_max_consecutive_ones_with_flip():
    assert find_max_consecutive_ones_with_flip([1, 0]) == 2
    assert find_max_consecutive_ones_with_flip([0]) == 1
    assert find_max_consecutive_ones_with_flip([1]) == 1
    assert find_max_consecutive_ones_with_flip([1, 0, 1, 1, 0]) == 4
    assert find_max_consecutive_ones_with_flip([1, 0, 1, 1, 1]) == 5
    assert find_max_consecutive_ones_with_flip([0, 1, 1, 0, 1, 0]) == 4
