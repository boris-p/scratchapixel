# given an mXn matrix. If an element is 0, set its entire row and column to 0
# do this in place


# initialize an array with empty values:
# new_matrix = [[1] * cols for i in range(rows)]
# matrix[i] = [0] * cols

from typing import List


def set_matrix_zeroes_old(matrix: List[List[int]]) -> None:
    rows = len(matrix)
    cols = len(matrix[0])

    zero_rows = set()
    zero_cols = set()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(i)

    for i in zero_rows:
        matrix[i] = [0] * cols
    for i in range(rows):
        for j in zero_cols:
            matrix[i][j] = 0


def set_matrix_zeroes(matrix: List[List[int]]) -> None:
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                matrix[0][j] = 2
                matrix[i][0] = 2

    for i in range(rows):
        if matrix[i][0] == 2:
            matrix[i] = [0] * cols

    for j in range(cols):
        if matrix[0][j] == 2:
            for i in range(rows):
                matrix[i][j] = 0


input = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
]

expected_output = [
    [1, 0, 1],
    [0, 0, 0],
    [1, 0, 1],
]

set_matrix_zeroes(input)

print(input)
assert(input) == expected_output
