# You have a set of balls that are colored in such a way that there is ballsPerColor balls of each of the given number of colors. You also have an infinite number of boxes of the same max capacity boxSize.
# You distribute the balls among the boxes as follows:
# first you fill up the first box, then the second, etc.
# first you use all of the balls of the first color, then all of the balls of the second color, etc.
# Find the number of colors for which there is more than one box that contains a ball of that color.


def ballsDistribution(colors, ballsPerColor, boxSize):

    currentBox = 0
    capacity = boxSize
    result = 0

    for i in range(colors):
        startBox = currentBox
        for j in range(ballsPerColor):
            capacity -= 1
            if capacity <= 0:
                currentBox += 1
                capacity = boxSize
        if startBox < currentBox and capacity < boxSize or startBox + 1 < currentBox:
            result += 1

    return result
