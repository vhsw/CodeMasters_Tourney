# Consider the following operation - we take a positive integer n 
# and replace it with the sum of its prime factors (if a prime number 
# is presented multiple times in the factorization of n, then it's counted
# the same number of times in the sum). This operation is applied sequentially
# first to the given number, then to the first result, then to the second
# result and so on, until the result remains the same.
# Given any number, find the final result of the operation.


def factorSum(n):

    prevValue = 0
    currentValue = 0
    nextValue = n

    while nextValue != prevValue:
        divisor = 2
        currentValue =  nextValue 
        prevValue = nextValue
        nextValue = 0
        while divisor * divisor <= currentValue:
            if currentValue % divisor == 0:
                currentValue /= divisor
                nextValue += divisor
            else:
                divisor += 1
        nextValue += currentValue

    return nextValue

