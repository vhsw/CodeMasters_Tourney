# You have N sticks. Given an array of their lengths, find the number of triangles
# that can be constructed using any three of these sticks.
# Note that the sum of the lengths of any two sides of a triangle must be greater
# than the third side.
# Equal triangles that are constructed from different sticks are considered different.

import itertools


def numberOfTriangles2(sticks):
    count = 0
    for a, b, c in list(itertools.combinations(sticks, 3)):
        count += ((a + b) < c)
    return count
