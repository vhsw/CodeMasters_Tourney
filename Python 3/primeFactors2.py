# Find all distinct prime factors of a given integer.


def primeFactors2(n):
    i = 2
    res = []

    while i <= n:
        while n % i == 0:
            n //= i
            if i not in res:
                res.append(i)
        i += 1
    return res
