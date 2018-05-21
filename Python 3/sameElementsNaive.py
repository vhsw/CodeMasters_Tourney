# Find the number of elements that are contained in both of the given arrays.


def sameElementsNaive(a, b):
    return sum(1 for i in a if i in b)