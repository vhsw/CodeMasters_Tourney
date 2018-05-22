# Given an array of integers, count the odd numbers before the first
# (i.e. leftmost) occurrence of zero.

def oddNumbersBeforeZero(sequence):
    n = 0
    for i in sequence:
        if i == 0:
            return n
        n += i%2 != 0