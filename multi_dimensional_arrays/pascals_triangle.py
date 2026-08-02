def pascals_triangle(rows: int) -> list[list[int]]:
    """Pascal's Triangle.

    Given a non-negative integer numRows, generate the first numRows of Pascal's triangle. In
    Pascal's triangle, each number is the sum of the two numbers directly above it, so each row
    is built from the previous row's adjacent sums, bounded by the leading and trailing 1s.

    Example: `5` -> `[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]`
    """
    output = []
    if rows <= 0:
        return output

    output.append([1])

    for i in range(1, rows):
        # Create row
        output.append([])
        # Set first 1
        output[i].append(1)

        # Constrain to values within first and last index of row
        for col in range(1, i):
            # Calculate total, left value is left 1 col and right value is the same col
            output[i].append(output[i - 1][col - 1] + output[i - 1][col])

        # Set last value
        output[i].append(1)
    return output
