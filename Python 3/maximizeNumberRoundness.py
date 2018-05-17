# Given an integer n, find the minimum number of swaps required to maximize n's roundness.

def maximizeNumberRoundness(n):
    return int('0' in str(n).rstrip('0'))