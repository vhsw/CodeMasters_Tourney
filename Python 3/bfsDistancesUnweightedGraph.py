# Given the adjacency matrix of the connected undirected graph
# with no loops or multiple edges and the index of the start vertex,
# find the distances between the start vertex and each vertex of the graph.

def bfsDistancesUnweightedGraph(matrix, startVertex):
    n = len(matrix)
    visited = [False]*n
    queue = [startVertex]
    distance = [0]*n
    while len(queue):
        currentVertex = queue.pop(0)
        for nextVertex in range(n):
            if matrix[currentVertex][nextVertex] and not visited[nextVertex]:
                visited[nextVertex] = True
                distance[nextVertex] = distance[currentVertex] + 1
                queue.append(nextVertex)

    distance[startVertex] = 0
    return distance
