from arrays.missing_number import missing_number, missing_number_ii


def test_missing_number():
    assert missing_number([3, 0, 1]) == 2
    assert missing_number([0, 1]) == 2
    assert missing_number([2, 0]) == 1
    assert missing_number([1, 2, 3]) == 0


def test_missing_number_ii():
    assert missing_number_ii([3, 0, 1]) == 2
    assert missing_number_ii([0, 1]) == 2
    assert missing_number_ii([2, 0]) == 1
    assert missing_number_ii([1, 2, 3]) == 0
