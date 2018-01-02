"""
Problem:
    Write an algorithm such that if an element in an MxN matrix is 0,
    its entire row and column are set to 0.

Implementation:
    My initial, naive approach to the problem was to first find all
    occurrences of zeros and add their row and column values to two lists.
    Afterwards, we would check these lists and zero their respective rows and
    columns. This works well, but we still need to allocate an additional
    O(M+N) space for the two lists.

    Instead, we can reduce this to O(1) space by storing this information of
    what rows and columns to zero in the original matrix itself.

    This relies on the order in which we check the values in the matrix. When
    we check a value, we have checked all of the values preceding it -- the
    values in all previous rows, and all previous columns of that row.

    We can then set the first row at that column to zero, and the first column
    at that row to zero. These two slices of our matrix will store the
    information we need to zero all elements in these rows and columns. After
    parsing the matrix for zeros, we then just need to parse the first row and
    the first column.

Efficiency:
    Time: O(MN)
    Space: O(1)

"""
from typing import List


def zero_matrix(matrix: List[List[int]]) -> None:
    """
    Set the contents of an element's row and column to 0 if the element is 0.

    Args:
        matrix (List[List[int]]): The matrix we are zeroing in-place.

    """
    # Find the rows and the columns we want to zero
    for row, row_slice in enumerate(matrix):
        for col, value in enumerate(row_slice):
            if value == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0

    # Zero the correct rows
    for row in range(1, len(matrix)):
        if matrix[row][0] == 0:
            for col in range(len(matrix[row])):
                matrix[row][col] = 0

    # Zero the correct columns
    for col in range(1, len(matrix[0])):
        if matrix[0][col] == 0:
            for row in range(len(matrix)):
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
