# Given an integer, find the number of the ways to change
# exactly one digit in it in order to obtain a bigger integer.


def countWaysToChangeDigit(value):
    answer = 0
    while value > 0:
        answer += 9 - value % 10
        value //= 10
    return answer