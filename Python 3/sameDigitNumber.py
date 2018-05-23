# Given an integer, check that all the digits in the number are the same.


def sameDigitNumber(n):
    digit = n % 10
    while n != 0:
        if n % 10 != digit:
            return False
        n //= 10
    return True


def sameDigitNumber_(n):
    return len(set(str(n))) == 1