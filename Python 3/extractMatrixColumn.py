# Given a rectangular matrix and an integer column,
# return an array containing the elements of the columnth column of the given matrix 
# (the leftmost column is the 0th one).


def extractMatrixColumn(matrix, column):
    return [row[column] for row in matrix]