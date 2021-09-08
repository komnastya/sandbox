from typing import List

Matrix = List[List[int]]  # Type Alias


# Tests whether the given matrix is square.
# Example: [] -> True
# Example: [[1]] -> True
# Example: [[1,2],[3,4]] -> True
# Example: [[1],[2]] -> False
def is_square(matrix: Matrix) -> bool:
    for row in matrix:
        if len(row) != len(matrix):
            return False
    return True


# Returns sum of the given matrices.
def matrix_sum(a: Matrix, b: Matrix) -> Matrix:
    if len(a) != len(b):
        raise ValueError
    rows = []
    for i in range(len(a)):
        columns = []
        for j in range(len(a[i])):
            x = a[i][j] + b[i][j]
            columns.append(x)
        rows.append(columns)
    return rows
