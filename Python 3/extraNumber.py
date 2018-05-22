# You're given three integers, a, b and c. It is guaranteed that two of these
# integers are equal to each other. What is the value of the third integer?

def extraNumber(a, b, c):
    if a == b:
        return c
    if b == c:
        return a
    return b