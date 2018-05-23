# Given the center and the radius of a circle and the coordinates of a point determine if the point is inside (or on the border of) the circle.


def insideCircle(point, center, radius):
    x = point[0] - center[0]
    y = point[1] - center[1]
    return (x**2 + y**2) <= radius**2
