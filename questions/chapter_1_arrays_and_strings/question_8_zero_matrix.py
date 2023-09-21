"""
Zero Matrix:
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
"""


def zero_matrix(matrix: list):
    if not matrix:
        return matrix

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    rows_with_zeros = set()
    cols_with_zeros = set()

    # Identify rows and columns with zeros
    for i_row in range(num_rows):
        for i_col in range(num_cols):
            if matrix[i_row][i_col] == 0:
                rows_with_zeros.add(i_row)
                cols_with_zeros.add(i_col)

    # Zero out rows
    for i_row in rows_with_zeros:
        matrix[i_row] = [0] * num_cols

    # Zero out columns
    for i_col in cols_with_zeros:
        for i_row in range(num_rows):
            matrix[i_row][i_col] = 0

    return matrix


