def pascals_triangle_ii(row_index: int) -> list[int]:
    """Pascal's Triangle II.

    Given an integer row_index, return the row of Pascal's triangle at that index (0-indexed).

    ```
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
    ```

    Build each row in place from the previous one, working right to left to avoid overwriting values still needed.
    """
    row = [1]

    # Generate a row by adding numbers right to left  ([i] + [i - 1])
    # then append a closing 1

    for i in range(row_index):
        for j in range(i, 0, -1):
            row[j] = row[j] + row[j - 1]
        row.append(1)

    return row
