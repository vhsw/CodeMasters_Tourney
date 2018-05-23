# Given integers a and b, determine whether the following 
# pseudocode results in an infinite loop
# while a is not equal to b do
#   increase a by 1
#   decrease b by 1


def isInfiniteProcess(a, b):
    return (a - b) % 2 != 0 or a > b