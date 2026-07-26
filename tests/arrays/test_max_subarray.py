from arrays.max_subarray import max_subarray


def test_max_subarray():
    assert max_subarray([1]) == 1
    assert max_subarray([1, 2, 3]) == 6
    assert max_subarray([1, -1, 5, -2, 3, -2]) == 6
