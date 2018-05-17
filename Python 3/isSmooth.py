# An array is called smooth if its first and its last elements are equal to one another and to the middle. Given an array arr, determine if it is smooth or not.


def isSmooth(arr):
    l = len(arr)
    if l%2==0:
        mid = arr[l//2-1] + arr[l//2]
    else:
        mid = arr[l//2]
    return arr[0] == mid == arr[-1]