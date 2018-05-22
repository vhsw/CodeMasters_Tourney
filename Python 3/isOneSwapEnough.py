# Given a string, check if a palindrome can be obtained from it
# by at most one swap of some pair of characters. 


def isOneSwapEnough(inputString):
    l = list(inputString)
    if l == l[::-1]:
        return True
    for i in range(1, len(l)):
        tmp = l[:]
        tmp[i-1], tmp[i] = tmp[i],tmp[i-1]
        if tmp == tmp[::-1]:
            return True 
    return False