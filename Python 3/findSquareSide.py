# Given a square's vertices in arbitrary order, find (the length of the square's side)^2.


def findSquareSide(x, y):
    res = float('inf')
    for px, py, x, y in zip(x, y, x[1:], y[1:]):
        res = min(res, (x - px) ** 2 + (y - py) ** 2)

    return res
