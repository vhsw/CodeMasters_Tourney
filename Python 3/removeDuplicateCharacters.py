# Remove all characters from a given string that appear more than once in it.


def removeDuplicateCharacters(str):
    return ''.join(l for l in str if str.count(l) == 1)

def removeDuplicateCharacters(inputStr):
    charCount = {}
    newInputStr = []
    for i in range(len(inputStr)):
        char =  inputStr[i]
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1
    for i in range(len(inputStr)):
        if charCount[inputStr[i]] == 1:
            newInputStr.append(inputStr[i])
    return ''.join(newInputStr)
    