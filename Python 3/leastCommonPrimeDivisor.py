# Calculate the LCPD (least common prime divisor) of two numbers.


def leastCommonPrimeDivisor(a, b):
    def is_prime(x):
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                return False 
        return True 
    for i in range(2, max(a, b)):
        if a % i == 0 and b % i == 0 and is_prime(i):
            return i 
    return -1