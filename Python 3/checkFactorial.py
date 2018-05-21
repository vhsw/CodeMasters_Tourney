# Given an integer n, check if n = k! for some non-negative integer k.


def checkFactorial(n):
    c = 1
    i = 1
    while c<=n:
        if c == n:
            return True
        c *= i
        i+=1
    return False