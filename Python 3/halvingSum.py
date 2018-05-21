# Given a positive integer n, calculate the following sum: n + n/2 + n/4 + n/8 + ...
# All divisions are integer.


def halvingSum(n):
    s = 0
    while n:
        s += n
        n //= 2
    return s