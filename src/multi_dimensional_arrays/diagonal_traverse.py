def diagonal_traverse(matrix: list[list[int]]) -> list[int]:
    """Diagonal Traverse.

    Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in
    diagonal order by zigzagging along each diagonal, reversing every other one, and flattening
    the results into a single list.

    Example: `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` -> `[1, 2, 4, 7, 5, 3, 6, 8, 9]`
    """
    result = []
    temp = []  # to reverse odd rows

    if not matrix or not matrix[0]:
        return result

    height, length = len(matrix), len(matrix[0])
    diagonals = range(height + length - 1)

    for diagonal in diagonals:
        row = 0 if diagonal < length else diagonal - length + 1
        col = diagonal if diagonal < length else length - 1

        while row < height and col > -1:
            temp.append(matrix[row][col])
            row += 1
            col -= 1

        if diagonal % 2 == 0:
            result.extend(temp[::-1])
        else:
            result.extend(temp)
        temp.clear()

    return result
