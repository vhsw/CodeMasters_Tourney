# Let the integer n be represented by digits a1, a2, ..., ak 
# (the digits are listed from left to right in the order they appear 
# in the decimal representation of n).
# Define bi = |ai + 1 - ai|.
# Construct the number from the digits b1, b2, ..., bk - 1 (in that order).
# Let's call the resulting value a digit distance number for n.


def digitDistanceNumber(n):
    diff_concat = ''
    n = str(n)
    for i in range(len(n) - 1):
        diff_concat += str(abs(int(n[i]) - int(n[i + 1])))
    return int(diff_concat)
