"""Rotate Image 90 Degrees Clockwise.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise). Try to solve
this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

Example: `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` -> `[[7, 4, 1], [8, 5, 2], [9, 6, 3]]`
"""


def rotate_image_90_degrees(matrix: [[int]]) -> [[int]]:
    """Rotate each concentric layer in place by cycling four corresponding elements at a time."""
    size = len(matrix)
    layer_count = int(size / 2)

    for layer in range(0, layer_count):
        last = size - layer - 1

        for element in range(layer, last):
            offset = element - layer

            top = matrix[layer][element]
            right_side = matrix[element][last]
            bottom = matrix[last][last - offset]
            left_side = matrix[last - offset][layer]

            matrix[layer][element] = left_side
            matrix[element][last] = top
            matrix[last][last - offset] = right_side
            matrix[last - offset][layer] = bottom
    return matrix
