# For given n and k find the sum of all multiples of k that are not greater than n.


def sumOfMultiples(n, k):
    res = 0
    mul = 0
    while mul <= n:
        res += mul
        mul += k
    return res