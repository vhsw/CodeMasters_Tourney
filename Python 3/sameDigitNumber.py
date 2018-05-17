# Given an integer, check that all the digits in the number are the same.


def sameDigitNumber(n):
    return len(set(str(n))) == 1