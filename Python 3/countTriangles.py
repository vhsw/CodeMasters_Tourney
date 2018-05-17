# Given a set of points, find the number of triangles with non-zero areas formed by some trio of the given points.


def countTriangles(x, y):
    count = 0

    def check(a, b, c):
        x1, y1, x2, y2, x3, y3 = a[0], a[1], b[0], b[1], c[0], c[1]
        return abs((x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)) != 0
    import itertools
    t = itertools.combinations(zip(x, y), 3)
    t = list(t)
    for i in t:
        print(i)
        if check(i[0], i[1], i[2]):
            count += 1
    return count
