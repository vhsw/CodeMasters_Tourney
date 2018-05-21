# A string is said to be a correct sentence if it starts with the capital
# letter and ends with a full stop (.).
# Given a string, check whether it represents a correct sentence.


def isCorrectSentence(inputString):
    return 'A' <= inputString[0] <= 'Z' and inputString[-1] == '.'