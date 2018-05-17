# Given a positive integer, check if it doesn't contain a pair of adjacent bits set to 1 in its binary representation.


def noAdjacentBits(a):
    lastBit = 0
    idx = 0
    while (1 << idx) <= a:
        curBit = a & (1 << idx) > 0
        if lastBit == 1 and curBit == 1:
            return False
        lastBit = curBit
        idx += 1

    return True
