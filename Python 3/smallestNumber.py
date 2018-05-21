# The algorithm should return the smallest non-negative integer of N digits length.


def smallestNumber(n):

    if n == 1:
        return 0

    res = 1

    for i in range(n):
        res *= 10

    return res

