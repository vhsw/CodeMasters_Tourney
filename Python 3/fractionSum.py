# Implement a function that can sum two reduced fractions and produce a new one.

import math


def fractionSum(a, b):
    u = a[0]*b[1] + b[0]*a[1]
    d = a[1]*b[1]

    g = math.gcd(u, d)
    return [u/g, d/g]
