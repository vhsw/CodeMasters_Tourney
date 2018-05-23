# Given a string, find the number of different non-empty substrings in it.


def differentSubstringsTrie(inputString):

    def addNode(lastVersion):
        line = []
        for i in range(26):
            line.append(0)
        lastVersion.append(line)

    nodesCount = 1
    trie = []
    addNode(trie)

    for i in range(len(inputString)):
        currentNode = 0
        for j in range(i, len(inputString)):
            symbol = ord(inputString[j]) - ord('a')
            if trie[currentNode][symbol] == 0:
                addNode(trie)
                trie[currentNode][symbol] = nodesCount
                nodesCount += 1
            currentNode = trie[currentNode][symbol]

    return nodesCount - 1

