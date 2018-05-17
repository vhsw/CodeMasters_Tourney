# You are given an n × m matrix, which contains all the integers from 1 to n * m, inclusive, each exactly once.
# Initially you are standing in the cell containing the number 1. On each turn you are allowed to move to an adjacent cell, 
# i.e. to a cell that shares a common side with the one you are standing on now. It is prohibited to visit any cell more than once.
# Check if it is possible to visit all the cells of the matrix in the order of increasing numbers in the cells,
# i.e. get to the cell with the number 2 on the first turn, then move to 3, etc.


def findPath(matrix):

    positionX = -1
    positionY = -1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                positionX = i
                positionY = j
    for i in range(1, len(matrix) * len(matrix[0])):
        found = False
        nextX = -1
        nextY = -1
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx * dy == 0:
                    if (positionX + dx >= 0 and positionX + dx < len(matrix)
                    and positionY + dy >= 0 and positionY + dy < len(matrix[0])):
                        if matrix[positionX + dx][positionY + dy] == i + 1:
                            found = True
                            nextX = positionX + dx
                            nextY = positionY + dy
        if found:
            positionX = nextX
            positionY = nextY
        else:
            return False
    return True

