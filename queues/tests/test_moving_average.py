from queues.moving_average import MovingAverage


def test_moving_average():
    m = MovingAverage(3)
    assert m.next(0) == 0
    assert m.next(2) == 1
    assert m.next(4) == 2
    assert m.next(12) == 6
    assert round(m.next(1), 2) == 5.67
