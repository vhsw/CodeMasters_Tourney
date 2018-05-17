# Given an array of strings, produce a single string as follows:
# Repeat the following steps while there is more than one string in the array:
# find the shortest string in the array (if there are several strings of the same length take the leftmost one);
# find the shortest string among the rest (if there are several strings of the same length take the rightmost one);
# extract the chosen strings from the array;
# append the result of their concatenation (the second string should be added to the end of the first string) to the right end of the array.
# After the algorithm has finished, there will be a single string left in the array. Return that string.


def concatenationProcess(init):
    while len(init) > 1:
        print(init)
        idx_l, short_l = min(enumerate(init), key=lambda t: len(t[1]))
        init.pop(idx_l)
        idx_r, short_r = min(
            reversed(list(enumerate(init))), key=lambda t: len(t[1]))
        init.pop(idx_r)
        init.append(short_l+short_r)
    return init[0]
