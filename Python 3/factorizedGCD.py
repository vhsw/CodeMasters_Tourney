# Find the greatest common divisor of two given integers. 
# Each integer is given in the form of its prime factorization - 
# a sorted array of all prime factors of the number.


def factorizedGCD(a, b):
    j = 0
    result = 1
    for i in range(len(a)):
        while j < len(b) and a[i] > b[j]:
            j += 1
        if j < len(b) and a[i] == b[j]:
            result *= a[i]
            j += 1
    return result
