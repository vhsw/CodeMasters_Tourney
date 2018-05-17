# Given a string, find the number of different non-empty substrings in it.


def differentSubstrings(inputString):

    substrings = []
    result = 1

    for i in range(len(inputString)):
        for j in range(i + 1, len(inputString) + 1):
            substrings.append(inputString[i:j])
    substrings.sort()
    for i in range(1, len(substrings)):
        if substrings[i] != substrings[i - 1]:
            result += 1

    return result

