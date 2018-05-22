# Given an array of integers, find the number of inversions it contains.


def countInversionsNaive(inputArray):

    result = 0

    for i in range(len(inputArray)):
        for j in range(i + 1, len(inputArray)):
            if inputArray[j] < inputArray[i]:
                result += 1
    return result

