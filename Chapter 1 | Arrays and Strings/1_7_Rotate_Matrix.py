"""
Problem:
    Given an image represented by an NxN matrix, where each pixel in the
    image is 4 bytes, write a method to rotate the image by 90 degrees. Can
    you do this in place?

Implementation:
    Note: Because we have a square matrix, it is possible to do this in-place.
    If we did not have a square matrix, we would have to return a new matrix.

    After writing the test cases, it became clear what the pattern should be.
    The replacement of values follows a similar "rotation" for each layer.

    Because of the in-place substitution, this is not only slightly faster, but
    does not use an additional O(MM) space for the rotated matrix.

Efficiency:
    Time: O(MM)
    Space: O(1)

"""
from typing import List


def rotate_matrix(matrix: List[List[int]]) -> None:
    """
    Rotate a square NxN matrix in-place.

    Args:
        matrix (List[List[int]]): The matrix to be rotated.

    """
    M = len(matrix) - 1

    # Iterate over all of the "layers" of our matrix.
    for L in range(M):
        i = L
        # Swap all of the values in a given layer.
        while i < M - L:
            TL = matrix[L][i]
            TR = matrix[i][M - L]
            BR = matrix[M - L][M - i]
            BL = matrix[M - i][L]

            matrix[L][i] = BL
            matrix[i][M - L] = TL
            matrix[M - L][M - i] = TR
            matrix[M - i][L] = BR

            i += 1


# 1x1 matrix
image = [[1]]
rotate_matrix(image)
assert image == [
    [1]
]

# 2x2 matrix
image = [
    [1, 2],
    [3, 4]
]
rotate_matrix(image)
assert image == [
    [3, 1],
    [4, 2]
]

# 3x3 matrix
image = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate_matrix(image)
assert image == [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]

# 4x4 matrix
image = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
rotate_matrix(image)
assert image == [
    [13, 9, 5, 1],
    [14, 10, 6, 2],
    [15, 11, 7, 3],
    [16, 12, 8, 4]
]


def test_copy():
    i = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    i = zip(*i[::-1])


def test_inplace():
    i = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    rotate_matrix(i)


if __name__ == '__main__':
    import timeit

    copying = timeit.timeit(
        "test_copy()",
        setup="from __main__ import test_copy",
        number=100000
    )

    inplace = timeit.timeit(
        "test_inplace()",
        setup="from __main__ import test_inplace",
        number=100000
    )

    print('In-place is {} times faster than copying.'.format(copying / inplace))
