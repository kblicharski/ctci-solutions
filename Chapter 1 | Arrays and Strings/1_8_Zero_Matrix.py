"""
Problem:
    Write an algorithm such that if an element in an MxN matrix is 0,
    its entire row and column are set to 0.

Implementation:
    TODO

Efficiency:
    Time: TODO
    Space: TODO

"""
from typing import List


def zero_matrix(matrix: List[List[int]]) -> None:
    """
    Set the contents of an element's row and column to 0 if the element is 0.

    Args:
        matrix (List[List[int]]): The matrix we are zeroing in-place.

    """
    print(matrix)


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