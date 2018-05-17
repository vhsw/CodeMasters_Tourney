# Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.


def differentSquares(matrix):
    def to_num(array):
        res = ''
        for row in array:
            for el in row:
                res+=str(el)
        return int(res)
    array = []
    lenx = len(matrix) - 1
    leny = len(matrix[0]) - 1
    for i in range(0, leny):
        for j in range(0, lenx):
            array += [[matrix[k][i:i + 2] for k in range(j, j + 2)]]
    iarray = []
    for el in array:
        iarray.append(to_num(el))

    return len(set(iarray))