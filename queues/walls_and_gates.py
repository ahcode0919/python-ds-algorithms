from collections import deque
from typing import List


def walls_and_gates(rooms_input: List[List[int]]) -> List[List[int]]:
    rooms = rooms_input[:]
    height = len(rooms)
    if height == 0:
        return [[]]

    width = len(rooms[0])
    queue = deque()

    for row in range(height):
        for col in range(width):
            if rooms[row][col] == 0:
                queue.appendleft((row, col))

    # (Row, Col)
    # Up, Down, Right, Left
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while queue:
        point = queue.pop()
        for direction in directions:
            row = point[0] + direction[0]
            col = point[1] + direction[1]
            if row < 0 or col < 0 or row >= height or col >= width or rooms[row][col] != 2147483647:
                continue
            rooms[row][col] = rooms[point[0]][point[1]] + 1
            queue.appendleft((row, col))

    return rooms
