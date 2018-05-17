# Remove all characters from a given string that appear more than once in it.


def removeDuplicateCharacters(str):
    return ''.join(l for l in str if str.count(l) == 1)
