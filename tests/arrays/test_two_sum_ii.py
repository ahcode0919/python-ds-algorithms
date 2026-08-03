from src.arrays.two_sum_ii import two_sum_ii


def test_two_sum_ii():
    assert two_sum_ii([2, 7, 11, 15], 1) == []
    assert two_sum_ii([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum_ii([2, 7, 11, 15], 26) == [3, 4]
    assert two_sum_ii([-1, 0], -1) == [1, 2]
