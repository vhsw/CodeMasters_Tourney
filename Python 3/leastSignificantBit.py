# Given a positive integer n, construct a number which has a single 1 bit,
# which is at the position of the least significant 1 bit in n.


def leastSignificantBit(n):

    ans = 1
    while ((n & 1) == 0):
        n >>= 1
        ans *= 2

    return ans
