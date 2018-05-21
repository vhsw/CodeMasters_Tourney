# Given a set of points, find the number of triangles with non-zero areas formed by some trio of the given points.

import itertools
def countTriangles(x, y):
    count = 0
    for a,b,c in list(itertools.combinations(zip(x, y), 3)):
        count += (abs(( b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])) != 0)
    return count
