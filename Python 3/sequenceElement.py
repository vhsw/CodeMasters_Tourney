# Consider an infinite sequence a of decimal digits which is generated using the following algorithm:
# the first 5 digits are initially given;
# for i > 4, a[i] = (a[i - 5] + a[i - 4] + a[i - 3] + a[i - 2] + a[i - 1]) % 10, 
# i.e. each element starting with the fifth is the sum of the previous five elements modulo 10.
# Given the initial five elements, You need to find the nth element of the sequence
# (the first element has index 0).

def sequenceElement(a, n):

    MOD = 10**5
    seq = []
    for i in range(5):
        seq.append(a[i])

    lastFive = (a[0] * 10**4 + a[1] * 10**3 +
                a[2] * 10**2 + a[3] * 10 + a[4])
    was = {}
    was[lastFive] = 4

    i = 5
    while True:
        seq.append((seq[i - 1] + seq[i - 2] +
                    seq[i - 3] + seq[i - 4] + seq[i - 5]) % 10)
        lastFive = (lastFive * 10 + seq[i]) % MOD
        if lastFive in was:
            last = was[lastFive]
            return seq[n%(i - last)]
        else:
            was[lastFive] = i
        i += 1

