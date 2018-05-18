# Given integers n, l and r, find the number of ways 
# to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.


def countSumOfTwoRepresentations3(n, l, r):
    result = 0

    i = 1
    while i <= n - i:
        if  i >= l and i <= r and n - i >= l and n - i <= r :
            result += 1
        i += 1

    return result