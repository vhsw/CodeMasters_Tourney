# Define GCPD (Greatest Common Prime Divisor) as the largest prime number
# that divides both given positive integers. Your task is to find GCPD 
# of the given integers a and b.


def greatestCommonPrimeDivisor(a, b):
    def is_prime(x):
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                return False 
        return True 
    for i in reversed(range(2, min(a, b))):
        if a % i == 0 and b % i == 0 and is_prime(i):
            return i 
    return -1