#!/usr/bin/python3

"""A module that implementing an in-place algorithm
to rotate an n x n 2D  matrix by 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """Returns a 90 degrees rotated matrix"""

    copied_matrix = matrix.copy()
    matrix.clear()

    copied_matrix.reverse()

    for i in range(len(copied_matrix)):
        temp_row = [element[i] for element in copied_matrix]
        matrix.append(temp_row)
