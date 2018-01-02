"""
Problem:
    Write an algorithm such that if an element in an MxN matrix is 0,
    its entire row and column are set to 0.

Implementation:
    TODO

Efficiency:
    Time: O(MN)
    Space: O(M+N)

"""
from typing import List


def zero_matrix(matrix: List[List[int]]) -> None:
    """
    Set the contents of an element's row and column to 0 if the element is 0.

    Args:
        matrix (List[List[int]]): The matrix we are zeroing in-place.

    """
    zero_rows = []
    zero_cols = []

    # Find the rows and the columns we want to zero
    for row, row_slice in enumerate(matrix):
        for col, value in enumerate(row_slice):
            if value == 0:
                zero_rows.append(row)
                zero_cols.append(col)

    # Zero the correct rows
    for row in zero_rows:
        for i in range(len(matrix[row])):
            matrix[row][i] = 0

    # Zero the correct columns
    for row in range(len(matrix)):
        for col in zero_cols:
            matrix[row][col] = 0


# 1x1 matrix
m = [[1]]
zero_matrix(m)
assert m == [[1]]

# 1x1 matrix
m = [[0]]
zero_matrix(m)
assert m == [[0]]

# 1x2 matrix
m = [[1, 0]]
zero_matrix(m)
assert m == [[0, 0]]

# 2x1 matrix
m = [
    [1],
    [0]
]
zero_matrix(m)
assert m == [
    [0],
    [0]
]

# 2x2 matrix
m = [
    [1, 1],
    [0, 1]
]
zero_matrix(m)
assert m == [
    [0, 1],
    [0, 0]
]

# 3x3 matrix
m = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
zero_matrix(m)
assert m == [
    [1, 0, 1],
    [0, 0, 0],
    [1, 0, 1]
]

# 4x5 matrix with two zeros
m = [
    [1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0]
]
zero_matrix(m)
assert m == [
    [1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
]