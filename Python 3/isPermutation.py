# Given a certain array, find out if it's a permutation of numbers from 1 to a given integer.


def isPermutation(n, inputArray):
    return sorted(inputArray) == list(range(1, n+1))