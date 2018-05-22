# Given an integer index n, find the nth Fibonacci number.

def fibonacciNumber(n):

    fibs = [0, 1]
    for i in range(2, n + 1):
        fibs.append(fibs[i-1] + fibs[i - 2])

    return fibs[n]


