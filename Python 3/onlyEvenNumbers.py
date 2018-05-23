# Return a strictly increasing array of all even numbers
# between given left and right (both inclusive).


def onlyEvenNumbers(left, right):
    return [n for n in range(left, right + 1) if n%2 == 0]
