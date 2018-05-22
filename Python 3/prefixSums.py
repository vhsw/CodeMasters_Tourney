# Construct an array b of prefix sums of the given array a.
# b is defined as:
#   b[0] = a[0]
#   b[1] = a[0] + a[1]
#   b[2] = a[0] + a[1] + a[2]
#   ...
#   b[n - 1] = a[0] + a[1] + ... + a[n - 1]
# where n is the length of a.


def prefixSums(a):

    b = [ a[0] ]
    for i in range(1, len(a)):
        b.append(b[i-1] + a[i])

    return b
