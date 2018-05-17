# How many strings equal to a can be constructed using letters from the string b? Each letter can be used only once and in one string only.


def stringsConstruction(a, b):
    return min([b.count(l)//a.count(l) for l in a])
