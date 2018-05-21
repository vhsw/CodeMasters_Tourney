# Implement a function that can reduce a fraction.

import math
def fractionReducing(fraction):
    g = math.gcd(*fraction)
    a, b = fraction
    return [a // g, b // g]