# Given a sequence, check whether it is cyclic increasing.


def cyclicSequence(s):
    m = s.index(min(s))
    s=s[m:]+s[:m]
    return all(x<y for x, y in zip(s, s[1:]))
