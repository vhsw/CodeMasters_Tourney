# Define l-r-segment number as the number formed by concatenating all the digits from l to r in ascending order.
# Given l and r (l ≤ r), return the l-r-segment number.


def lrSegmentNumber(l, r):
    return int(''.join(str(n) for n in range(l,r+1)))