"""
Rotate Matrix:
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""


def rotate_matrix(square_matrix: list):
    if not square_matrix:
        return square_matrix

    n = len(square_matrix)

    # Create an output matrix with the same size as the input matrix
    rotated_matrix = [[None for _ in range(n)] for _ in range(n)]

    # Perform the rotation by iterating through rows and columns
    for i_row in range(n):
        for i_column in range(n):
            # Rotate the elements 90 degrees clockwise and store them in the output matrix
            rotated_matrix[i_row][i_column] = square_matrix[n - 1 - i_column][i_row]

    # Return the rotated matrix
    return rotated_matrix


def rotate_matrix_optimal(square_matrix: list):
    if not square_matrix:
        return square_matrix

    n = len(square_matrix)

    # Transpose the matrix in-place
    for i in range(n):
        for j in range(i, n):
            square_matrix[i][j], square_matrix[j][i] = square_matrix[j][i], square_matrix[i][j]

    # Reverse the columns to complete the rotation
    for i in range(n):
        square_matrix[i].reverse()

    return square_matrix

