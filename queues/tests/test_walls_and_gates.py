from queues.walls_and_gates import walls_and_gates


def test_walls_and_gates():
    rooms = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647]
    ]

    assert walls_and_gates(rooms) == [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
    assert walls_and_gates([[]]) == [[]]
    assert walls_and_gates([[2147483647, 2147483647, 2147483647, 0]]) == [[3, 2, 1, 0]]
    assert walls_and_gates([[2147483647], [2147483647], [2147483647], [0]]) == [[3], [2], [1], [0]]
