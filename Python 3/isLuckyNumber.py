# Lucky numbers are the positive integers whose decimal representations contain only the lucky digits 4 and 7.


def isLuckyNumber(n):
    for i in str(n):
        if i not in ['4', '7']:
            return False
    return True
