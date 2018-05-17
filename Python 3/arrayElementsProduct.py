# Given an array of integers, find the product of its elements.


def arrayElementsProduct(inputArray):

    result =  inputArray[0]

    for i in range(1, len(inputArray)):
        result *= inputArray[i]
    return result
