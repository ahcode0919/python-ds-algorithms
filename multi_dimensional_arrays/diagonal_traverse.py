from typing import List
# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order.
# #
# # Input:
# # ```
# #     [[1, 2, 3],
# #      [4, 5, 6],
# #      [7, 8, 9]]
# # ```
# # Output: `1, 2, 4, 7, 5, 3, 6, 8, 9`

def diagonal_traverse(matrix: List[List[int]]) -> List[int]:
    start = [0, 0]
    end = [len(matrix) - 1, len(matrix[0])]
    current = start[::1]
    increments = 0

