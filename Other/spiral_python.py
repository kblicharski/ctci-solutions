"""
An algorithm for printing size N x M matrices in spiral order.

Time: O(NM)
Space: O(NM)

Relies on the use of four control variables to demarcate the
boundaries of the not-yet-printed numbers in our matrix.
"""

from typing import List


def spiral_order(A: List[List[int]]) -> List[int]:
    """
    Create a list representing the spiral order of a matrix.

    Implementation Notes:
        1. Because the range() function's second argument is exclusive,
        we need to increment/decrement the border variables respectively.
        2. When going from right to left or bottom to top, we need to pass
        in the -1 step argument to reverse our range() call.
        3. The while loop concludes after either T or L increments after
        reaching the "center" of the matrix.

    Args:
        A (Tuple[List[int]]): The given matrix.
    Returns:
        List[int]: The list representing the spiral ordering.

    """
    if len(A) == 1: return A[0]

    ordering = []
    
    T = 0
    B = len(A) - 1
    L = 0
    R = len(A[0]) - 1

    while (T <= B and L <= R):
        for i in range(L, R+1):
            ordering.append(A[T][i])
        T += 1
        for i in range(T, B+1):
            ordering.append(A[i][R])
        R -= 1
        for i in range(R, L-1, -1):
            ordering.append(A[B][i])
        B -= 1
        for i in range(B, T-1, -1):
            ordering.append(A[i][L])
        L += 1
        
    return ordering


# 3x3 matrix
assert spiral_order([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

# 3x2 matrix
assert spiral_order([
    [1, 2],
    [3, 4],
    [5, 6]
]) == [1, 2, 4, 6, 5, 3]

# 2x3 matrix
assert spiral_order([
    [1, 2, 3],
    [4, 5, 6]
]) == [1, 2, 3, 6, 5, 4]

# 2x2 matrix
assert spiral_order([
    [1, 2],
    [3, 4]
]) == [1, 2, 4, 3]

# 2x1 matrix
assert spiral_order([
    [1],
    [2]
]) == [1, 2]

# 1x2 matrix
assert spiral_order([
    [1, 2]
]) == [1, 2]

# 1x1 matrix
assert spiral_order([
    [1]
]) == [1]
