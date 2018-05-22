# Given a rectangular matrix of integers and integers n and m,
# we are looking for the submatrix of size n × m that has the maximal sum
# among all submatrices of the given size.


def maxSubmatrixSum(matrix, n, m):
    return max(sum(matrix[i + x][j + y] for y in range(m) for x in range(n))
               for i in range(len(matrix) - n + 1)
               for j in range(len(matrix[0]) - m + 1))

