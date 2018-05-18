# Write an algorithm that constructs an array of non unique prime factors of a number n.


def primeFactors(n):
    res = []
    i = 2
    while i<=n:
        while n%i == 0:
            n//=i
            res.append(i)
        i+=1
    return res