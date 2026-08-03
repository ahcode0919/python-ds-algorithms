from src.arrays.make_array_consecutive import make_array_consecutive


def test_make_array_consecutive():
    assert make_array_consecutive([6, 2, 3, 8]) == 3
    assert make_array_consecutive([]) == 0
    assert make_array_consecutive([1]) == 0
    assert make_array_consecutive([1, 2]) == 0
