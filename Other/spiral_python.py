"""
Problem:
    An algorithm for printing size N x M matrices in spiral order.

Implementation:
    Relies on the use of four control variables to demarcate the
    boundaries of the not-yet-printed numbers in our matrix.

    Additionally, a fifth variable functions as a flag for the direction
    we are currently traversing in. This is important for the special
    case where we have a matrix with more than two rows, but one column.

    One example is the assertion for an 8x1 matrix. For this reason,
    although it would be nice to delete all of the `elif` statements
    and direction assignments, we cannot.

Efficiency:
    Time: O(NM)
    Space: O(NM)

"""
from enum import Enum
from typing import List


class Direction(Enum):
    """An enum to define the cardinal directions."""
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


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

    direction = Direction.RIGHT

    while (T <= B and L <= R):
        if direction == Direction.RIGHT:
            for i in range(L, R+1):
                ordering.append(A[T][i])
            T += 1
            direction = Direction.DOWN
        elif direction == Direction.DOWN:
            for i in range(T, B+1):
                ordering.append(A[i][R])
            R -= 1
            direction = Direction.LEFT
        elif direction == Direction.LEFT:
            for i in range(R, L-1, -1):
                ordering.append(A[B][i])
            B -= 1
            direction = Direction.UP
        elif direction == Direction.UP:
            for i in range(B, T-1, -1):
                ordering.append(A[i][L])
            L += 1
            direction = Direction.RIGHT
            
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

# 1x8 matrix
assert spiral_order([
    [1, 2, 3, 4, 5, 6, 7, 8]
]) == [1, 2, 3, 4, 5, 6, 7, 8]


# 8x1 matrix
assert spiral_order([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8]
]) == [1, 2, 3, 4, 5, 6, 7, 8]
