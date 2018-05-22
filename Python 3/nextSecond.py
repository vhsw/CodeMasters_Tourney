# Given some time output the time after one second.


def nextSecond(currentTime):

    if currentTime[2] == 59:
        currentTime[2] = 0
        if currentTime[1] == 59:
            currentTime[0] = (currentTime[0] + 1)%24
            currentTime[1] = 0
        else:
            currentTime[1] += 1
    else:
        currentTime[2] += 1

    return currentTime