# Given a set of points on the plane, find the area of its axis-aligned minimum bounding box.


def axisAlignedBoundingBox(x, y):
    return (max(x) - min(x))*(max(y) - min(y))
