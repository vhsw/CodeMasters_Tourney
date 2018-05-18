# Find the sum of all digits that occur in a string.


def sumUpDigits(inputString):
    return sum(int(i) for i in inputString if i.isdigit())