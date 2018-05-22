# There are n houses in a village on a circular road numbered
# from 1 to n starting from some house in clockwise order.
# It takes one minute to get from one house to any of two adjacent houses
# and there are no other roads in this village besides the circular one.
# Find the minimal time required to make all visits in the desired order starting
# from house 1.

def visitsOnCircularRoad(n, visitsOrder):
    current  = 1
    time = 0
    for disired in visitsOrder:
        time += min(abs(disired - current), abs(n - abs(disired - current)))
        current = disired
    return time