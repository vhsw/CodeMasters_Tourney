# Given two version strings composed of several non-negative decimal fields
# separated by periods ("."), both strings contain equal number of numeric fields.
# Return true if the first version is higher than the second version and false otherwise.


def higherVersion(ver1, ver2):

    a = ver1.split('.')
    b = ver2.split('.')
    for i in range(len(a)):
        cmp_ = int(a[i]) - int(b[i])
        if cmp_ > 0:
            return True
        elif cmp_ < 0:
            return False

    return  False

