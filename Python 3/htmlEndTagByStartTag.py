# You are implementing your own HTML editor. To make it more comfortable for developers you would like to add an auto-completion feature to it.
# Given the starting HTML tag, find the appropriate end tag which your editor should propose.


def htmlEndTagByStartTag(startTag):

    result = ['<', '/']
    position = 1
    while startTag[position] != ' ' and startTag[position] != '>':
        result.append(startTag[position])
        position += 1
    result.append('>')
    return ''.join(result)
