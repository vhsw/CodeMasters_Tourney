# Consider an array of integers a. Let min(a) be its minimal element, and let avg(a) be its mean.
# Define the center of the array a as array b such that:
# b is formed from a by erasing some of its elements.
# For each i, |b[i] - avg(a)| < min(a).
# b has the maximum number of elements among all the arrays satisfying the above requirements.
# Given an array of integers, return its center.


def arrayCenter(a):
    min_ = min(a)
    avg = sum(a)/len(a)
    return [e for e in a if abs(e-avg) < min_]
