from collections import deque
from typing import List


def walls_and_gates(rooms_input: List[List[int]]) -> List[List[int]]:
    """Walls and Gates (BFS).

    Run a multi-source BFS from every gate to fill each empty room with its distance to the
    nearest gate.

    You are given a m x n 2D grid initialized with these three possible values: `-1` - a wall or
    an obstacle; `0` - a gate; `INF` - infinity, meaning an empty room. We use the value
    `2^31 - 1 = 2147483647` to represent INF as you may assume that the distance to a gate is less
    than `2147483647`. Fill each empty room with the distance to its nearest gate. If it is
    impossible to reach a gate, it should be filled with INF.

    Example: given the 2D grid
    ```
    INF  -1  0  INF
    INF INF INF  -1
    INF  -1 INF  -1
      0  -1 INF INF
    ```
    after running the function, the 2D grid should be
    ```
    3  -1   0   1
    2   2   1  -1
    1  -1   2  -1
    0  -1   3   4
    ```
    """
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
