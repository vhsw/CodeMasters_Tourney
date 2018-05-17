# Given an array of integers inputArray and an integer extraElement, remove all the elements which are equal to extraElement from inputArray.


def myFilter(inputArray, extraElement):

    result = []
    for i in range(0, len(inputArray)):
        if inputArray[i] == extraElement:
            continue
        result.append(inputArray[i])

    return result
