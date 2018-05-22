# Two two-dimensional arrays are isomorphic if they have the same number of rows
# and each pair of respective rows contains the same number of elements.
# Given two two-dimensional arrays, check if they are isomorphic.


def areIsomorphic(array1, array2):
    return len(array1) == len(array2) and all(len(a) == len(b) for a, b in zip(array1, array2))