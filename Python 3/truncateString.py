# Consider the following operation on a string containing digits from 1 to 9:
# if the leftmost digit of the string is divisible by 3, remove it from the string;
# otherwise, if the rightmost digit of the string is divisible by 3, remove it from the string;
# otherwise, if the sum of two digits on the sides of the string is divisible by 3, remove both digits from the string;
# This operation is applied sequentially until the string is empty or neither of the three given conditions is met.
# For a given string find the result of applying the given algorithm to it.


def truncateString(s):

    def truncate(l, r):
        if l >= r:
            return ''
        newL = l
        newR = r
        left = ord(s[l]) - ord('0')
        right = ord(s[r - 1]) - ord('0')
        if left % 3 == 0:
            newL += 1
        elif right % 3 == 0:
            newR -= 1
        elif (left + right) % 3 == 0:
            newR -= 1
            newL += 1
        else:
            return s[l : r]

        return truncate(newL, newR)

    return truncate(0, len(s))
