# Given an array of integers, find the maximal absolute
# difference between any two of its adjacent elements

def arrayMaximalAdjacentDifference(inputArray):
    return max(abs(a-b) for a,b in zip(inputArray, inputArray[1:]))
