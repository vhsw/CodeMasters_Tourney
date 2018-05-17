# You found two items, for each of them you know their weight. You have a max weight capacity of maxW.
# If your weight capacity allows you to take with you both items, return "both". If you can take whichever one you want, return "either".
# If you cannot take any items, return "none". Otherwise, return "first" or "second" based on the index of the item which you can take.


def knapsackLight2(weight1, weight2, maxW):
    if weight1+weight2 <= maxW:
        return 'both'
    if weight1 <= maxW and weight2 <= maxW:
        return 'either'
    if weight1 <= maxW:
        return 'first'
    if weight2 <= maxW:
        return 'second'
    return 'none'
