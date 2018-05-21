# Return a sorted array of all non-negative numbers less than the given n which are divisible both by 3 and 4.


def threeAndFour(n):
    res = []
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            res.append(i)
    return res
