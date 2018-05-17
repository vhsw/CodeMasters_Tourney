# Change the capitalization of all letters in a given string.


def swapCase(text):

    answer = []

    for i in range(len(text)):
        if text[i] == text[i].upper():
            answer.append(text[i].lower())
        else:
            answer.append(text[i].upper())
    return ''.join(answer)
