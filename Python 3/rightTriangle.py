# For a given triangle determine if it is a right triangle.


def rightTriangle(sides):
    a,b,c = sorted(sides)
    return (a*a + b*b) == (c*c)