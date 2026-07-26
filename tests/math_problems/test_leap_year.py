from math_problems.leap_year import leap_year


def test_leap_year():
    assert leap_year(2000)
    assert leap_year(2400)
    assert not leap_year(1800)
    assert not leap_year(1900)
    assert not leap_year(2100)
    assert not leap_year(2200)
    assert not leap_year(2300)
