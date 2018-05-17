# Given an integer n, find the number of trailing zeros in the decimal representation of n! (the exclamation mark means factorial).


def factorialTrailingZeros(n):
    m = 1
    for i in range(1, n+1):
        m *= i

    res = 0
    while m % 10 == 0:
        m //= 10
        res += 1
    return res
