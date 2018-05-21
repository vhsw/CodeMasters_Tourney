# Given a point and a circle, determine if the point lies strictly inside the circle.


def isInsideTheCircle(xa, ya, xc, yc, rc):
    dist = (xa - xc) * (xa - xc) + (ya - yc) * (ya - yc)
    rc *= rc
    if dist > rc:
        return True
    return False
