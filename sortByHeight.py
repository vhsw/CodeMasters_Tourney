# Some people are standing in a row in a park. 
# There are trees between them which cannot be moved. 
# Your task is to rearrange the people by their heights in a non-descending order 
# without moving the trees.

def sortByHeight(a):
    for i in range(len(a)):
        minIndex = -1
        tmp = a[i]
        if a[i] == -1:
            continue
        for j in range(i + 1, len(a)):
            if a[j] != -1:
                if minIndex == -1 or a[j] < a[minIndex]:
                    minIndex = j
        a[i] = a[minIndex]
        a[minIndex] = tmp
    return a
