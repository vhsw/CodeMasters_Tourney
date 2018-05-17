# Check if the given point belongs to the given line.


def pointInLine(point, line):

    if point[0] * line[0] + point[1] * line[1] +  line[2] == 0:
        return True
    return False
