# Given integers n and k, find the kth divisor (1-based) of n or determine if n has less than k divisors.


def kthDivisor(n, k):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    if len(divisors) < k:
        return -1
    else:
        return divisors[k - 1]
