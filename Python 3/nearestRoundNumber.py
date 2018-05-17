# Find the smallest round number that is not less than a given value.


import math

def nearestRoundNumber(value):
    return math.ceil(value/10)*10
