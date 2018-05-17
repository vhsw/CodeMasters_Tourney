# Given array of integers, find the maximal possible sum of some of its k consecutive elements.


def arrayMaxConsecutiveSum(inputArray, k):
    buf = inputArray[:k]
    res = []
    sum_ = sum(buf)
    res.append(sum_)
    for i in inputArray:
        buf.append(i)
        sum_ += buf[-1] - buf[0]
        res.append(sum_)
        buf.pop(0)
    return max(res)
