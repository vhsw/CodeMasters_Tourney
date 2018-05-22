# You are given an array of integers representing coordinates of obstacles situated on a straight line.
# Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.
# Find the minimal length of the jump enough to avoid all the obstacles.


def avoidObstacles(inputArray):
    pos = 0
    step = 1
    while pos<=max(inputArray):
        if pos in inputArray:
            step+=1
            pos = 0
        else:
            pos += step
    return step
