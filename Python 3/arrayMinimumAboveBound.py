# Given an array of integers inputArray and an integer bound, find the smallest array element strictly greater than bound.


def arrayMinimumAboveBound(inputArray, bound):
    t = [x for x in inputArray if x > bound]
    return min(t)
