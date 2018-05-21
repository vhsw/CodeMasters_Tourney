# Apply union operation to the given sets of integers.
# Sets may contain duplicate elements.


def setUnion(a, b):

    c = []
    pos_b = 0

    a.sort()
    b.sort()

    for pos_a in range(len(a)):
        while pos_b < len(b) and b[pos_b] < a[pos_a]:
            c.append(b[pos_b])
            pos_b += 1
        c.append(a[pos_a])
        if pos_b < len(b) and a[pos_a] == b[pos_b]:
            pos_b += 1
    while pos_b < len(b):
        c.append(b[pos_b])
        pos_b += 1

    return c