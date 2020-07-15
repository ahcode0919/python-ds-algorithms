from arrays.rotate_array import rotate_array_with_array


def test_rotate_array_with_array():
    nums = [1, 2, 3, 4, 5, 6]
    assert rotate_array_with_array(nums, 3) == [4, 5, 6, 1, 2, 3]
