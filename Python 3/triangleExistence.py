# Check the existence of a triangle with the given side lengths. A necessary and sufficient condition for triangle existence is that the sum of any two of its sides must be strictly greater than the third side.


def triangleExistence(sides):
    sides.sort()
    return sides[0]+sides[1] > sides[2]
