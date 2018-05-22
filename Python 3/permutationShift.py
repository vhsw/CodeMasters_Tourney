# Define the permutation element shift as the difference between the element's value and its index. For example, for permutation [1, 0, 2, 3] of array [0, 1, 2, 3] shifts for the respective elements are [1, -1, 0, 0].
# Define the permutation shift as the difference between the maximal and the minimal element shifts among all of the permutation elements.
# Given a permutation of integers from 0 to n - 1 for some integer n, find its shift.


def permutationShift(permutation):
    dist = [permutation[i] - i for i in range(len(permutation))]
    return max(dist) - min(dist)
