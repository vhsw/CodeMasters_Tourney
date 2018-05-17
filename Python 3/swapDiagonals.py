# The longest diagonals of a square matrix are defined as follows:
# the first longest diagonal goes from the top left corner to the bottom right one;
# the second longest diagonal goes from the top right corner to the bottom left one.
# Given a square matrix, your task is to swap its longest diagonals by exchanging their elements at the corresponding positions.


def swapDiagonals(matrix):
    for i in range(len(matrix)):
        matrix[i][i], matrix[i][-i-1] = matrix[i][-i-1], matrix[i][i]
    return matrix
