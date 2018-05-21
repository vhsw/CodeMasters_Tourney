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

def primeFactors2(n):
    factors = []
    divisor = 2

    while n != 1:
        if n % divisor == 0:
            factors.append(divisor)
        while n % divisor == 0:
            n //= divisor
        divisor += 1

    return factors