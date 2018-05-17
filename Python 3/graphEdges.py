# Count the number of different edges in a given undirected graph with no loops and multiple edges.


def graphEdges(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]:
                count += 1
    return count//2
