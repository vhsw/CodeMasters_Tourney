# Given the first two elements of an arithmetic progression, find its nth element.


def arithmeticProgression(element1, element2, n):
    return element1 + (element2-element1) * (n-1)
