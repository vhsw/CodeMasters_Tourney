# Let's call product(x) the product of x's digits. Given an array of integers a, calculate product(x) for each x in a, and return the number of distinct results you get.


def uniqueDigitProducts(a):
    def p(n):
        res = 1
        for d in str(n):
            res *= int(d)
        return res
    
    return len(set(p(n) for n in a))