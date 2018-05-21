# Given an array of integers, find the rightmost round number
# in it and output its position in the array (0-based).
# If there are no round numbers in the given array, output -1.


def rightmostRoundNumber(inputArray):

    ans = -1
    for i in range(len(inputArray)):
        if inputArray[i] % 10 == 0:
            ans = i

    return ans