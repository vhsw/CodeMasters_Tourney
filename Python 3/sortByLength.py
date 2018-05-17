# Given an array of strings, sort them in the order of increasing lengths.
# If two strings have the same length, their relative order must be the same as in the initial array.

def sortByLength(inputArray):
    return sorted(inputArray, key=len)
