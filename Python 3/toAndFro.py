# A person is moving along a straight line. Initially he is at point A.
# He goes to point B from A with speed equal to 1 meter per second.
# Immediately after reaching B he turns around and heads to A from B with
# the same speed. After reaching point A he turns around once again and heads to B. etc.
# We need an algorithm that identifies the location of the person at any given moment in time.
# It's guaranteed that A and B are two different points.


def toAndFro(a, b, t):

    length = abs(a - b)
    t %= 2 * length
    if t <= length:
        return a + (b - a) / abs(b - a) * t
    else:
        t -= length
        return b + (a - b) / abs(a - b) * t