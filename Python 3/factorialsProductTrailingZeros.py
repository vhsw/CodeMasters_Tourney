# Given integers l and r, find the number of trailing zeros in the decimal representation of
# l! * (l + 1)! * ... * r! (the exclamation mark means factorial).


def factorialsProductTrailingZeros(l, r):
    result = 0
    last = 0
    for i in range(1, r + 1):
        number = i
        while number % 5 == 0:
            number /= 5
            last += 1
        if i > l:
            result += last
    return result

