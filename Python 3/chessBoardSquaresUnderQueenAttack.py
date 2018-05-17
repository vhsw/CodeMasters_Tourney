# Consider a rectangular chess board of a × b squares. For each of the squares imagine a lone queen standing on that square and compute the number of squares under the queen's attack. Add all the numbers you got for each of the a × b possible queen's positions.


def chessBoardSquaresUnderQueenAttack(a, b):

    def go(x, y, dx, dy):
        if x < 0 or x >= a or y < 0 or y >= b:
            return 0
        return go(x + dx, y + dy, dx, dy) + 1

    res = 0

    for i in range(a):
        for j in range(b):
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx != 0 or dy != 0:
                        res += go(i + dx, j + dy, dx, dy)

    return res
