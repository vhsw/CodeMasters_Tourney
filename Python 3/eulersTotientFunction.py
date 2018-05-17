# Given an integer n, find the value of phi(n), where phi is Euler's totient function.


import math


def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount


def eulersTotientFunction(n):
    return phi(n)
