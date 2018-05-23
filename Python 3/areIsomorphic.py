# Two two-dimensional arrays are isomorphic if they have the same number of rows
# and each pair of respective rows contains the same number of elements.
# Given two two-dimensional arrays, check if they are isomorphic.


def areIsomorphic(array1, array2):

    if len(array1) != len(array2):
        return False

    for i in range(len(array1)):
        if len(array1[i]) != len(array2[i]):
            return False

    return True