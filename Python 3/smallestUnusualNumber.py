# Let's call an integer unusual if the sum of its digits is larger than the product of its digits. For example, the numbers 21 and 990 are unusual, while the numbers 22 and 991 aren't.
# Given an integer a (represented as a string), find the smallest unusual integer x such that x ≥ a. Since both x and a can be very large, return the value of x - a.


def smallestUnusualNumber(a):
    s = 0
    p = 1
    for d in a:
        d = int(d)
        s += d
        p *= d
        if d == 0:
            return 0

    if s > p:
        return 0
    return 10 - int(a[len(a) - 1])
